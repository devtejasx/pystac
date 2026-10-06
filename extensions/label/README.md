# pystac-ext-label

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Label Extension](https://github.com/stac-extensions/label).
This extension provides fields for describing labeled training data for machine learning, including label types, classes, tasks, methods, and overviews of label distributions.

## Supported versions

- [v1.0.1](https://stac-extensions.github.io/label/v1.0.1/schema.json)
- [v1.0.0](https://stac-extensions.github.io/label/v1.0.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.0.2` still targets v1.0.1.
