from ithopy.message import Message
from ithopy.payload import Payload

# Message structure

# [0]     destination address
# [1]     reply address
# [2..3]  message class
# [4]     message type
# [5]     payload size in bytes
# [6..n]  payload
# [n+1]   checksum

class BaseMessageParser:
  def __init__(self) -> None:
    self.message = Message()
    self.payload = Payload()

  def parse(self, byteArr):
    self.dest = byteArr[0]
    self.src = byteArr[1]
    self.msg_class = byteArr[2:4] # needs conversion
    self.type = byteArr[4]
    self.payload_length = byteArr[5]
    self.raw_payload = byteArr[6:len(byteArr) - 1]
    self.checksum = byteArr[len(byteArr) - 1]

    self.payload.parse(self.raw_payload, Payload.DATA_TYPES['4_bytes'])

    self.message.dest = self.dest
    self.message.src = self.src
    self.message.msg_class = self.decode_msg_class(self.msg_class)
    self.message.type = self.type
    self.message.payload = self.payload

  def decode_msg_class(self, msg_class):
    byte0, byte1 = msg_class

    return (byte0 - 128) * 256 + byte1

  def verify_checksum(self):
    pass