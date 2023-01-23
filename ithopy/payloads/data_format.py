class DataFormat:
    'Data format representing one or more bytes in the device status payload'

    formats = []
    byte_offset = 0

    # TODO: Read from CSV based on device type and hardware/software version
    labels = [
        "Requested fanspeed (%)",
        "Balance (%)",
        "supply fan (rpm)",
        "supply fan actual (rpm)",
        "exhaust fan (rpm)",
        "exhaust fan actual (rpm)",
        "supply temp (°C)",
        "exhaust temp (°C)",
        "Status",
        "Room temp (°C)",
        "Outdoor temp (°C)",
        "Valve position (pulse)",
        "Bypass position (pulse)",
        "Summercounter",
        "Summerday",
        "Frost timer (sec)",
        "Boiler timer (min)",
        "Frost block",
        "Current position",
        "VKKswitch",
        "GHEswitch",
        "Filter counter",
    ]

    def __init__(self, divider=None, bytes=None, signed=None) -> None:
        self.idx = len(DataFormat.formats)
        self.divider = divider
        self.bytes = bytes
        self.signed = signed
        self.offset = DataFormat.byte_offset

        DataFormat.byte_offset = DataFormat.byte_offset + bytes

    @staticmethod
    def load(payload):
        DataFormat.formats = []
        DataFormat.byte_offset = 0

        for format_byte in payload:
            DataFormat.formats.append(DataFormat.from_byte(format_byte))

        return DataFormat.formats

    @staticmethod
    def data_size():
        "Computes expected data size by summing all parsed format bytes"
        return DataFormat.byte_offset + DataFormat.formats[-1].bytes

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
    @staticmethod
    def from_byte(format_byte):
        return DataFormat(
            divider=10 ** int(format_byte & 0b1111),
            bytes=2 ** int((format_byte >> 4) & 0b111),
            signed=bool((format_byte >> 7) & 0b1),
        )

    @staticmethod
    def parse_data(data):
        "Parses given data using previously received formats"
        results = {}

        if len(DataFormat.formats) == 0:
            raise Exception(
                "Formats list is unpopulated! Use the `load` method to load formats before parsing data."
            )

        if DataFormat.data_size() != (len(data) + 1):
            raise Exception(
                f"Expected payload size to be {DataFormat.data_size()}, instead got {(len(data) + 1)}")

        for data_format in DataFormat.formats:
            fragment = data[data_format.offset:(
                data_format.offset + data_format.bytes)]

            value = 0
            for idx, b in enumerate(fragment):
                value = (value << (8 * idx)) | b

            if data_format.signed:
                if value & (1 << (data_format.bits() - 1)):
                    value -= 1 << data_format.bits()

            value = value / data_format.divider

            results[data_format.idx] = {
                'label': data_format.label(),
                'value': value,
            }

        return results

    def label(self):
        return DataFormat.labels[self.idx]

    def bits(self):
        return self.bytes * 8

    def __dict__(self):
        return {
            'idx': self.idx,
            'divider': self.divider,
            'bytes': self.bytes,
            'signed': self.signed,
            'offset': self.offset,
            'label': self.label(),
        }

    def to_dict(self):
        return self.__dict__()

    def __str__(self):
        return str(self.__dict__())
