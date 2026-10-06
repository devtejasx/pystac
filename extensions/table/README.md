# pystac-ext-table

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Table Extension](https://github.com/stac-extensions/table).
This extension provides fields for describing tabular data assets, including column definitions, row counts, primary/foreign keys, and storage formats.

## Supported versions

- [v1.2.0](https://stac-extensions.github.io/table/v1.2.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.2.1` still targets v1.2.0.
