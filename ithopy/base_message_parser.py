from ithopy.message import Message
from ithopy.exceptions import IthoPyChecksumError
from ithopy.constants import Constants

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

    def parse(self, data, skip_checksum=False):
        self.message = Message()

        self.dest = data[0]
        self.src = data[1]
        self.msg_class = data[2:4]
        self.msg_class_int = self.decode_msg_class(self.msg_class)
        self.type = data[4]
        self.payload_length = data[5]
        self.payload_data = data[6:len(data) - 1]
        self.checksum = data[len(data) - 1]

        payload_class = Constants.MSG_CLASSES.get(
            self.msg_class_int, Constants.MSG_CLASSES[0])['payload_class']

        self.payload = payload_class()
        # move to Payload class implementation
        self.payload.parse(self.payload_data)  # move to constants?

        self.message.data = data
        self.message.dest = self.dest
        self.message.src = self.src
        self.message.msg_class = self.decode_msg_class(self.msg_class)
        self.message.type = self.type
        self.message.payload = self.payload

        if not skip_checksum:
            self.validate_checksum(data)

    def decode_msg_class(self, msg_class):
        byte0, byte1 = msg_class

        return (byte0 - 128) * 256 + byte1

    def validate_checksum(self, data):
        checksum = self.message.calc_checksum(data[:-1])
        if checksum != self.checksum:
            raise IthoPyChecksumError(
                f"Checksum mismatch! Received: `{self.to_hex(self.checksum)}`, calculated: `{self.to_hex(checksum)}`")
