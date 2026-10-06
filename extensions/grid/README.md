# pystac-ext-grid

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Grid Extension](https://github.com/stac-extensions/grid).
This extension describes gridded data products by specifying the grid code (e.g. MGRS, MODIS, or other tiling schemes) that the data corresponds to.

## Supported versions

- [v1.1.0](https://stac-extensions.github.io/grid/v1.1.0/schema.json)
- [v1.0.0](https://stac-extensions.github.io/grid/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.1.1` still targets v1.1.0.
