from ithopy.payloads import BasePayload


class StatusFormatPayload(BasePayload):
    def __init__(self) -> None:
        # Create an empty data buffer with room for 19 bytes:
        self.byteArr = [0x0] * 19
        self.data_type = 0  # not sure what this is, but it needs to be zero

        pass

    def parse(self, byteArr, payload_type):
        self.data_type = byteArr[16]
        # can be used to look up the correct payload_type, right?
        self.setting_id = byteArr[17]
        self.payload_type = payload_type

        _num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        _resolution = self.payload_type['resolution']

        value = (
            byteArr[0] << 24) | (
            byteArr[1] << 16) | (
            byteArr[2] << 8) | byteArr[3]

        self.payload_value = value

        return self.payload_value

    # Data format (1 byte):
    #
    # | Bit  | Description                        |
    # | ---- | ---------------------------------- |
    # | 7    | signed (1) / unsigned (0)          |
    # | 6..4 | size in bytes (2^n): 0=1, 1=2, 2=4 |
    # | 3..0 | decimal digits (divider 10^n)      |
    #
    # So for example `0x91` would mean "signed, 2 bytes, 0.1 values".
    #
    #   0b10010001 (0x91)
    #     1        (signed)
    #     ^001     (001 = 1 -> 2^1=2)
    #     |   0001 (0001 = 1 -> 10^1=10, so divide by 10 to get 0.1 resolution)
    #     |      ^
    #     |      |
    # bit 7......0
    def parse_format_byte(self, format_byte):
        {
            'divider': 10 ** int((format_byte >> 4) & 0b111),
            'size_bytes': 2 ** int(format_byte & 0b1111),
            'signed': (format_byte >> 7) & 0b1,
        }

    def build(self):
        num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        resolution = self.payload_type['resolution']

        self.byteArr[16] = self.data_type
        self.byteArr[17] = self.setting_id  # "index" column in the CSV

        value = self.payload_value * resolution

        if (num_bytes > 0):
            self.byteArr[3] = value & 0xFF

        if (num_bytes > 1):
            self.byteArr[2] = (value >> 8) & 0xFF

        if (num_bytes > 2):
            self.byteArr[1] = (value >> 16) & 0xFF
            self.byteArr[0] = (value >> 24) & 0xFF

        return self

    def inspect(self):
        return {
            # TODO
        }

    # bytestring representation of the payload
    def __str__(self):
        return " ".join(self.build().byteArr)
