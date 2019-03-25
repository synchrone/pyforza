import attr

UUID = "e74e3827-fc47-4e5c-bcfa-be7a86d59331"
NAME = "Forza App"

HELLO = b"\xff\x55\x02\x00\xee\x10"

FZA_HELLO = [
    b"\x46\x5a\x41",
    b"\x00\x00\x02\x00\x00",
    b"\x00\x00\x02\x00\x13\x00\x00\x02",
    b"\x00\x14"
]

INFO = [
    # 6 packets snipped
    b"\x00\x00\x16\x00\x14\x43\x48\x33\x33\x32\x37\x43\x30\x30\x30\x32\x38\x00\x00\x00\x06\x00\x00\x00\x00"
]

FZA_START_TT = b"\x00\x00\x03\x03\xfd\x01"
START_TT_OK = b"\x00\x00\x03\x03\xfd\x00"

TYPE_INIT = 0
TYPE_TOUCH = 1
TYPE_HEARTBEAT = 2
TYPE_FRAMES = 3

FRAMES_ACK = b"\x00\x00\xb8"


def format_bytes(data):
    return ''.join('\\x{:02x}'.format(x) for x in data)


def b2i(data: bytes):
    return int.from_bytes(data, byteorder='big')


def i2b(integer: int, len=2):
    return integer.to_bytes(len, byteorder='big')


@attr.s
class TTPacket:
    header = attr.ib()
    payload = attr.ib(default=bytes())
    payload_length = attr.ib(default=None)
    type = attr.ib(default=0)
    checksum = attr.ib(default=None)

    @property
    def bytes_to_read(self):
        return self.payload_to_read + 2 if not self.checksum else 0

    @property
    def payload_to_read(self):
        return self.payload_length - len(self.payload)

    def hydrate(self, data):
        payload_data = data[:self.payload_to_read]  # get as much as possible to fill payload
        self.payload += bytes(payload_data)

        if len(data) - len(payload_data) > 0:  # and the last 2 bytes are sum
            self.checksum = b2i(data[len(payload_data):len(payload_data)+2])

    def is_valid(self):
        return self.calculate_checksum() == self.checksum

    def calculate_checksum(self):
        return sum(self.payload) % 65536

    @classmethod
    def from_bytes(cls, data):
        assert data[3:5] == b"TT"

        if data[0] == TYPE_TOUCH:
            klass = TTTouch
        else:
            klass = TTPacket

        return klass.parse(data)

    @classmethod
    def parse(cls, data):
        length = b2i(data[1:3])
        inst = cls(type=int(data[0]), header=data[5:8], payload_length=length)
        inst.hydrate(data[8:])
        return inst

    def __str__(self):
        msg = 'TT %s|%s' % (hex(self.type), format_bytes(self.header))
        if self.type == TYPE_FRAMES and self.header != FRAMES_ACK:  # b8 is VIO img ok response
            int1, datalen, counter, int2 = (b2i(self.payload[0:2]), b2i(self.payload[2:6]),
                                            b2i(self.payload[6:10]), b2i(self.payload[10:14]))

            msg += '/%d' % b2i(self.header[1:])

            msg += ': %s +PNG (%d)' % (
                (int1, datalen, counter, int2),
                len(self.payload) - 14)

            msg += 'x=%d' % (len(self.payload) - 14 - b2i(self.header[1:]))
        else:
            msg += ': ' + format_bytes(self.payload)

        if not self.checksum:
            self.checksum = self.calculate_checksum()

        if not self.is_valid():
            msg += ', sum nok: %s vs %s/%d' % (
                format_bytes(i2b(self.calculate_checksum())),
                format_bytes(i2b(self.checksum)),
                self.checksum
            )
        return msg

    def __bytes__(self):
        """{
            TYPE: 0x03,
            LENGTH: { len(PAYLOAD), 2bytes },
            MAGIC: b"TT",
            HEADER: { 0x00, 0x00, 0x00 },
            PAYLOAD: {
                int1: { 2 bytes, always 1 },
                datalen: { len(counter + int2 + imagedata), 4 bytes },
                counter: { 4 bytes },
                int2: { 4 bytes, always 0 },
                imagedata: PNG
            },
            CHECKSUM: { sum(PAYLOAD) % 65536, 2 bytes }
        }
        """
        if not self.checksum:
            self.checksum = self.calculate_checksum()

        if not self.payload_length:
            self.payload_length = len(self.payload)

        data = bytes([self.type]) + \
           i2b(self.payload_length) + \
           b"TT" + \
           self.header + \
           self.payload + \
           i2b(self.checksum)
        return data


@attr.s
class TTTouch(TTPacket):
    int1 = attr.ib(default=None)  # always 1
    down = attr.ib(default=None)
    x = attr.ib(default=None)
    y = attr.ib(default=None)
    int2 = attr.ib(default=None)
    int3 = attr.ib(default=None)

    @classmethod
    def parse(cls, data):
        inst = super().parse(data)
        # header = \x00\x00\xb9
        # payload= \x00\x01\x00\xff\x00\xaa\x00\x68\x00\x00\x37\x81\x00\x00\x00\x62

        args = [b2i(inst.payload[i:i+2]) for i in [0, 2, 4, 6]]
        args += [b2i(inst.payload[i:i+4]) for i in [8, 12]]

        inst.int1, inst.down, inst.x, inst.y, inst.int2, inst.int3 = args

        return inst
