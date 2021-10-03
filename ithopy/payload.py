class Payload:
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
    # Create an empty data buffer with room for 19 bytes:
    self.byteArr = [0x0] * 19

    pass

  def build(self):
    num_bytes = self.payload_type['bytes']
    _bitmask = self.payload_type['bitmask']
    resolution = self.payload_type['resolution']

    self.byteArr[16] = 0 # data_type?
    self.byteArr[17] = self.setting_id # "index" column in the CSV

    value = self.payload_value * resolution

    # corresponds to "LongToByteArray" function:
    if (num_bytes > 0):
      self.byteArr[3] = value & 0xFF

    if (num_bytes > 1):
      self.byteArr[2] = (value >> 8) & 0xFF

    if (num_bytes > 2):
      self.byteArr[1] = (value >> 16) & 0xFF
      self.byteArr[0] = (value >> 24) & 0xFF

    return self

  # bytestring representation of the payload
  def __str__(self):
    return " ".join(self.build().byteArr)