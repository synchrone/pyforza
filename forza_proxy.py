#!/usr/bin/env python3
import logging
import sys
import select
from time import sleep
from typing import Dict

import bluetooth as bt
from bluetooth import BluetoothSocket, BluetoothError

import forza
from forza import TTPacket

logger = logging.getLogger(__name__)


DIR_UP = 1
DIR_DOWN = 2


class RfcommProxy:
    def __init__(self, upstream_addr=None, uuid=None, name=None, buffer_size=1004):
        if uuid:
            self.uuid = uuid
        if name:
            self.name = name

        self.upstream_addr = upstream_addr
        self.buffer_size = buffer_size

    def _create_server(self):
        server_sock = BluetoothSocket(bt.RFCOMM)
        server_sock.bind(("", bt.PORT_ANY))
        server_sock.listen(1)
        self.channel = server_sock.getsockname()[1]

        bt.advertise_service(
            server_sock, self.name,
            service_classes=[self.uuid],
            profiles=[])

        return server_sock

    def _create_client(self):
        assert self.uuid is not None
        logger.info("searching service %s (UUID: %s) @ %s" % (self.name, self.uuid, self.upstream_addr or 'anywhere'))

        service_matches = []
        while len(service_matches) == 0:
            try:
                service_matches = bt.find_service(uuid=self.uuid, address=self.upstream_addr)
                if len(service_matches) == 0:
                    sleep(1)
            except KeyboardInterrupt:
                break

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]

        logger.info("connecting to App \"%s\" on %s" % (name, host))

        # Create the client socket
        sock = BluetoothSocket(bt.RFCOMM)
        sock.connect((host, port))
        return sock

    def observe(self, data, dir):
        pass

    def listen(self):
        logger.info("Configuring RFCOMM server")
        server = self._create_server()
        upstream_sock = self._create_client()

        logger.info('Listening on channel %d, press Ctrl+C to exit' % self.channel)
        downstream_sock, client_info = server.accept()
        assert isinstance(downstream_sock, BluetoothSocket)
        logger.info("Accepted connection from VIO %s (%d)" % tuple(client_info))

        while True:
            try:
                rlist, wlist, xlist = select.select([upstream_sock, downstream_sock], [], [])
                for source in rlist:
                    assert isinstance(source, BluetoothSocket)

                    if source is downstream_sock:
                        target = upstream_sock
                        dir = DIR_UP
                    else:
                        target = downstream_sock
                        dir = DIR_DOWN

                    data = source.recv(self.buffer_size)
                    if len(data) > 0:
                        patched_data = self.observe(data, dir)
                        target.send(patched_data or data)

            except BluetoothError as e:
                if e.args[0] == 107:  # connreset
                    upstream_sock.close()
                    downstream_sock.close()
                    break

            except KeyboardInterrupt:
                raise

            except Exception as e:
                logger.exception('Unhandled exception in serve loop')


def format_dir(dir):
    return 'VIO: ' if dir == DIR_UP else 'APP: '


class ForzaProxy(RfcommProxy):
    name = forza.NAME
    uuid = forza.UUID

    _in_packet: Dict[int, TTPacket] = {DIR_UP: None, DIR_DOWN: None}

    def observe_raw_init(self, data, dir):
        logger.debug('.')
        print(format_dir(dir) + forza.format_bytes(data))

        if data[0] == 0x03 and dir == DIR_DOWN:  # app is sending pics
            sys.exit(0)

    def observe(self, data, dir):
        #logger.debug('.')
        chunked = self._in_packet[dir]

        if data[3:5] == b"TT":
            p = TTPacket.parse(data)
            if p.bytes_to_read > 0:
                self._in_packet[dir] = p
            else:
                pass
                #print(format_dir(dir) + str(p))

        elif chunked:
            chunked.hydrate(data)

            if chunked.bytes_to_read == 0:
                print(format_dir(dir) + str(chunked))

                if chunked.type == forza.TYPE_FRAMES and chunked.header != forza.FRAMES_ACK:
                    pass
                    #print(format_dir(dir) + '^^^' + forza.format_bytes(bytes(chunked)))

                self._in_packet[dir] = None
        else:
            pass
            #print(format_dir(dir) + forza.format_bytes(data))


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    while True:
        try:
            # does not work w/o address
            ForzaProxy("94:65:2D:7A:7A:09").listen()
        except KeyboardInterrupt:
            break
