"""Type definitions for Volkszaehler entities."""

from typing import Literal, TypedDict

# List from https://github.com/volkszaehler/volkszaehler.org/blob/master/lib/Definition/EntityDefinition.json
EntityType = Literal[
    "group",
    "building",
    "user",
    "power",
    "powersensor",
    "electric meter",
    "voltage",
    "current",
    "gas",
    "gas sensor",
    "gas meter",
    "heat",
    "heatsensor",
    "heattotal",
    "temperature",
    "water",
    "flow",
    "watertotal",
    "filllevel",
    "workinghours",
    "workinghourstotal",
    "workinghourssensor",
    "valve",
    "pressure",
    "humidity",
    "humidity absolute",
    "windspeed",
    "fanspeed",
    "luminosity",
    "illumination",
    "frequency",
    "universalcounter",
    "universalsensor",
    "consumptionsensor",
    "virtualsensor",
    "virtualconsumption",
    "co2 concentration",
    "particulate matter",
]


class Entity(TypedDict, total=False):
    """Typed representation of a Volkszaehler entity."""

    uuid: str
    type: EntityType
    color: str
    fillstyle: int
    linestyle: str
    public: bool
    resolution: int
    style: str
    title: str
    yaxis: str
