from pystac.utils import StringEnum


class RoleType(StringEnum):
    """A list of common asset roles that can be used in STAC Asset metadata.

    See :stac-spec:`"Asset Roles" <best-practices.md#asset-roles>` in the STAC
    Best Practices for guidance on choosing roles, and
    :stac-spec:`Assets <commons/assets.md#roles>` for the field itself. Roles
    are not a closed set: an asset may carry any string, and extensions define
    further roles of their own, such as
    :class:`pystac.extensions.eo.EORoleType` and
    :class:`pystac.extensions.sar.SarRoleType`.
    """

    DATA = "data"
    METADATA = "metadata"
    THUMBNAIL = "thumbnail"
    OVERVIEW = "overview"
    VISUAL = "visual"
    DATE = "date"
    GRAPHIC = "graphic"
    DATA_MASK = "data-mask"
    SNOW_ICE = "snow-ice"
    LAND_WATER = "land-water"
    WATER_MASK = "water-mask"
    ISO_19115 = "iso-19115"
