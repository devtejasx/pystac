# pystac-ext-projection

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Projection Extension](https://github.com/stac-extensions/projection).
This extension provides fields for describing the geospatial projection of data, including EPSG code, WKT2, PROJJSON, geometry, bounding box, centroid, shape, and transform.

## Supported versions

- [v2.0.0](https://stac-extensions.github.io/projection/v2.0.0/schema.json)
- [v1.2.0](https://stac-extensions.github.io/projection/v1.2.0/schema.json)
- [v1.1.0](https://stac-extensions.github.io/projection/v1.1.0/schema.json)
- [v1.0.0](https://stac-extensions.github.io/projection/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `2.0.1` still targets v2.0.0.
