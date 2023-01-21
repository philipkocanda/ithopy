from ithopy.payloads import *

class Constants:
  MSG_CLASSES = {
    0: {
      'name': 'unknown message class',
      'payload_class': UnknownPayload,
    },
    9232: {
      # seems to be identical to [0x24, 0x10] (aka "2410")
      'name': 'config',
      'payload_class': ConfigPayload,
    },
    9216: {
      # [0xA4, 0x00]
      'name': 'status_format',
      'payload_class': StatusFormatPayload,
    },
    9217: {
      # [0xA4, 0x01]
      'name': 'device_status',
      'payload_class': DeviceStatusPayload,
    },
    9219: {
      'name': 'log_flags',
      'payload_class': UnknownPayload,
    },
    16432: {
      'name': 'raw_data_response',
      'payload_class': UnknownPayload,
    }
  }

  MSG_TYPES = {
    # The device sends a request/response to us:
    0: 'query_response',
    1: 'report_response', # ?
    2: 'change_response',

    # Sending a request to the device:
    4: 'query',
    5: 'report', # ?
    6: 'write',
  }

  DATA_TYPES = {
    0: '0, but what does that mean?',
  }
