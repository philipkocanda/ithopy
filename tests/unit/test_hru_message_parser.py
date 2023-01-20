import unittest
import ipdb
from ithopy.devices.hru_device import HruDevice
from ithopy.devices.hru_message_parser import HruMessageParser

class TestHruMessageParser(unittest.TestCase):
  def setUp(self) -> None:
    self.parser = HruMessageParser()

  def test_parsing(self):
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

  # TODO throw error on checksum failure!
  def test_checksum_error(self):
    pass

  def test_parsing_unknown_payload(self):
    # Let's try to parse this message from IthoWifi
    # (src/IthoSystem.cpp#1388)
    self.parser.parse(
      [0x82, 0x80, 0x24, 0x10, 0x04, 0x13, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0xFF]
    )

    self.assertEqual(
      self.parser.message.msg_class,
      -23536 # that doesn't seem right...
    )

    self.assertEqual(
      self.parser.message.payload.payload_value,
      0
    )

    self.assertEqual(
      self.parser.message.build().intArr,
      [130, 128, 36, 16, 4, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 180]
    )

    m = self.parser.message
    # m.build().byteArr
    # m.build().intArr

    # ipdb.set_trace()

if __name__ == '__main__':
  unittest.main()
