import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select
from esphome.const import (
    CONF_ID,
    CONF_OPTIONS
)

from . import (
    CONF_KM271_ID,
    KM271
)

from .const import *

CODEOWNERS = ["@the78mole", "@jensgraef"]

TYPES = [
    CONF_HC1_OPMODE,
    CONF_WW_OPMODE,
]

km271_ns = cg.esphome_ns.namespace("KM271")

BuderusParamSelect = km271_ns.class_("BuderusParamSelect", select.Select, cg.Component)


# taken from tuya select
def ensure_option_map(value):
    cv.check_not_templatable(value)
    option = cv.All(cv.int_range(0, 2**8 - 1))
    mapping = cv.All(cv.string_strict)
    options_map_schema = cv.Schema({option: mapping})
    value = options_map_schema(value)

    all_values = list(value.keys())
    unique_values = set(value.keys())
    if len(all_values) != len(unique_values):
        raise cv.Invalid("Mapping values must be unique.")

    return value




CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            cv.Optional(CONF_HC1_OPMODE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Nacht', 1: 'Tag', 2: 'Auto'}): ensure_option_map
            }),
            cv.Optional(CONF_WW_OPMODE): select.SELECT_SCHEMA.extend({
                cv.GenerateID(): cv.declare_id(BuderusParamSelect),
                cv.Optional(CONF_OPTIONS, default={0: 'Aus', 1: 'Ein', 2: 'Auto'}): ensure_option_map
            })

        }
    )
)


async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]
        options_map = conf[CONF_OPTIONS]
        sens = await select.new_select(conf, options=list(options_map.values()))
        cg.add(sens.setSelectMappings(list(options_map.keys())))
        cg.add(getattr(hub, f"set_communication_component")(cg.RawExpression("KM271::" + key), sens))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_KM271_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)
