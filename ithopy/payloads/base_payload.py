from ithopy.exceptions import IthoPyException


class BasePayload:
    DATA_TYPES = {
        "1_byte": {
            "bytes": 1,
            "bitmask": 0,
            "resolution": 1,
        },
        "2_bytes": {
            "bytes": 2,
            "bitmask": 16,
            "resolution": 1,
        },
        "4_bytes": {
            "bytes": 4,
            "bitmask": 32,
            "resolution": 1,
        },
        "bool": {
            "bytes": 4,
            "bitmask": 3,
            "resolution": 1000,
        },
        "4_bits": {
            "bytes": 1,
            "bitmask": 4,
            "resolution": 10000,
        },
        "12_bits": {
            "bytes": 2,
            "bitmask": 5,
            "resolution": 100000,
        },
        "float": {
            "bytes": 4,
            "bitmask": 7,
            "resolution": 1E+07,
        },
    }

    def __init__(self) -> None:
        self.byteArr = [0x0] * 19

        pass

    # Data format (1 byte):

    # | Bit  | Description                        |
    # | ---- | ---------------------------------- |
    # | 7    | signed (1) / unsigned (0)          |
    # | 6..4 | size in bytes (2^n): 0=1, 1=2, 2=4 |
    # | 3..0 | decimal digits (divider 10^n)      |

    # TODO:
    # Each message class might need its own payload and parser.
    # For instance the device status message. See format above.
    #
    # Or perhaps there is some way of knowing when
    # there are multiple data values sent at once?
    def parse(self, byteArr, payload_type):
        raise IthoPyException('Not implemented')

    def build(self):
        raise IthoPyException('Not implemented')

    def inspect(self):
        raise IthoPyException('Not implemented')

    # bytestring representation of the payload
    def __str__(self):
        return " ".join(self.build().byteArr)
