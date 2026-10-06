# pystac-ext-sat

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Satellite Extension](https://github.com/stac-extensions/sat).
This extension provides fields for describing satellite-specific metadata, including orbit state vectors, relative orbit numbers, and platform-specific identifiers.

## Supported versions

- [v1.0.0](https://stac-extensions.github.io/sat/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.0.1` still targets v1.0.0.
