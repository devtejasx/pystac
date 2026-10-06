# pystac-ext-timestamps

[PySTAC](https://pypi.org/project/pystac/) extension package for the [Timestamps Extension](https://github.com/stac-extensions/timestamps).
This extension provides fields for additional temporal metadata beyond the core datetime, including published, expires, and unpublished timestamps.

## Supported versions

- [v1.1.0](https://stac-extensions.github.io/timestamps/v1.1.0/schema.json)

## Versioning

This package's MAJOR and MINOR versions match the version of the extension specification it targets.
When we release updates to the package code without changing the target extension version, we use [PATCH releases](https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers), so the PATCH number can differ from the extension's, e.g. `1.1.1` still targets v1.1.0.
