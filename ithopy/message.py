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

  def encoded_msg_class(self):
    num = self.msg_class >> 8
    byte1 = num + 128
    byte2 = self.msg_class - (num * 256)
    return [byte1, byte2]

  # Note: All bytes are stores as ints as long as possible before being returned
  def build(self):
    payload = self.payload.build().byteArr

    self.intArr = [
      self.dest,
      self.src,
      *self.encoded_msg_class(),
      self.type,
      len(payload),
      *payload,
    ]

    self.intArr.append(self.calc_checksum(self.intArr))

    for i in self.intArr:
      self.byteArr.extend(self.to_hex(i))

    self.byteArr = list(map(self.to_hex, self.intArr))

    return self

  # bytestring representation of the message
  def __str__(self):
    return " ".join(self.build().byteArr)