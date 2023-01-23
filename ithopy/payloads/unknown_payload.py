from .base_payload import BasePayload


class UnknownPayload(BasePayload):
    def __init__(self) -> None:
        # Create an empty data buffer with room for 19 bytes:
        self.data = [0x0] * 19

        pass

    def parse(self, data):
        self.payload_value = data

        return self.payload_value

    def build(self):
        return self

    def __dict__(self):
        return {}
