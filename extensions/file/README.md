# pystac-ext-file

[PySTAC](https://pypi.org/project/pystac/) extension package for the [File Info Extension](https://github.com/stac-extensions/file).
This extension provides fields for describing file details such as byte order, checksum, header size, and data type for assets.

## Supported versions

- [v2.1.0](https://stac-extensions.github.io/file/v2.1.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `2.1.1` still targets v2.1.0.
