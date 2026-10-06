# pystac-ext-classification

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Classification Extension](https://github.com/stac-extensions/classification).
This extension provides a way to describe categorical data and classification schemes for raster and vector data, including class names, descriptions, color hints, and regional mappings.

## Supported versions

- [v2.0.0](https://stac-extensions.github.io/classification/v2.0.0/schema.json)
- [v1.1.0](https://stac-extensions.github.io/classification/v1.1.0/schema.json)
- [v1.0.0](https://stac-extensions.github.io/classification/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `2.0.1` still targets v2.0.0.
