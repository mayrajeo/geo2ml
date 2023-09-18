# Autogenerated by nbdev

d = { 'settings': { 'branch': 'main',
                'doc_baseurl': '/geo2ml',
                'doc_host': 'https://mayrajeo.github.io',
                'git_url': 'https://github.com/mayrajeo/geo2ml',
                'lib_path': 'geo2ml'},
  'syms': { 'geo2ml.cli': {'geo2ml.cli.chelp': ('cli.html#chelp', 'geo2ml/cli.py')},
            'geo2ml.data.coordinates': { 'geo2ml.data.coordinates._reduce_geom_precision': ( 'data.coordinates.html#_reduce_geom_precision',
                                                                                             'geo2ml/data/coordinates.py'),
                                         'geo2ml.data.coordinates.affine_transform_gdf': ( 'data.coordinates.html#affine_transform_gdf',
                                                                                           'geo2ml/data/coordinates.py'),
                                         'geo2ml.data.coordinates.convert_poly_coords': ( 'data.coordinates.html#convert_poly_coords',
                                                                                          'geo2ml/data/coordinates.py'),
                                         'geo2ml.data.coordinates.gdf_to_px': ( 'data.coordinates.html#gdf_to_px',
                                                                                'geo2ml/data/coordinates.py'),
                                         'geo2ml.data.coordinates.georegister_px_df': ( 'data.coordinates.html#georegister_px_df',
                                                                                        'geo2ml/data/coordinates.py'),
                                         'geo2ml.data.coordinates.get_geo_transform': ( 'data.coordinates.html#get_geo_transform',
                                                                                        'geo2ml/data/coordinates.py'),
                                         'geo2ml.data.coordinates.list_to_affine': ( 'data.coordinates.html#list_to_affine',
                                                                                     'geo2ml/data/coordinates.py')},
            'geo2ml.data.cv': { 'geo2ml.data.cv._corners2rotatedbbox': ('data.cv.html#_corners2rotatedbbox', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv._process_shp_to_coco': ('data.cv.html#_process_shp_to_coco', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.calc_bearing': ('data.cv.html#calc_bearing', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.coco_to_shp': ('data.cv.html#coco_to_shp', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.nor_theta': ('data.cv.html#nor_theta', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.shp_to_coco': ('data.cv.html#shp_to_coco', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.shp_to_coco_results': ('data.cv.html#shp_to_coco_results', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.shp_to_yolo': ('data.cv.html#shp_to_yolo', 'geo2ml/data/cv.py'),
                                'geo2ml.data.cv.yolo_to_shp': ('data.cv.html#yolo_to_shp', 'geo2ml/data/cv.py')},
            'geo2ml.data.postproc': { 'geo2ml.data.postproc.do_nms': ('data.postprocessing.html#do_nms', 'geo2ml/data/postproc.py'),
                                      'geo2ml.data.postproc.non_max_suppression_fast': ( 'data.postprocessing.html#non_max_suppression_fast',
                                                                                         'geo2ml/data/postproc.py'),
                                      'geo2ml.data.postproc.non_max_suppression_poly': ( 'data.postprocessing.html#non_max_suppression_poly',
                                                                                         'geo2ml/data/postproc.py'),
                                      'geo2ml.data.postproc.poly_IoU': ('data.postprocessing.html#poly_iou', 'geo2ml/data/postproc.py')},
            'geo2ml.data.tabular': { 'geo2ml.data.tabular.array_to_longform': ( 'data.tabular.html#array_to_longform',
                                                                                'geo2ml/data/tabular.py'),
                                     'geo2ml.data.tabular.drop_small_classes': ( 'data.tabular.html#drop_small_classes',
                                                                                 'geo2ml/data/tabular.py'),
                                     'geo2ml.data.tabular.sample_raster_with_points': ( 'data.tabular.html#sample_raster_with_points',
                                                                                        'geo2ml/data/tabular.py'),
                                     'geo2ml.data.tabular.sample_raster_with_polygons': ( 'data.tabular.html#sample_raster_with_polygons',
                                                                                          'geo2ml/data/tabular.py')},
            'geo2ml.data.tiling': { 'geo2ml.data.tiling.Tiler': ('data.tiling.html#tiler', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.Tiler.__init__': ('data.tiling.html#tiler.__init__', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.Tiler.tile_and_rasterize_vector': ( 'data.tiling.html#tiler.tile_and_rasterize_vector',
                                                                                            'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.Tiler.tile_raster': ('data.tiling.html#tiler.tile_raster', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.Tiler.tile_vector': ('data.tiling.html#tiler.tile_vector', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.copy_sum': ('data.tiling.html#copy_sum', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.fix_multipolys': ('data.tiling.html#fix_multipolys', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.untile_raster': ('data.tiling.html#untile_raster', 'geo2ml/data/tiling.py'),
                                    'geo2ml.data.tiling.untile_vector': ('data.tiling.html#untile_vector', 'geo2ml/data/tiling.py')},
            'geo2ml.plotting': { 'geo2ml.plotting.plot_coco_instance': ('plotting.html#plot_coco_instance', 'geo2ml/plotting.py'),
                                 'geo2ml.plotting.plot_yolo_instance': ('plotting.html#plot_yolo_instance', 'geo2ml/plotting.py')},
            'geo2ml.scripts.data': { 'geo2ml.scripts.data.create_coco_dataset': ( 'scripts.data.html#create_coco_dataset',
                                                                                  'geo2ml/scripts/data.py'),
                                     'geo2ml.scripts.data.create_raster_dataset': ( 'scripts.data.html#create_raster_dataset',
                                                                                    'geo2ml/scripts/data.py'),
                                     'geo2ml.scripts.data.create_yolo_dataset': ( 'scripts.data.html#create_yolo_dataset',
                                                                                  'geo2ml/scripts/data.py'),
                                     'geo2ml.scripts.data.sample_points': ('scripts.data.html#sample_points', 'geo2ml/scripts/data.py'),
                                     'geo2ml.scripts.data.sample_polygons': ( 'scripts.data.html#sample_polygons',
                                                                              'geo2ml/scripts/data.py')},
            'geo2ml.utils': { 'geo2ml.utils.build_overviews': ('utils.html#build_overviews', 'geo2ml/utils.py'),
                              'geo2ml.utils.check_cell': ('utils.html#check_cell', 'geo2ml/utils.py'),
                              'geo2ml.utils.create_grid': ('utils.html#create_grid', 'geo2ml/utils.py'),
                              'geo2ml.utils.create_qgis_colormap': ('utils.html#create_qgis_colormap', 'geo2ml/utils.py'),
                              'geo2ml.utils.format_cli_info': ('utils.html#format_cli_info', 'geo2ml/utils.py'),
                              'geo2ml.utils.save_raster': ('utils.html#save_raster', 'geo2ml/utils.py'),
                              'geo2ml.utils.set_cli_styles': ('utils.html#set_cli_styles', 'geo2ml/utils.py')}}}
