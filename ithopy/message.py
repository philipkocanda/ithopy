from ithopy.constants import Constants


class Message:
    def __init__(self) -> None:
        self.data = []
        pass

    def to_hex(self, n):
        return '{0:02X}'.format(n)

    def calc_checksum(self, data):
        c = 0

        for i in data:
            c += i
            if c > 255:
                c -= 256

        if c > 0:
            return 256 - c

        return c

    def encode_msg_class(self, msg_class):
        num = msg_class >> 8
        byte0 = num + 128
        byte1 = msg_class - (num * 256)
        return [byte0, byte1]

    # Note: All bytes are stored as ints as long as possible before being returned
    # err, we don't need to do this! ^
    def build(self):
        payload = self.payload.build().data

        self.data = [
            self.dest,
            self.src,
            *self.encode_msg_class(self.msg_class),
            self.type,
            len(payload),
            *payload,
        ]

        self.checksum = self.calc_checksum(self.data)

        self.data.append(self.checksum)

        return self

    # this could be in a separate "serializer" class
    def inspect(self):
        return {
            "dest": self.src,
            "src": self.src,
            "msg_class": Constants.MSG_CLASSES.get(self.msg_class, 0)['name'],
            "msg_type": Constants.MSG_TYPES.get(self.type, f"<unknown: {self.type}>"),
            "payload": self.payload.inspect(),
        }

    def bytes_list(self):
        "Returns list of bytes as strings: ['82', '80', 'A4', '10']"
        self.build()
        return list(map(self.to_hex, self.data))

    def __str__(self):
        "Returns bytestring: '82 80 A4 10'"
        self.build()

        data = list(map(self.to_hex, self.data))

        return " ".join(data)
