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
        self.data = [0x0] * 19

        pass

    def parse(self, data):
        raise IthoPyException('Not implemented')

    def build(self):
        raise IthoPyException('Not implemented')

    def inspect(self):
        return self.__dict__()

    def __str__(self):
        """
        Hexacedimal bytestring representation of the message payload: '82 80 A4 10'
        """
        return " ".join(self.build().data)
