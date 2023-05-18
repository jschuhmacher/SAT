from custom_components.sat import CONF_NAME, CONF_DEVICE, CONF_INSIDE_SENSOR_ENTITY_ID, CONF_OUTSIDE_SENSOR_ENTITY_ID, CONF_MODE, MODE_FAKE, CONF_AUTOMATIC_GAINS, \
    CONF_AUTOMATIC_DUTY_CYCLE, CONF_OVERSHOOT_PROTECTION

DEFAULT_USER_DATA = {
    CONF_MODE: MODE_FAKE,
    CONF_NAME: "Test",
    CONF_DEVICE: None,
    CONF_AUTOMATIC_GAINS: True,
    CONF_AUTOMATIC_DUTY_CYCLE: True,
    CONF_OVERSHOOT_PROTECTION: True,
    CONF_INSIDE_SENSOR_ENTITY_ID: "sensor.test_inside_sensor",
    CONF_OUTSIDE_SENSOR_ENTITY_ID: "sensor.test_outside_sensor",
}
