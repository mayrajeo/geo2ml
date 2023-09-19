# geo2ml

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

- Sampling features from a raster using point geometries or polygons
- Tiling larger rasters and shapefiles into smaller patches
- Rasterizing polygon geometries for semantic segmentation tasks
- Converting vector data to COCO and YOLO formats and creating required
  dataset files
- Visualization of generated datasets

## Install

First install GDAL to your system. If you use conda then installing
`rasterio` is enough, but with pip use instructions from
<https://pypi.org/project/GDAL/>.

Then you can install the package by

``` bash
pip install git+git://github.com/mayrajeo/geo2ml.git
```

If you want to have an editable install then first clone the repository

``` bash
git clone https://github.com/mayrajeo/geo2ml.git
cd geo2ml
pip install -e .
```

## How to use

Running `geo2ml_help` shows all available commands. Documentation for
each command is found by running for example
`geo2ml_sample_points --help`
