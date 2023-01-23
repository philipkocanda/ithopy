from .base_payload import BasePayload
from .data_format import DataFormat


class DeviceStatusPayload(BasePayload):
    def __init__(self) -> None:
        pass

    def parse(self, data):
        self.data = DataFormat.parse_data(data)
        return self.data

    def build(self):
        return self

    def __dict__(self):
        return self.data
