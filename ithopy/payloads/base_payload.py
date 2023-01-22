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
        self.byte_list = [0x0] * 19

        pass

    def parse(self, byte_list, payload_type):
        raise IthoPyException('Not implemented')

    def build(self):
        raise IthoPyException('Not implemented')

    def inspect(self):
        raise IthoPyException('Not implemented')

    # bytestring representation of the payload
    def __str__(self):
        return " ".join(self.build().byte_list)
