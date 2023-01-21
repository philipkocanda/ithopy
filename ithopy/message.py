from ithopy.constants import Constants

class Message:
  def __init__(self) -> None:
      self.intArr = []
      self.byteArr = []
      pass

  def to_hex(self, n):
    return '{0:02X}'.format(n)

  def calc_checksum(self, intArr):
    c = 0

    for i in intArr:
      c += i
      if c > 255: c -= 256

    if c > 0: return 256 - c

    return c

  def encode_msg_class(self, msg_class):
    num = msg_class >> 8
    byte0 = num + 128
    byte1 = msg_class - (num * 256)
    return [byte0, byte1]

  # Note: All bytes are stored as ints as long as possible before being returned
  def build(self):
    payload = self.payload.build().byteArr

    self.intArr = [
      self.dest,
      self.src,
      *self.encode_msg_class(self.msg_class),
      self.type,
      len(payload),
      *payload,
    ]

    self.checksum = self.calc_checksum(self.intArr)

    self.intArr.append(self.checksum)

    for i in self.intArr:
      self.byteArr.extend(self.to_hex(i))

    self.byteArr = list(map(self.to_hex, self.intArr))

    return self

  # this could be in a separate "serializer" class
  def inspect(self):
    return {
      "dest": self.src,
      "src": self.src,
      "msg_class": Constants.MSG_CLASSES.get(self.msg_class, f"<unknown: {self.msg_class}>"),
      "msg_type": Constants.MSG_TYPES.get(self.type, f"<unknown: {self.type}>"),
      "payload": self.payload.inspect(),
    }

  # bytestring representation of the message
  def __str__(self):
    return " ".join(self.build().byteArr)