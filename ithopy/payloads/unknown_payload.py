from .base_payload import BasePayload


class UnknownPayload(BasePayload):
    def __init__(self) -> None:
        # Create an empty data buffer with room for 19 bytes:
        self.byte_list = [0x0] * 19

        pass

    def parse(self, byte_list, payload_type):
        self.payload_value = byte_list

        return self.payload_value

    def build(self):
        return self

    def inspect(self):
        return {}

    # bytestring representation of the payload
    def __str__(self):
        return " ".join(self.build().byte_list)
