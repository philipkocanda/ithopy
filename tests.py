#!/usr/bin/env python3

import unittest
from ithopy.devices.hru_device import HruDevice
from ithopy.devices.hru_message_builder import HruMessageBuilder

class TestHruMessageBuilder(unittest.TestCase):
  def setUp(self) -> None:
    self.hru = HruMessageBuilder(HruDevice.ESP32_ADDR, HruDevice.HRU_ADDR)

  # Supply Fan Speed
  #
  def test_set_supply_fan_rpm(self):
    self.assertEqual(
      str(self.hru.set_supply_fan_rpm(0)),
      "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D 00 04"
    )

    self.assertEqual(
      str(self.hru.set_supply_fan_rpm(1477)),
      "82 80 A4 10 06 13 00 00 05 C5 00 00 00 00 00 00 00 00 00 00 00 00 00 2D 00 3A"
    )

    self.assertEqual(
      str(self.hru.set_supply_fan_rpm(1800)),
      "82 80 A4 10 06 13 00 00 07 08 00 00 00 00 00 00 00 00 00 00 00 00 00 2D 00 F5"
    )

  # Exhaust Fan Speed
  #
  def test_set_exhaust_fan_rpm(self):
    self.assertEqual(
      str(self.hru.set_exhaust_fan_rpm(0)),
      "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2E 00 03"
    )

    self.assertEqual(
      str(self.hru.set_exhaust_fan_rpm(1200)),
      "82 80 A4 10 06 13 00 00 04 B0 00 00 00 00 00 00 00 00 00 00 00 00 00 2E 00 4F"
    )

  def test_manual_mode(self):
    # Manual mode is forgotten after power cycle!
    self.assertEqual(
      str(self.hru.set_manual_mode(True)),
      "82 80 A4 10 06 13 00 00 00 01 00 00 00 00 00 00 00 00 00 00 00 00 00 2C 00 04"
    )

    self.assertEqual(
      str(self.hru.set_manual_mode(False)),
      "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2C 00 05"
    )

  def test_valve_position(self):
    # Closed position (default)
    #
    # Both intake and exhaust air pass through heat exchanger.
    self.assertEqual(
      str(self.hru.set_valve_position(0)),
      "82 80 A4 10 06 13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2F 00 02"
    )

    # Frost position
    #
    # Mix in some (or a lot of) indoor air to prevent heat exchanger from freezing up on very cold days.
    self.assertEqual(
      str(self.hru.set_valve_position(-800)),
      "82 80 A4 10 06 13 00 00 FC E0 00 00 00 00 00 00 00 00 00 00 00 00 00 2F 00 26"
    )

    # Bypass position
    #
    # Intake air bypasses heat exchanger, useful on warm summer nights.
    self.assertEqual(
      str(self.hru.set_valve_position(800)),
      "82 80 A4 10 06 13 00 00 03 20 00 00 00 00 00 00 00 00 00 00 00 00 00 2F 00 DF"
    )

  def test_internal_methods(self):
    self.assertEqual(
      self.hru.set_exhaust_fan_rpm(1200).build().byteArr,
      ['82', '80', 'A4', '10', '06', '13', '00', '00', '04', 'B0', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '2E', '00', '4F']
    )

    self.assertEqual(
      self.hru.set_exhaust_fan_rpm(1200).build().intArr,
      [130, 128, 164, 16, 6, 19, 0, 0, 4, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 0, 79]
    )

if __name__ == '__main__':
  unittest.main()
