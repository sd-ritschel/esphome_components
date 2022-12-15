import esphome.codegen as cg
from esphome.core import EnumValue
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    UNIT_CELSIUS,
    UNIT_PERCENT,
    DEVICE_CLASS_TEMPERATURE,
    STATE_CLASS_MEASUREMENT,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ENTITY_CATEGORY_NONE
)

from . import (
    CONF_KM271_ID,
    KM271
)

from .const import (
    CONF_HC1_FLOWTEMP_SETP,
    CONF_HC1_FLOWTEMP_MEAS,
    CONF_HC1_ROOM_TEMP_SETP,
    CONF_HC1_ROOM_TEMP_MEAS,
    CONF_HC1_PUMP_POWER,
    CONF_HC1_MIXER_POS,
    CONF_HC1_CURVE_P10,
    CONF_HC1_CURVE_P0,
    CONF_HC1_CURVE_N10,
    CONF_HC2_FLOWTEMP_SETP,
    CONF_HC2_FLOWTEMP_MEAS,
    CONF_HC2_ROOM_TEMP_SETP,
    CONF_HC2_ROOM_TEMP_MEAS,
    CONF_HC2_PUMP_POWER,
    CONF_HC2_MIXER_POS,
    CONF_HC2_CURVE_P10,
    CONF_HC2_CURVE_P0,
    CONF_HC2_CURVE_N10,
    CONF_WW_TEMP_SETP,
    CONF_WW_TEMP_MEAS,
    CONF_BOILER_TEMP_SETP,
    CONF_BOILER_TEMP_MEAS,
    CONF_BOILER_TEMP_TURNON,
    CONF_BOILER_TEMP_TURNOFF,
    CONF_EXHAUST_TEMP,
    CONF_OUTDOOR_TEMP,
    CONF_OUTDOOR_TEMP_ATTEN
)

CODEOWNERS = ["@the78mole", "@jensgraef"]

TYPES = [
    CONF_HC1_FLOWTEMP_SETP,
    CONF_HC1_FLOWTEMP_MEAS,
    CONF_HC1_ROOM_TEMP_SETP,
    CONF_HC1_ROOM_TEMP_MEAS,
    CONF_HC1_PUMP_POWER,
    CONF_HC1_MIXER_POS,
    CONF_HC1_CURVE_P10,
    CONF_HC1_CURVE_P0,
    CONF_HC1_CURVE_N10,
    CONF_HC2_FLOWTEMP_SETP,
    CONF_HC2_FLOWTEMP_MEAS,
    CONF_HC2_ROOM_TEMP_SETP,
    CONF_HC2_ROOM_TEMP_MEAS,
    CONF_HC2_PUMP_POWER,
    CONF_HC2_MIXER_POS,
    CONF_HC2_CURVE_P10,
    CONF_HC2_CURVE_P0,
    CONF_HC2_CURVE_N10,
    CONF_WW_TEMP_SETP,
    CONF_WW_TEMP_MEAS,
    CONF_BOILER_TEMP_SETP,
    CONF_BOILER_TEMP_MEAS,
    CONF_BOILER_TEMP_TURNON,
    CONF_BOILER_TEMP_TURNOFF,
    CONF_EXHAUST_TEMP,
    CONF_OUTDOOR_TEMP,
    CONF_OUTDOOR_TEMP_ATTEN
]


CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(CONF_KM271_ID): cv.use_id(KM271),
            # Heating Circuit 1
            cv.Optional(CONF_HC1_FLOWTEMP_SETP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  		
            ),
            cv.Optional(CONF_HC1_FLOWTEMP_MEAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC1_ROOM_TEMP_SETP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,   	
            ),
            cv.Optional(CONF_HC1_ROOM_TEMP_MEAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC1_PUMP_POWER): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC1_MIXER_POS): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC1_CURVE_P10): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_HC1_CURVE_P0): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_HC1_CURVE_N10): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            # Heating Circuit 2
            cv.Optional(CONF_HC2_FLOWTEMP_SETP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_HC2_FLOWTEMP_MEAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC2_ROOM_TEMP_SETP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_HC2_ROOM_TEMP_MEAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC2_PUMP_POWER): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC2_MIXER_POS): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                accuracy_decimals=0,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_HC2_CURVE_P10): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_HC2_CURVE_P0): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC, 	
            ),
            cv.Optional(CONF_HC2_CURVE_N10): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC, 	
            ),    
            # Hot Water Circuit
            cv.Optional(CONF_WW_TEMP_SETP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_WW_TEMP_MEAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            # Boiler
            cv.Optional(CONF_BOILER_TEMP_SETP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            cv.Optional(CONF_BOILER_TEMP_MEAS): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),            
            cv.Optional(CONF_BOILER_TEMP_TURNON): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC, 	
            ),
            cv.Optional(CONF_BOILER_TEMP_TURNOFF): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,  	
            ),
            # Other
            cv.Optional(CONF_EXHAUST_TEMP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_OUTDOOR_TEMP): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
            cv.Optional(CONF_OUTDOOR_TEMP_ATTEN): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
                entity_category=ENTITY_CATEGORY_NONE, 	
            ),
          
        }
    )
)


async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]

        sens = await sensor.new_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_sensor")(sens))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_KM271_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)
