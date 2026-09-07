"""Tests for the machinery shared by every extension"""

import json
from datetime import datetime
from typing import Any

import pytest

import pystac
from pystac.extensions.base import PropertiesExtension

PROP = "test:prop"


class Inner:
    """An object that only knows how to serialize itself."""

    def __init__(self, value: str) -> None:
        self.value = value

    def to_dict(self) -> dict[str, Any]:
        return {"value": self.value}


class Outer:
    """An object whose dictionary form still holds objects."""

    def __init__(self, inner: Inner) -> None:
        self.inner = inner

    def to_dict(self) -> dict[str, Any]:
        return {"inner": self.inner, "inners": [self.inner]}


class Extension(PropertiesExtension):
    def __init__(self, item: pystac.Item) -> None:
        self.properties = item.properties

    def set(self, v: Any) -> None:
        self._set_property(PROP, v)


@pytest.fixture
def item() -> pystac.Item:
    return pystac.Item(
        id="an-id",
        geometry=None,
        bbox=None,
        datetime=datetime(2020, 1, 1),
        properties={},
    )


@pytest.fixture
def extension(item: pystac.Item) -> Extension:
    return Extension(item)


def test_converts_a_bare_object(extension: Extension) -> None:
    extension.set(Inner("a"))

    assert extension.properties[PROP] == {"value": "a"}


def test_converts_objects_in_a_list(extension: Extension) -> None:
    extension.set([Inner("a"), Inner("b")])

    assert extension.properties[PROP] == [{"value": "a"}, {"value": "b"}]


def test_converts_objects_nested_in_a_dict(extension: Extension) -> None:
    extension.set({"key": Inner("a"), "keys": [Inner("b")]})

    assert extension.properties[PROP] == {
        "key": {"value": "a"},
        "keys": [{"value": "b"}],
    }


def test_converts_objects_a_to_dict_leaves_behind(extension: Extension) -> None:
    extension.set(Outer(Inner("a")))

    assert extension.properties[PROP] == {
        "inner": {"value": "a"},
        "inners": [{"value": "a"}],
    }


def test_converts_a_tuple_to_a_list(extension: Extension) -> None:
    extension.set((Inner("a"), 1))

    assert extension.properties[PROP] == [{"value": "a"}, 1]


def test_leaves_plain_values_alone(extension: Extension) -> None:
    extension.set({"a": [1, "two", None, 3.0]})

    assert extension.properties[PROP] == {"a": [1, "two", None, 3.0]}


def test_the_item_stays_serializable(item: pystac.Item) -> None:
    Extension(item).set(Outer(Inner("a")))

    assert json.loads(json.dumps(item.to_dict()))["properties"][PROP] == {
        "inner": {"value": "a"},
        "inners": [{"value": "a"}],
    }


def test_none_still_pops_the_property(extension: Extension) -> None:
    extension.set(Inner("a"))
    extension.set(None)

    assert PROP not in extension.properties
