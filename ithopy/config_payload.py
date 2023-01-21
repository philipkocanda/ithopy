from ithopy.base_payload import BasePayload
from ithopy.exceptions import IthoPyException

class ConfigPayload(BasePayload):
  PAYLOAD_SIZE = 19 # bytes

  def __init__(self) -> None:
    # Create an empty data buffer with room for 19 bytes:
    self.byteArr = [0x0] * self.PAYLOAD_SIZE
    self.data_type = 0 # not sure what this is, but it needs to be zero

    pass

  def parse(self, byteArr, payload_type):
    if len(byteArr) != self.PAYLOAD_SIZE:
      raise IthoPyException(f"Failed parsing config message payload: expected length to be {self.PAYLOAD_SIZE} bytes, actual length: {len(byteArr)} bytes")

    self.data_type = byteArr[16]
    self.setting_id = byteArr[17] # can be used to look up the correct payload_type, right?
    self.payload_type = payload_type

    _num_bytes = self.payload_type['bytes']
    _bitmask = self.payload_type['bitmask']
    _resolution = self.payload_type['resolution']

    value = (byteArr[0] << 24) | (byteArr[1] << 16) | (byteArr[2] << 8) | byteArr[3]

    self.payload_value = value

    return self.payload_value

  def build(self):
    num_bytes = self.payload_type['bytes']
    _bitmask = self.payload_type['bitmask']
    resolution = self.payload_type['resolution']

    self.byteArr[16] = self.data_type
    self.byteArr[17] = self.setting_id # "index" column in the CSV

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
    {
      "value": self.payload_value,
      "setting_id": self.setting_id,
      "data_type": self.data_type,
      "type": self.payload_type,
    }

  # bytestring representation of the payload
  def __str__(self):
    return " ".join(self.build().byteArr)