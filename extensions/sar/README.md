# pystac-ext-sar

[PySTAC](https://pypi.org/project/pystac/) extension package for the [SAR Extension](https://github.com/stac-extensions/sar).
This extension provides fields for describing Synthetic-Aperture Radar (SAR) data, including instrument mode, frequency band, polarizations, product type, and observation direction.

## Supported versions

- [v1.0.0](https://stac-extensions.github.io/sar/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.0.1` still targets v1.0.0.
