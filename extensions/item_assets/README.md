# pystac-ext-item-assets

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Item Assets Definition Extension](https://github.com/stac-extensions/item-assets).
This extension allows collections to define common asset properties that are shared across all items in the collection, providing a template for expected assets.

## Supported versions

- [v1.0.0](https://stac-extensions.github.io/item-assets/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.0.1` still targets v1.0.0.
