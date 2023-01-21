import unittest
import ipdb
from ithopy.devices import HruMessageParser
from ithopy.exceptions import *

class TestHruMessageParser(unittest.TestCase):
  def setUp(self) -> None:
    self.parser = HruMessageParser()

  def test_parsing_status_format_message(self):
    # Query device status format:
    self.parser.parse(
      [0x80, 0x82, 0xA4, 0x00, 0x01, 0x16, 0x91, 0x11, 0x10, 0x90, 0x10, 0x90, 0x92, 0x92, 0x00, 0x92, 0x92, 0x00, 0x00, 0x91, 0x00, 0x10, 0x10, 0x00, 0x90, 0x00, 0x00, 0x10, 0xC8]
    )
    print(self.parser.message.inspect())

    # A4 00 01 followed by number of data elements, followed by element formats (1 byte per element).

    # Data format (1 byte):

    # | Bit  | Description                        |
    # | ---- | ---------------------------------- |
    # | 7    | signed (1) / unsigned (0)          |
    # | 6..4 | size in bytes (2^n): 0=1, 1=2, 2=4 |
    # | 3..0 | decimal digits (divider 10^n)      |

    # So for example `91` would mean "signed, 2 bytes, 0.1 values".

  def test_parsing_device_status_message(self):
    # Query device status:
    self.parser.parse(
      [0x82, 0x80, 0xA4, 0x01, 0x04, 0x00, 0x55]
    )

    print(self.parser.message.inspect())

    # Query device status (response):
    self.parser.parse(
      [0x80, 0x82, 0xA4, 0x01, 0x01, 0x25, 0x00, 0x00, 0x03, 0x9C, 0x03, 0x9E, 0x03, 0x98, 0x03, 0xEB, 0x03, 0xEB, 0x09, 0x09, 0x09, 0x8A, 0x00, 0x09, 0x09, 0x09, 0x8A, 0x00, 0x00, 0x0B, 0xB8, 0x01, 0x00, 0x00, 0x00, 0xB1, 0x79, 0x00, 0x00, 0x00, 0x00, 0x10, 0x95, 0x9F]
    )

    print(self.parser.message.inspect())

  def test_parsing_speed_setting_message(self):
    # 2-byte integer payload:
    # generated using `hru.set_exhaust_fan_rpm(1200)`
    self.parser.parse(
      [130, 128, 164, 16, 6, 19, 0, 0, 4, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 0, 79]
    )

    self.assertEqual(
      self.parser.message.payload.payload_value,
      1200
    )

    self.assertEqual(
      self.parser.message.msg_class,
      9232
    )

    self.assertEqual(
      self.parser.message.build().intArr,
      [130, 128, 164, 16, 6, 19, 0, 0, 4, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 0, 79]
    )

    print(self.parser.message.inspect())

  def test_checksum_error(self):
      self.assertRaises(
        IthoPyException,
        self.parser.parse,
        [0x82, 0x80, 0x24, 0x10, 0x04, 0x13, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0xFF],
      )

if __name__ == '__main__':
  unittest.main()
