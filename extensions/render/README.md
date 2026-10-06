# pystac-ext-render

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Render Extension](https://github.com/stac-extensions/render).
This extension provides fields for describing visualization parameters for assets, including rescaling, color maps, expressions, and tile matrix set configurations.

## Supported versions

- [v2.0.0](https://stac-extensions.github.io/render/v2.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `2.0.1` still targets v2.0.0.
