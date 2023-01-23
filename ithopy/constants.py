from ithopy.payloads import UnknownPayload, ConfigPayload, StatusFormatPayload, DeviceStatusPayload


class Constants:
    MSG_CLASSES = {
        0: {
            'name': 'unknown message class',
            'payload_class': UnknownPayload,
        },
        9232: {
            # A410
            # 2410 (looks to be same as A410, but may have compatibility issues)
            'name': 'config',
            'payload_class': ConfigPayload,
        },
        9216: {
            # A400
            'name': 'status_format',
            'payload_class': StatusFormatPayload,
        },
        9217: {
            # A401
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
        },
        # The following msg classes are incorrectly parsed
        # (hex->int conversion only goes one way):
        #
        # B1D9 - Used by itho-wifi, purpose unclear
        # 31D9 - Used by itho-wifi, "Fan system status" <<- used to control fan speed? (either or both of these)
        # 31DA - Used by itho-wifi, "Ventilation status" <<- used to control fan speed? (either or both of these)
        # 2401 - Used by itho-wifi, "System status"
    }

    MSG_TYPES = {
        # The device sends a request/response to us:
        0: 'query_response',
        1: 'report_response',  # ?
        2: 'change_response',

        # Sending a request to the device:
        4: 'query',
        5: 'report',  # ?
        6: 'write',
    }

    DATA_TYPES = {
        0: '0, but what does that mean?',
    }
