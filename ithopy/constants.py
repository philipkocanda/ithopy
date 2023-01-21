class Constants:
  MSG_CLASSES = {
    9232: 'config', # 2410

    9216: 'status_format', # = [0xA4, 0x00]
    9217: 'device_status', # = [0xA4, 0x01]

    9219: 'log_flags',

    16432: 'raw_data_response',
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
