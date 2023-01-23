from .base_payload import BasePayload
from .data_format import DataFormat

class StatusFormatPayload(BasePayload):
    def __init__(self) -> None:
        self.data_formats = []

        # Clear any cached data formats to avoid order-dependent (test) failures:
        DataFormat.formats = []

        pass

    def parse(self, data):
        self.data = data

        self.data_formats = DataFormat.load(data)

        return self.data_formats

    def build(self):
        return self

    def __dict__(self):
        return {
            'data_formats': list(map(lambda x: x.to_dict(), self.data_formats)),
        }

    def to_dict(self):
      return self.__dict__()
