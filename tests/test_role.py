"""Tests for :class:`pystac.RoleType`."""

import json

import pystac
from pystac import RoleType

# The roles listed under "List of Asset Roles" in the STAC best practices.
SPEC_ROLES = {
    "data",
    "metadata",
    "thumbnail",
    "overview",
    "visual",
    "date",
    "graphic",
    "data-mask",
    "snow-ice",
    "land-water",
    "water-mask",
    "iso-19115",
}


def test_covers_the_spec_list() -> None:
    assert {role.value for role in RoleType} == SPEC_ROLES


def test_is_a_string() -> None:
    assert RoleType.THUMBNAIL == "thumbnail"
    assert str(RoleType.DATA_MASK) == "data-mask"
    assert json.dumps([RoleType.OVERVIEW]) == '["overview"]'


def test_usable_as_an_asset_role() -> None:
    asset = pystac.Asset(
        href="https://example.com/thumb.png",
        media_type=pystac.MediaType.PNG,
        roles=[RoleType.THUMBNAIL, RoleType.OVERVIEW],
    )

    assert asset.to_dict()["roles"] == ["thumbnail", "overview"]
