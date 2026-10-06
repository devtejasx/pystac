# pystac-ext-storage

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Storage Extension](https://github.com/stac-extensions/storage).
This extension provides fields for describing cloud storage attributes of assets, including storage platform, region, tier, and requester-pays configuration.

## Supported versions

- [v2.0.0](https://stac-extensions.github.io/storage/v2.0.0/schema.json)
- [v1.0.0](https://stac-extensions.github.io/storage/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `2.0.1` still targets v2.0.0.
