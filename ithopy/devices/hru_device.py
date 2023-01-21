class HruDevice:
    HRU_ADDR = 0x82
    RFT_ADDR = 0x60
    ESP32_ADDR = 0x80

    # Message Classes
    SETTINGS_MSG = 9232
    STATUS_MSG = 9216
    DEVICE_STATUS_MSG = 9217

    # Settings
    # TODO: read from parameters csv
    SET_MANUAL_MODE = 44
    SET_SUPPLY_FAN_RPM = 45
    SET_EXHAUST_FAN_RPM = 46
    SET_VALVE_POSITION = 47
