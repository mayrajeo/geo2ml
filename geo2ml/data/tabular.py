# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/10_data.tabular.ipynb.

# %% auto 0
__all__ = ['array_to_longform', 'drop_small_classes', 'sample_raster_with_points', 'sample_raster_with_polygons']

# %% ../../nbs/10_data.tabular.ipynb 3
from fastcore.basics import *
import pandas as pd
import numpy as np
import geopandas as gpd
import rasterio as rio
import logging
from rasterstats import zonal_stats
from pathlib import Path

# %% ../../nbs/10_data.tabular.ipynb 7
def array_to_longform(a: pd.DataFrame, columns: list) -> pd.DataFrame:
    "Convert pd.DataFrame `a` to longform array"
    dfa = pd.DataFrame(data=a, columns=columns)
    dfa = dfa.reset_index()
    return dfa.melt(id_vars=["index"], ignore_index=False)

# %% ../../nbs/10_data.tabular.ipynb 8
def drop_small_classes(
    df: pd.DataFrame, min_class_size: int, target_column: str | int = 0
) -> pd.DataFrame:
    "Drop rows from the dataframe if their `target_column` value has less instances than `min_class_size"
    if type(target_column) == int:
        target = df.columns[0]
    else:
        target = target_column
    drop_classes = (
        df[target]
        .value_counts()[df[target].value_counts() < min_class_size]
        .index.values
    )
    drop_series = ~df[target].isin(drop_classes)
    logging.info(f"Classes with less than {min_class_size} were dropped:")
    logging.info(drop_classes)
    return df.loc[drop_series, :]

# %% ../../nbs/10_data.tabular.ipynb 17
def sample_raster_with_points(
    sampling_locations: Path,
    input_raster: Path,
    target_column: str,
    band_names: list[str] = None,
    rename_target: str = None,
) -> gpd.GeoDataFrame:
    "Extract values from `input_raster` using points from `sampling_locations`. Returns a `gpd.GeoDataFrame` with columns `target_column`, `geometry` and bands"

    gdf = gpd.read_file(sampling_locations)

    with rio.open(input_raster) as src:
        assert str(gdf.crs) == str(
            src.crs
        ), "Sampling locations and input raster have different crs"
        coords = [(x, y) for x, y in zip(gdf.geometry.x, gdf.geometry.y)]
        values = np.array([p for p in src.sample(coords)])
        prof = src.profile

    bands = [f"band_{i}" for i in range_of(values[0])]

    out_gdf = gdf[[target_column, "geometry"]].copy()

    if band_names:
        assert len(bands) == len(
            band_names
        ), f"Mismatch provided band names ({len(band_names)}) and number of bands in raster ({len(bands)})"
        bands = band_names

    if target_column in bands:
        if not rename_target:
            raise Exception(
                "One of the band names is the same as target column. Provide rename_target"
            )
        out_gdf.rename(columns={target_column: rename_target}, inplace=True)
    elif rename_target:
        out_gdf.rename(columns={target_column: rename_target}, inplace=True)

    for i, b in enumerate(bands):
        out_gdf[b] = values[:, i].astype(prof["dtype"])
    return out_gdf

# %% ../../nbs/10_data.tabular.ipynb 24
def sample_raster_with_polygons(
    sampling_locations: Path,
    input_raster: Path,
    target_column: str = None,
    band_names: list[str] = None,
    rename_target: str = None,
    stats: list[str] = ["min", "max", "mean", "count"],
    categorical: bool = False,
) -> gpd.GeoDataFrame:
    "Extract values from `input_raster` using polygons from `sampling_locations` with `rasterstats.zonal_stats` for all bands"

    gdf = gpd.read_file(sampling_locations)
    with rio.open(input_raster) as src:
        assert str(gdf.crs) == str(
            src.crs
        ), "Sampling locations and input raster have different crs"
        n_bands = src.count
        prof = src.profile
    zstats = []
    for i in range(n_bands):
        zstats.append(
            zonal_stats(
                gdf, input_raster, band_num=i + 1, categorical=categorical, stats=stats
            )
        )

    out_gdf = gdf[[target_column, "geometry"]].copy()

    bands = [f"band_{i}" for i in range(n_bands)]

    if band_names:
        assert len(bands) == len(
            band_names
        ), f"Mismatch provided band names ({len(band_names)}) and number of bands in raster ({len(bands)})"
        bands = band_names

    if target_column in bands:
        if not rename_target:
            raise Exception(
                "One of the band names is the same as target column. Provide rename_target"
            )
        out_gdf.rename(columns={target_column: rename_target}, inplace=True)
    elif rename_target:
        out_gdf.rename(columns={target_column: rename_target}, inplace=True)

    for i, b in enumerate(bands):
        temp = pd.json_normalize(data=zstats[i])
        temp.rename(columns={c: f"{b}_{c}" for c in temp.columns}, inplace=True)
        out_gdf = out_gdf.join(temp)

    return out_gdf
