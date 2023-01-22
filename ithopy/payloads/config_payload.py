from ithopy.payloads import BasePayload
from ithopy.exceptions import IthoPyException


class ConfigPayload(BasePayload):
    PAYLOAD_SIZE = 19  # bytes

    def __init__(self) -> None:
        # Create an empty data buffer with room for 19 bytes:
        self.byte_list = [0x0] * self.PAYLOAD_SIZE
        self.data_type = 0  # not sure what this is, but it needs to be zero

        pass

    def parse(self, data, payload_type):
        if len(data) != self.PAYLOAD_SIZE:
            raise IthoPyException(
                f"Failed parsing config message payload: expected length to be {self.PAYLOAD_SIZE} bytes, actual length: {len(data)} bytes")

        self.data_type = data[16]
        # can be used to look up the correct payload_type, right?
        self.setting_id = data[17]
        self.payload_type = payload_type

        _num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        _resolution = self.payload_type['resolution']

        value = (
            data[0] << 24) | (
            data[1] << 16) | (
            data[2] << 8) | data[3]

        self.payload_value = value

        return self.payload_value

    def build(self):
        num_bytes = self.payload_type['bytes']
        _bitmask = self.payload_type['bitmask']
        resolution = self.payload_type['resolution']

        self.byte_list[16] = self.data_type
        self.byte_list[17] = self.setting_id  # "index" column in the CSV

        value = self.payload_value * resolution

        if (num_bytes > 0):
            self.byte_list[3] = value & 0xFF

        if (num_bytes > 1):
            self.byte_list[2] = (value >> 8) & 0xFF

        if (num_bytes > 2):
            self.byte_list[1] = (value >> 16) & 0xFF
            self.byte_list[0] = (value >> 24) & 0xFF

        return self

    def inspect(self):
        self.__dict__()

    def __dict__(self):
        return {
            "value": self.payload_value,
            "setting_id": self.setting_id,
            "data_type": self.data_type,
            "type": self.payload_type,
        }

    def __str__(self):
        'Bytestring representation of the payload'
        return " ".join(self.build().byte_list)
