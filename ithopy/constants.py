from ithopy.payloads import *

class Constants:
  MSG_CLASSES = {
    9232: {
      # seems to be identical to [0x24, 0x10] (aka "2410")
      'name': 'config',
    },
    9216: {
      # [0xA4, 0x00]
      'name': 'status_format',
      'payload_class': ConfigPayload,
    },
    9217: {
      # [0xA4, 0x01]
      'name': 'device_status',
    },
    9219: {
      'name': 'log_flags',
    },
    16432: {
      'name': 'raw_data_response',
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
