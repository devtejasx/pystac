import datetime
import json
from pathlib import Path

import pytest

from pystac import Item, utils


def test_item_init() -> None:
    item = Item(id="an-id")
    item.validate()


def test_item_from_dict(examples_path: Path) -> None:
    with open(examples_path / "simple-item.json") as f:
        data = json.load(f)

    # Normalize datetime string to get rid of spurious zeros
    data["properties"]["datetime"] = utils.datetime_to_str(
        datetime.datetime.fromisoformat(data["properties"]["datetime"])
    )

    item = Item.from_dict(data)
    item.validate()
    assert item.to_dict() == data


@pytest.mark.vcr
def test_validate_extension(proj_example: Item) -> None:
    proj_example.validate()


def test_validate_tuple_coordinates() -> None:
    # e.g. from shapely.geometry.mapping, which uses tuples for coordinates
    geometry = {
        "type": "Polygon",
        "coordinates": (
            ((-1.0, -1.0), (1.0, -1.0), (1.0, 1.0), (-1.0, 1.0), (-1.0, -1.0)),
        ),
    }
    item = Item(id="an-id", geometry=geometry, bbox=[-1.0, -1.0, 1.0, 1.0])
    item.validate()
