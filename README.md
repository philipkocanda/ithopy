# IthoPy

Python3 library to build and parse I2C bus messages for Itho devices. Meant for inclusion in your own Python code, not for direct consumption through the CLI.

NOTE: This library can't communicate directly with your device. For that you'll need to use something like [itho-esp](https://github.com/rustyx/itho-esp) to send/receive these messages to a ESP32 using MQTT.

## Supported devices

- Itho HRU ECO BAL LE (2017 model)

## TODO

- [x] Implement message builder
- [x] Tests for message builder
- [ ] Implement message parser
- [ ] Tests for message parser
- [ ] Support for more commands and devices:
  - [ ] Support for device type and status queries
  - [ ] Allow user to select device model
  - [ ] Load parameters from csv file
  - [ ] Load data labels from csv file

## Example usage

NOTE: The most up to date examples can be found in the test suite.

```py
from ithopy.hru_device import HruDevice

hru = HruDevice(HruDevice.ESP32_ADDR, HruDevice.HRU_ADDR)
msg = hru.set_supply_fan_rpm(0)

print(str(msg))
# => "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D 00 04"

print(msg.build().byte_list)
# => ['82', '80', 'A4', '10', '06', '13', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '2D', '00', '04']

print(msg.build().intArr)
# => [130, 128, 164, 16, 6, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 45, 0, 4]
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