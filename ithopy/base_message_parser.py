from ithopy.message import Message
from ithopy.base_payload import BasePayload
from ithopy.config_payload import ConfigPayload
from ithopy.device_status_payload import DeviceStatusPayload
from ithopy.status_format_payload import StatusFormatPayload
from ithopy.unknown_payload import UnknownPayload
from ithopy.exceptions import *

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
    pass

  def to_hex(self, n):
    return '{0:02X}'.format(n)

  def parse(self, byteArr):
    self.message = Message()

    self.dest = byteArr[0]
    self.src = byteArr[1]
    self.msg_class = byteArr[2:4] # needs conversion
    self.type = byteArr[4]
    self.payload_length = byteArr[5]
    self.raw_payload = byteArr[6:len(byteArr) - 1]
    self.checksum = byteArr[len(byteArr) - 1]

    self.payload = ConfigPayload()
    self.payload.parse(self.raw_payload, BasePayload.DATA_TYPES['4_bytes']) # move to Payload class implementation

    self.message.dest = self.dest
    self.message.src = self.src
    self.message.msg_class = self.decode_msg_class(self.msg_class)
    self.message.type = self.type
    self.message.payload = self.payload
    self.message.build()

    self.validate_checksum()

  def decode_msg_class(self, msg_class):
    byte0, byte1 = msg_class

    return (byte0 - 128) * 256 + byte1

  def validate_checksum(self):
    if self.message.checksum != self.checksum:
      raise IthoPyChecksumError(f"Checksum mismatch! Received: `{self.to_hex(self.checksum)}`, calculated: `{self.to_hex(self.message.checksum)}`")