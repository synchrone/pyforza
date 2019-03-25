from forza import TTPacket
from forza_proxy import ForzaProxy
from tests.test_ttpacket import chunked_img_packet


def test_proxy():
    s = ForzaProxy()
    in_packet = None

    for c in chunked_img_packet:
        if not in_packet:
            in_packet = s._in_packet[1]  # storing a ref
        s.observe(c, 1)

    assert isinstance(in_packet, TTPacket)
    assert in_packet.bytes_to_read == 0
    assert in_packet.is_valid()
