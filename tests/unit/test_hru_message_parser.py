import unittest
import ipdb
import json
from ithopy.devices import HruMessageParser
from ithopy.exceptions import *


class TestHruMessageParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = HruMessageParser()

    def test_parsing_status_format_message(self):
        self.maxDiff = None

        # Query device status format:
        self.parser.parse(
            [0x80, 0x82, 0xA4, 0x00, 0x01, 0x16, 0x91, 0x11, 0x10, 0x90, 0x10,
             0x90, 0x92, 0x92, 0x00, 0x92, 0x92, 0x00, 0x00, 0x91, 0x00, 0x10,
             0x10, 0x00, 0x90, 0x00, 0x00, 0x10, 0xC8])

        # ipdb.set_trace()

        # autopep8: off
        self.assertEqual(self.parser.message.inspect(),
        {
          'dest': 128,
          'src': 130,
          'msg_class': 'status_format',
          'msg_type': 'report_response',
          'payload': {'data_formats': [
            {'idx': 0, 'divider': 10, 'bytes': 2, 'signed': True, 'offset': 0, 'label': 'Requested fanspeed (%)'},
            {'idx': 1, 'divider': 10, 'bytes': 2, 'signed': False, 'offset': 2, 'label': 'Balance (%)'},
            {'idx': 2, 'divider': 1, 'bytes': 2, 'signed': False, 'offset': 4, 'label': 'supply fan (rpm)'},
            {'idx': 3, 'divider': 1, 'bytes': 2, 'signed': True, 'offset': 6, 'label': 'supply fan actual (rpm)'},
            {'idx': 4, 'divider': 1, 'bytes': 2, 'signed': False, 'offset': 8, 'label': 'exhaust fan (rpm)'},
            {'idx': 5, 'divider': 1, 'bytes': 2, 'signed': True, 'offset': 10, 'label': 'exhaust fan actual (rpm)'},
            {'idx': 6, 'divider': 100, 'bytes': 2, 'signed': True, 'offset': 12, 'label': 'supply temp (°C)'},
            {'idx': 7, 'divider': 100, 'bytes': 2, 'signed': True, 'offset': 14, 'label': 'exhaust temp (°C)'},
            {'idx': 8, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 16, 'label': 'Status'},
            {'idx': 9, 'divider': 100, 'bytes': 2, 'signed': True, 'offset': 17, 'label': 'Room temp (°C)'},
            {'idx': 10, 'divider': 100, 'bytes': 2, 'signed': True, 'offset': 19, 'label': 'Outdoor temp (°C)'},
            {'idx': 11, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 21, 'label': 'Valve position (pulse)'},
            {'idx': 12, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 22, 'label': 'Bypass position (pulse)'},
            {'idx': 13, 'divider': 10, 'bytes': 2, 'signed': True, 'offset': 23, 'label': 'Summercounter'},
            {'idx': 14, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 25, 'label': 'Summerday'},
            {'idx': 15, 'divider': 1, 'bytes': 2, 'signed': False, 'offset': 26, 'label': 'Frost timer (sec)'},
            {'idx': 16, 'divider': 1, 'bytes': 2, 'signed': False, 'offset': 28, 'label': 'Boiler timer (min)'},
            {'idx': 17, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 30, 'label': 'Frost block'},
            {'idx': 18, 'divider': 1, 'bytes': 2, 'signed': True, 'offset': 31, 'label': 'Current position'},
            {'idx': 19, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 33, 'label': 'VKKswitch'},
            {'idx': 20, 'divider': 1, 'bytes': 1, 'signed': False, 'offset': 34, 'label': 'GHEswitch'},
            {'idx': 21, 'divider': 1, 'bytes': 2, 'signed': False, 'offset': 35, 'label': 'Filter counter'}
          ]},
        })
        # autopep8: on

    def test_parsing_device_status_message(self):
        self.maxDiff = None

        # Parse and load status format:
        self.parser.parse(
            [0x80, 0x82, 0xA4, 0x00, 0x01, 0x16, 0x91, 0x11, 0x10, 0x90, 0x10,
             0x90, 0x92, 0x92, 0x00, 0x92, 0x92, 0x00, 0x00, 0x91, 0x00, 0x10,
             0x10, 0x00, 0x90, 0x00, 0x00, 0x10, 0xC8])

        # print(self.parser.message.inspect())

        # Query device status (err.. what's this?):
        # self.parser.parse(
        #     [0x82, 0x80, 0xA4, 0x01, 0x04, 0x00, 0x55]
        # )

        # print(self.parser.message.inspect())

        # Query device status (response):
        self.parser.parse(
            [0x80, 0x82, 0xA4, 0x01, 0x01, 0x25, 0x00, 0x00, 0x03, 0x9C, 0x03,
             0x9E, 0x03, 0x98, 0x03, 0xEB, 0x03, 0xEB, 0x09, 0x09, 0x09, 0x8A,
             0x00, 0x09, 0x09, 0x09, 0x8A, 0x00, 0x00, 0x0B, 0xB8, 0x01, 0x00,
             0x00, 0x00, 0xB1, 0x79, 0x00, 0x00, 0x00, 0x00, 0x10, 0x95, 0x9F, 0x01],
            skip_checksum=False)

        # print(self.parser.message.inspect())

        self.assertEqual(
            self.parser.message.inspect(),
            {'dest': 128,
                'src': 130,
                'msg_class': 'device_status',
                'msg_type': 'report_response',
                'payload': {0: {'label': 'Requested fanspeed (%)', 'value': 0.0},
                            1: {'label': 'Balance (%)', 'value': 92.4},
                            2: {'label': 'supply fan (rpm)', 'value': 926.0},
                            3: {'label': 'supply fan actual (rpm)', 'value': 920.0},
                            4: {'label': 'exhaust fan (rpm)', 'value': 1003.0},
                            5: {'label': 'exhaust fan actual (rpm)', 'value': 1003.0},
                            6: {'label': 'supply temp (°C)', 'value': 23.13},
                            7: {'label': 'exhaust temp (°C)', 'value': 24.42},
                            8: {'label': 'Status', 'value': 0.0},
                            9: {'label': 'Room temp (°C)', 'value': 23.13},
                            10: {'label': 'Outdoor temp (°C)', 'value': 24.42},
                            11: {'label': 'Valve position (pulse)', 'value': 0.0},
                            12: {'label': 'Bypass position (pulse)', 'value': 0.0},
                            13: {'label': 'Summercounter', 'value': 300.0},
                            14: {'label': 'Summerday', 'value': 1.0},
                            15: {'label': 'Frost timer (sec)', 'value': 0.0},
                            16: {'label': 'Boiler timer (min)', 'value': 177.0},
                            17: {'label': 'Frost block', 'value': 121.0},
                            18: {'label': 'Current position', 'value': 0.0},
                            19: {'label': 'VKKswitch', 'value': 0.0},
                            20: {'label': 'GHEswitch', 'value': 0.0},
                            21: {'label': 'Filter counter', 'value': 4245.0}},
             })

    def test_parsing_speed_setting_message(self):
        # 2-byte integer payload:
        # generated using `hru.set_exhaust_fan_rpm(1200)`
        self.parser.parse(
            [130, 128, 164, 16, 6, 19, 0, 0, 4, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 46, 0, 79])

        self.assertEqual(
            self.parser.message.payload.payload_value,
            1200
        )

        self.assertEqual(
            self.parser.message.msg_class,
            9232
        )

        self.assertEqual(self.parser.message.build().data,
                         [130, 128, 164, 16, 6, 19, 0, 0, 4, 176, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 46, 0, 79])

        # print(self.parser.message.inspect())

        self.assertEqual(
            self.parser.message.inspect(),
            {'dest': 130, 'src': 128, 'msg_class': 'config',
             'msg_type': 'write',
             'payload':
             {'value': 1200, 'setting_id': 46, 'data_type': 0,
              'type': {'bytes': 4, 'bitmask': 32, 'resolution': 1}}})

    def test_checksum_error(self):
        self.assertRaises(IthoPyException, self.parser.parse,
                          [0x82, 0x80, 0x24, 0x10, 0x04, 0x13, 0x00, 0x00, 0x00,
                           0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                           0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0xFF],)


if __name__ == '__main__':
    unittest.main()
