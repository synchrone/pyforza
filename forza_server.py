#!/usr/bin/env python3
import random
from math import floor

import bluetooth as bt
import logging

import forza
from forza import format_bytes, TTPacket, b2i, i2b

logger = logging.getLogger(__name__)


def create_server():
    server_sock = bt.BluetoothSocket(bt.RFCOMM)
    server_sock.bind(("", bt.PORT_ANY))
    server_sock.listen(1)
    channel = server_sock.getsockname()[1]
    logger.debug('Listening on channel %d' % channel)

    bt.advertise_service(
        server_sock, forza.NAME,
        service_classes=[forza.UUID],
        profiles=[])

    return server_sock


def calculate_header(imglen):
    a = floor(imglen / 255) - 1
    return imglen - 70 - (a * 255)


def image_packet(image, counter=0, int1=1, int2=0):
    with open('img/%s.png' % image, 'rb') as img:
        imgdata = i2b(counter, 4) + i2b(int2, 4) + img.read()
        payload = i2b(int1) + i2b(len(imgdata), 4) + imgdata

        header = b"\x00"+i2b(calculate_header(len(imgdata) - 8), 2)
        p = TTPacket(type=forza.TYPE_FRAMES, header=header, payload=payload)
    return p


class ForzaServer:
    buffer = 1024
    client_sock = None
    ''':type: by.BluetoothSocket'''

    def _send(self, data):
        """
        :type data: Union[TomTomPacket,bytes,List[bytes]]
        """
        if isinstance(data, TTPacket):
            print('APP: ' + str(data))
            data = [bytes(data)]
        elif not isinstance(data, list):
            print('APP: ' + format_bytes(data))
            data = [data]
        else:
            for x in data:
                print('APP: ' + format_bytes(x))

        for x in data:
            self.client_sock.send(x)

    def _read(self, buffer=None):
        d = self.client_sock.recv(buffer or self.buffer)
        return d

    def listen(self):
        server = create_server()
        logger.info("Forza Server started")

        while True:
            self.client_sock, client_info = server.accept()
            logger.info("Accepted connection from VIO %s (%d)" % tuple(client_info))

            try:
                while True:
                    data = self._read()
                    if len(data) > 0:
                        self.handle_packet(data)
            except bt.BluetoothError as e:
                if e.args[0] == 104:
                    logger.warning('Connection reset by VIO')
                    break  # connection reset by peer, loop to accept again
            finally:
                self.client_sock and self.client_sock.close()

    def handle_packet(self, data):
        logger.debug('.')

        if data[3:5] != b"TT":
            print('VIO: ' + format_bytes(data))

        if data == forza.HELLO:
            self._send(forza.FZA_HELLO)
            logger.info('VIO HELLO -> FZA')

        elif data == forza.INFO[-1]:
            self._send(forza.FZA_START_TT)
            self._send(TTPacket(b"\x00\x00\xab", b"\x00\x01\x01"))
            # self._send(TTPacket(b"\x00\x00\xab", b"\x00\x01\x02"))
            self._send(TTPacket(b"\x00\x00\xaa", b"\x00\x0f"))  # app ready
            self._send(TTPacket(b"\x00\x00\xab", b"\x00\x01\x03"))  # app stage B-013
            logger.info('VIO INFO -> INIT')

        elif data == forza.START_TT_OK:
            logger.info('VIO START TT OK')

        elif data[3:5] == b"TT":
            packet = TTPacket.from_bytes(data)
            while packet.bytes_to_read > 0:  # chunked
                data = self._read(packet.bytes_to_read)
                packet.hydrate(data)
            print('VIO: '+str(packet))

            self.handle_command(packet)

    c_status = 0
    sent_counter = 0

    def handle_command(self, packet):
        if packet.type == forza.TYPE_INIT:
            if packet.header == b"\x00\x00\xac":
                self.c_status = b2i(packet.payload[-2:])
            elif packet.header == b"\x00\x00\xab" and packet.payload == b"\x00\x10\x0a":
                logger.info('VIO SHUTDOWN')
                sys.exit(0)

        elif isinstance(packet, forza.TTTouch):
            logger.info('touch %s @ %d, %d', 'down' if packet.down else 'up', packet.x, packet.y)

        if self.c_status >= 3:
            img = random.choice(['splash1', 'splash2'])
            p = image_packet(img, self.sent_counter)
            self._send(p)
            self.sent_counter += 1


if __name__ == '__main__':
    import sys
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    while True:
        try:
            ForzaServer().listen()
        except KeyboardInterrupt:
            break
