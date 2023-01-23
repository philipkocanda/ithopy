# IthoPy

Python3 library to build and parse I2C bus messages for Itho devices. Meant for inclusion in your own Python code, not for direct consumption through the CLI (though it's on the list!).

NOTE: This library can't communicate directly with your device. For that you'll need to use something like [itho-esp](https://github.com/rustyx/itho-esp) to send/receive these messages to a ESP32 using MQTT.

## Tested devices

- Itho HRU ECO BAL LE (firmware: v12, hardware: v3)

## TODO

- [x] Implement message builder
- [x] Tests for message builder
- [x] Implement message parser
- [x] Tests for message parser
- [x] Support for more commands and devices:
  - [x] Support for parsing device format and status queries
  - [ ] Support for building device type and serial queries
  - [ ] Allow user to select device model
  - [ ] Load parameters from csv file
  - [ ] Load data labels from csv file
- [ ] CLI for quick message parsing and building

## Building I2C Queries

NOTE: The most up to date examples can be found in the test suite.

```py
from ithopy.hru_device import HruDevice

hru = HruDevice(HruDevice.ESP32_ADDR, HruDevice.HRU_ADDR)
msg = hru.set_supply_fan_rpm(0)

print(str(msg))
# => "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D 00 04"

print(msg.bytes_list())
# => ['82', '80', 'A4', '10', '06', '13', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '2D', '00', '04']

print(msg.build().data)
# => [130, 128, 164, 16, 6, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 4]
```

## Parsing I2C Responses

### Device Status Format

```python
import json
from ithopy.devices import HruMessageParser

parser = HruMessageParser()

message = self.parser.parse(
    [0x80, 0x82, 0xA4, 0x00, 0x01, 0x16, 0x91, 0x11, 0x10, 0x90, 0x10,
     0x90, 0x92, 0x92, 0x00, 0x92, 0x92, 0x00, 0x00, 0x91, 0x00, 0x10,
     0x10, 0x00, 0x90, 0x00, 0x00, 0x10, 0xC8])

print(json.dumps(message.inspect()))
```

Outputs:

```json
{"dest": 128, "src": 130, "msg_class": "status_format", "msg_type": "report_response", "payload": {
"data_formats": [
  {"idx": 0, "divider": 10, "bytes": 2, "signed": true, "offset": 0, "label": "Requested fanspeed (%)"},
  {"idx": 1, "divider": 10, "bytes": 2, "signed": false, "offset": 2, "label": "Balance (%)"},
  {"idx": 2, "divider": 1, "bytes": 2, "signed": false, "offset": 4, "label": "supply fan (rpm)"},
  {"idx": 3, "divider": 1, "bytes": 2, "signed": true, "offset": 6, "label": "supply fan actual (rpm)"},
  {"idx": 4, "divider": 1, "bytes": 2, "signed": false, "offset": 8, "label": "exhaust fan (rpm)"},
  {"idx": 5, "divider": 1, "bytes": 2, "signed": true, "offset": 10, "label": "exhaust fan actual (rpm)"},
  {"idx": 6, "divider": 100, "bytes": 2, "signed": true, "offset": 12, "label": "supply temp (\u00b0C)"},
  {"idx": 7, "divider": 100, "bytes": 2, "signed": true, "offset": 14, "label": "exhaust temp (\u00b0C)"},
  {"idx": 8, "divider": 1, "bytes": 1, "signed": false, "offset": 16, "label": "Status"},
  {"idx": 9, "divider": 100, "bytes": 2, "signed": true, "offset": 17, "label": "Room temp (\u00b0C)"},
  {"idx": 10, "divider": 100, "bytes": 2, "signed": true, "offset": 19, "label": "Outdoor temp (\u00b0C)"},
  {"idx": 11, "divider": 1, "bytes": 1, "signed": false, "offset": 21, "label": "Valve position (pulse)"},
  {"idx": 12, "divider": 1, "bytes": 1, "signed": false, "offset": 22, "label": "Bypass position (pulse)"},
  {"idx": 13, "divider": 10, "bytes": 2, "signed": true, "offset": 23, "label": "Summercounter"},
  {"idx": 14, "divider": 1, "bytes": 1, "signed": false, "offset": 25, "label": "Summerday"},
  {"idx": 15, "divider": 1, "bytes": 2, "signed": false, "offset": 26, "label": "Frost timer (sec)"},
  {"idx": 16, "divider": 1, "bytes": 2, "signed": false, "offset": 28, "label": "Boiler timer (min)"},
  {"idx": 17, "divider": 1, "bytes": 1, "signed": false, "offset": 30, "label": "Frost block"},
  {"idx": 18, "divider": 1, "bytes": 2, "signed": true, "offset": 31, "label": "Current position"},
  {"idx": 19, "divider": 1, "bytes": 1, "signed": false, "offset": 33, "label": "VKKswitch"},
  {"idx": 20, "divider": 1, "bytes": 1, "signed": false, "offset": 34, "label": "GHEswitch"},
  {"idx": 21, "divider": 1, "bytes": 2, "signed": false, "offset": 35, "label": "Filter counter"}]}}
```

### Device Status Information

```python
import json
from ithopy.devices import HruMessageParser

parser = HruMessageParser()

message = self.parser.parse(
    [0x80, 0x82, 0xA4, 0x00, 0x01, 0x16, 0x91, 0x11, 0x10, 0x90, 0x10,
     0x90, 0x92, 0x92, 0x00, 0x92, 0x92, 0x00, 0x00, 0x91, 0x00, 0x10,
     0x10, 0x00, 0x90, 0x00, 0x00, 0x10, 0xC8])

print(json.dumps(message.inspect()))
```

Outputs:

```json
{
  "dest": 128,
  "src": 130,
  "msg_class": "device_status",
  "msg_type": "report_response",
  "payload": {
    "0": {
      "label": "Requested fanspeed (%)",
      "value": 0.0
    },
    "1": {
      "label": "Balance (%)",
      "value": 92.4
    },
    "2": {
      "label": "supply fan (rpm)",
      "value": 926.0
    },
    "3": {
      "label": "supply fan actual (rpm)",
      "value": 920.0
    },
    "4": {
      "label": "exhaust fan (rpm)",
      "value": 1003.0
    },
    "5": {
      "label": "exhaust fan actual (rpm)",
      "value": 1003.0
    },
    "6": {
      "label": "supply temp (\u00b0C)",
      "value": 23.13
    },
    "7": {
      "label": "exhaust temp (\u00b0C)",
      "value": 24.42
    },
    "8": {
      "label": "Status",
      "value": 0.0
    },
    "9": {
      "label": "Room temp (\u00b0C)",
      "value": 23.13
    },
    "10": {
      "label": "Outdoor temp (\u00b0C)",
      "value": 24.42
    },
    "11": {
      "label": "Valve position (pulse)",
      "value": 0.0
    },
    "12": {
      "label": "Bypass position (pulse)",
      "value": 0.0
    },
    "13": {
      "label": "Summercounter",
      "value": 300.0
    },
    "14": {
      "label": "Summerday",
      "value": 1.0
    },
    "15": {
      "label": "Frost timer (sec)",
      "value": 0.0
    },
    "16": {
      "label": "Boiler timer (min)",
      "value": 177.0
    },
    "17": {
      "label": "Frost block",
      "value": 121.0
    },
    "18": {
      "label": "Current position",
      "value": 0.0
    },
    "19": {
      "label": "VKKswitch",
      "value": 0.0
    },
    "20": {
      "label": "GHEswitch",
      "value": 0.0
    },
    "21": {
      "label": "Filter counter",
      "value": 4245.0
    }
  }
}
```

## I2C packet format

`[Byte index] description`

```
[0]     destination address
[1]     reply address
[2..3]  message class
[4]     message type
[5]     payload length
[n]     payload
[n+1]   checksum
```

Payload is parsed depending on message type.

## Unit Tests

Run all unit tests:

```sh
bin/test
```