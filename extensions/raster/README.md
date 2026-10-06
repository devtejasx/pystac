# pystac-ext-raster

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Raster Extension](https://github.com/stac-extensions/raster).
This extension provides fields for describing raster band metadata, including data type, statistics, histograms, spatial resolution, nodata values, and units.

## Supported versions

- [v1.1.0](https://stac-extensions.github.io/raster/v1.1.0/schema.json)
- [v1.0.0](https://stac-extensions.github.io/raster/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.1.1` still targets v1.1.0.
