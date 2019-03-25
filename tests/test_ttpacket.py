import pytest

from forza import TTPacket, TYPE_FRAMES, format_bytes, TYPE_INIT, i2b
from forza_server import calculate_header

img_packet = [
    b"\x03\x0b\x64\x54\x54\x00\x01\x1a\x00\x01\x00\x00\x0b\x5e\x00\x00\x00\x00\x00\x00\x00\x00\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x01\x40\x00\x00\x01\x40\x08\x03\x00\x00\x00\xfa\x4e\x55\x98\x00\x00\x01\x17\x50\x4c\x54\x45\xd9\xd9\xd9\x00\x00\x00\x66\x66\x66\xff\xff\xff\xff\x66\xff\xcc\x51\xcc\xaa\xaa\xaa\x99\x99\x99\x33\x33\x33\x00\x00\x00\xe0\xe0\xe0\xcc\xcc\xcc\xde\xde\xde\xf0\xf0\xf0\xff\xff\xff\xfb\xfb\xfb\xf7\xf7\xf7\xa6\xa6\xa6\x99\x3d\x99\x8c\x8c\x8c\xe9\xe9\xe9\x73\x73\x73\xe0\x59\xe1\xf4\xf4\xf5\xf2\xf2\xf3\xe4\xe4\xe5\x70\x70\x71\xfa\xfa\xfb\xd4\xd4\xd5\xc1\xc1\xc2\xe1\xe1\xe2\xa3\x72\x27\xb3\xcb\x35\x00\x6c\x87\xeb\xeb\xec\x80\x39\x08\x00\x5b\x89\x2d\x63\xa7\xb7\x49\xb8\x00\x8a\x90\xbc\x84\x2d\x00\x80\x99\x00\x9c\xa2\x23\x4d\x80\xa4\x00\x00\xa5\x00\x00\xc0\xd8\xe8\xd8\xe4\xf0\xb0\xc8\x80\x03\x60\x33\xb2\x83\x00\xff\x00\xcc\x00\x99\xb8\x46\x99\xff\x3d\x85\x06\x00\xb7\xbd\x98\xc0\xd8\xcc\x5a\x0c\xfb\xb0\x3b\x7a\x5b\xb8\x88\x66\xcc\xa8\xcc\xe0\x48\x62\x81\xc9\x98\x00\x00\xaa\xcc\xce\x00\x00\x52\xb1\x07\xaa\x80\xff\xd8\xa7\x00\x7e\x58\x1e\x00\xba\xe1\x3b\x82\xd9\x00\x5d\x63\x06\xb6\x63\xd5\x95\x33\xff\x00\x99\x67\x00\x00\xe7\xb6\x00\xff\x71\x10\x34\x73\xc0\x95\x70\xe1\x5a\x7b\xa2\xff\x30\x07\x26\xa7\xdf\x2d\x3e\x51\x00\x78\x7f\xff\xcc\x00\x66\x4c\x99\x00\xd4\xff\xff\xcc\x00\x00\xdc\xff\x00\xcc\xff\x00\xe7\xff\xb9\xb9\x2f\xbf\x00\x00\x09\xfa\x49\x44\x41\x54\x78\x9c\xed\xdd\x4b\x8e\xa3\x4a\x10\x85\xe1\x9a\x32\x29\x79\x25\x78\x64\xc9\x13\x4b\xbd\x07\xf6\xbf\x97\x2e\xb0\x0d\x09\xe4\x3b\x22\xe3\x04\x10\xff\xec\xde\xea\x92\x33\x3e\x01\x06\xfc\xa8\x9f\x4e\x5b\xff\xa2\xa1\x57\xb7\xeb\x07\xbd\x80\xb9\x38\x9c\x5a\x48\x0d\x80\x65\x74\xca\x18\xc1\x80\xf5\x76\x5a\x14\x71\x80\x1c\x76\x0a\x14\x41\x80\xbc\x7a\x48\x43\x00\x60\x0b\x3c\x1c\xa2\x34\x60\x4b\x3d\x88\xa1\x28\x60\x7b\x3d\x79\x43\x39\x40\x29\x3d\x61\x43\x21\x40\x59\x3d\x49\x43\x11\x40\x04\x9f\x14\x61\x7b\x40\x94\x9e\x90\x61\x6b\x40\x2c\x9f\x00\x61\x5b\x40\x34\xde\xbb\xa6\x23\xb6\x04\x44\xc3\x2d\x35\x1c\xb2\x1d\x20\x1a\x6d\x5d\xb3\x31\x5b\x01\xa2\xc1\xf6\x35\x1a\xb4\x0d\x20\x1a\xcb\x5f\x93\x51\x5b\x00\xa2\xa1\xc2\x35\x18\x96\x1f\x10\x8d\x14\x8f\x7d\x5c\x6e\x40\x34\x50\x3a\xe6\x81\x99\x01\xd1\x3a\x39\xf1\x4e\xcc\x0a\x88\xa6\xc9\x8d\x73\x66\x4e\x40\xb4\x4b\x7e\x8c\x43\xf3\x01\xa2\x51\xca\x62\x1b\x9b\x0b\x10\x0d\x52\x1e\xd3\xe0\x4c\x80\x68\x8d\x9a\x78\x26\x67\x01\x44\x53\xd4\xc6\x31\x3b\x07\x20\xda\xa1\x3e\x86\xe1\x19\x00\xd1\x0a\x94\x14\x00\xa2\x09\xa8\xa1\x01\xd1\xf3\xd3\xc3\x02\xa2\xa7\xe7\x08\x08\x88\x1e\x9d\x2b\x14\x20\x7a\x6e\xbe\x30\x80\xe8\xa9\x39\x43\x00\xa2\x67\xe6\x4d\x1e\x10\x3d\x31\x77\xc2\x80\xe8\x71\x5b\x24\x09\x88\x9e\xb5\x4d\x72\x80\xe8\x49\x5b\x25\x05\x88\x9e\xb3\x5d\x32\x80\xe8\x29\x5b\x26\x01\x88\x9e\xb1\x6d\xed\x01\xd1\x13\xb6\xae\x35\x20\x7a\xbe\xf6\xb5\x05\x44\x4f\x27\x51\x4b\x40\xf4\x6c\x32\xb5\x03\x44\x4f\x26\x55\x2b\x40\xf4\x5c\x72\xb5\x01\x44\x4f\x25\x59\x0b\x40\xf4\x4c\xb2\xf1\x03\xa2\x27\x92\x8e\x1b\x10\x3d\x8f\x7c\x06\x48\x8c\x17\x10\x3d\x0d\x22\x4e\x40\xf4\x2c\x98\xf8\x00\xd1\x93\xa0\xe2\x02\x44\xcf\x81\x8b\x07\x10\x3d\x05\x32\x03\x24\xc6\x01\x88\x9e\x01\x1b\x1d\x10\x3d\x01\x3a\x2a\x20\x7a\xfd\xf8\x0c\x90\x18\x0d\x10\xbd\x7a\x0d\x51\x00\xd1\x6b\xd7\x51\x3d\x20\x7a\xe5\x5a\x32\x40\x62\xb5\x80\xe8\x75\xeb\xa9\x0e\x10\xbd\x6a\x4d\x19\x20\xb1\x1a\x40\xf4\x9a\x75\x65\x80\xc4\xca\x01\xd1\x2b\xd6\x56\x29\x20\x7a\xbd\xfa\x32\x40\x62\x65\x80\xe8\xd5\x6a\xac\x04\x10\xbd\x56\x9d\x19\x20\xb1\x7c\x40\xf4\x4a\xb5\x66\x80\xc4\x72\x01\xd1\xeb\xd4\x9b\x01\x12\xcb\x03\x44\xaf\x52\x73\x06\x48\x2c\x07\x10\xbd\xc6\xb9\xe1\xd5\xff\x4e\xf5\xaf\x01\xbd\x96\xb9\xe3\x00\x3e\xef\xbf\x4e\xf7\x27\x7a\x3d\x9f\xd2\x80\xe8\x15\xbe\x7b\xac\xf8\x26\xc2\x07\x7a\x4d\xef\x8e\x01\xf8\xda\xf2\x8d\xbd\xd0\xab\x9a\x4a\x01\xa2\xd7\x37\xb5\xdb\xfc\x3e\x1b\x21\x7a\x5d\x53\x07\x00\x0c\xf8\x29\x11\x8c\x03\xa2\x57\x37\xe6\xdd\x7f\x15\xed\xc5\xda\x01\x1f\x61\xbf\xdf\x5f\x0d\xcf\x24\x31\x40\xf4\xda\xc6\x6e\x2e\xd8\xad\xef\xd7\xff",
    b"\x8d\x5e\xdd\x98\x6e\xc0\xa7\xbb\xc7\x4e\x27\xd0\x83\xbb\x4f\x6b\x38\x1f\x0c\x03\xa2\x57\x36\xb6\x6c\x70\xf7\xf9\xfa\x63\xb8\xeb\xdd\x04\xb5\x01\x2e\x47\xc0\xd5\x53\xee\x22\xa8\xed\x28\x28\x09\xe8\xee\x9d\xc9\x36\x9b\xda\x2d\xfd\x1b\x72\xfb\x79\x08\xb0\xf1\xc3\xfe\x1b\x4a\x10\x36\x5b\x5a\xf4\xb9\x79\x5b\xf3\x7b\x0f\x07\x00\xdc\x1d\xeb\x4a\x36\x41\x10\x60\xeb\x47\x8d\x5c\x62\xec\xeb\xb7\xbf\xdb\xe7\xff\xae\xc0\x05\x0b\x08\xb0\xe0\x20\xb8\x3b\x8c\x51\x7e\x97\x3f\x10\x60\xc1\x7e\x48\x00\x94\x38\xd3\xf1\x01\x0a\x3c\x6c\xc1\x53\xc1\xee\xaa\x37\x72\x85\xbc\x49\xe4\x44\x07\x04\x98\xcf\xb0\x3b\x8e\x65\x1f\x3f\x65\x6e\x38\xa0\x00\xf3\x05\x37\xcf\xa4\xd9\xcf\xe0\x42\x37\x6c\xf6\x80\x32\x8f\xeb\xbb\x59\xef\x6f\xf3\x34\xdc\xe7\xfd\x96\xdc\x8d\x7f\x18\xe0\x1f\x61\x9f\xf5\x5c\xb2\xa2\xc8\x3a\x78\xde\x7a\xc1\xeb\x3c\x20\x60\x34\x47\xea\x91\xfa\xbf\xd0\xb6\x80\xe8\xf5\xcc\x39\x5b\xe7\x7c\x38\x73\x0e\x9c\x2a\xee\xc6\x4c\x69\x05\x74\xcf\xf7\x6e\xaf\xc7\x30\x3c\x5e\xee\x1e\xaf\xe1\x7e\xe0\x3b\xad\x80\xf1\x93\x6d\x3d\x1b\xe0\x06\x10\xbd\x1a\x27\xf5\xaf\x89\x7c\xd3\x0a\xa8\xfe\x55\xb9\x6f\x6a\x01\xc3\x82\xaa\xfc\x14\x03\x86\x04\x75\xf9\xad\x00\xd1\x6b\xd9\xf6\xf0\x3c\x93\xdc\x34\x1d\xff\xa6\x14\x03\xae\x5f\xca\x7c\x6f\x7e\x7a\xde\x23\xf8\x4d\x33\xe0\x48\xe8\x5c\x34\xdf\x15\xf2\xb9\x80\xd0\x65\x3c\xbe\x6f\x44\xdd\xdf\x81\x79\x3c\xfb\xbf\x9e\x8f\xd0\x9d\x99\x5e\xf2\xe2\xd7\x93\x06\xc0\xa7\x7b\xb4\xbb\x65\x6d\x67\xc3\xea\x57\x90\x97\x26\x0a\x00\x37\xf7\xb6\x72\x04\x87\xcd\x13\x0c\xf0\x3d\x6f\x78\xc0\xdd\xbd\xc1\xb4\xe0\xd6\x0f\x79\x79\x07\x07\xf4\xdd\x5b\x4d\xec\x92\xbe\xd7\x96\x60\xdb\xe0\x17\x10\xf5\xf8\xfe\x17\xda\xfa\xc8\x46\x38\xf4\xde\x5f\x81\x1d\x07\xc1\x80\x81\xfb\x2e\xe1\xe7\x85\x67\xe8\x37\x24\x57\xed\x86\x05\x0c\xdf\x76\xf1\x13\x86\xf8\x7e\x71\x37\x69\xb0\x80\xd1\x17\xe8\xb6\x67\x78\x8f\xf8\xbf\xc6\x4c\x00\x06\xec\x63\x24\xbf\xe3\xe5\xc7\x73\x98\x7a\xbe\x52\xaf\xe4\xa1\x9e\x46\xde\x80\xa0\x07\xff\x97\x40\x29\x0a\x35\x83\x01\x12\x33\x40\x62\x06\x48\x4c\x11\xe0\xdf\x53\x46\xde\x3b\x16\xc6\x77\x20\xec\x9e\x56\x50\x33\xa8\x01\xfc\xdc\x6e\x8e\x9c\xea\x2d\xff\xf4\x7d\x92\xb8\xbe\x69\x8d\x9a\x61\x04\x44\x3d\xb6\x0b\x38\x9f\x86\xec\x6f\x15\xec\xfc\xe6\x2b\x3d\x77\x23\xc4\x4c\xf0\x97\x12\xc0\xe5\xf2\x37\xf9\x46\xd4\xe5\x22\xc5\x7d\xc7\x1b\x62\xfd\x53\x3a\x00\xdd\x0b\x89\xc4\x39\xb3\x7b\xca\xec\x5c\x9c\x48\xaf\x7d\x4e\x07\xa0\x7b\xd9\x96\x78\x07\xa6\xfb\xd2\xa6\x73\x31\x2d\xbd\xf6\x39\x1d\x80\xee\x0d\xac\xc4\x3e\xec\xde\x66\x70\xf6\x61\xe9\xb5\xcf\x19\x20\x31\x1d\x80\xee\x7e\xd9\xc7\x01\xdd\xc3\xa5\x63\x2d\xbd\xf6\x39\x1d\x80\xce\x33\x43\xf2\xcd\xe4\xce\xd6\xea\x3c\xdf\xc8\xaf\xfe\x53\xf7\x03\x7b\x68\xf7\x34\x66\xd9\x04\x13\x1b\xa0\xbb\x09\xba\x4f\x37\x88\xf5\xbf\xfb\xc1\x3d\xb4\xcb\xf2\x15\x4c\xfa\x2d\x82\xab\x83\x25\x6a\x06\x35\x80\xbf\xf7\xc7\xf0\x6f\xc8\xb9\x92\x1b\xaf\xe5\xfe\xfe\xe9\xe6\xd3\x12\xb8\x29\x7e\x70\x0f\x9d\x83\x95\x1b\x6e\x8a\x1f\xdc\x43\x1b\x20\x31\x03\x24\x66\x80\xc4\x0c\x90\x98\x01\x12\x33\x40\x62\x06\x48\xcc\x00\x89\x19\x20\x31\x03\x24\x66\x80\xc4\x0c\x90\x98\x01\x12\x33\x40\x62\x06\x48\xcc\x00\x89\x19\x20\x31\x03\x24\x66\x80\xc4\x0c\x90\x98\x01\x12\x33\x40\x62\x29\x94\xfb\xeb\xfd\x51\xf5\xe1\x91\xfc\xa0\x8d\x01\xee\xba\xad\xbf\x25\x61\x78\xc5\x5f\x73\x47\xcd\xa0\x16\xd0\xf3\x15\x31\xd1\x77\x5e\xca\xaf\xfe\xdb\x0f\xee\xa1\xc3\x1c\x77\xef\x47\x86\x87\xc8\x8e\x2c\xbd\xf6\x25\x15\x6f\x6f\xdb\x14\xfc\xec\x65\x78\x23\x94\x5c\xf7\x2a\x1d\xef\x0f\x5c\x17\xf9\x86\xa7\xa0\xa0\xdc\xaa\x37\x29\x04\x8c\x7e\x43\x56\x48\x50\x6a\xcd\xbb\xf4\x01\x26\x3e\xfa\x1b\x38\x0e\xca\xac\xd8\x93\x3a\xc0\xd4\xf7\x9e\x04\x3e\xca\x24\xb3\x62\x4f\xea\x00\x57\xef\xc2\x7f\x9f\x40\xaf\xbf\x38\xcb\xff\x2e\x7e\xe9\xb5\xcf\x69\x03\x74\x77\xe0\x7e\xf9\xdf\xbd\xff\xad\xe5\x06\xb8\x6b\xf9\xcc\xd2\x7a\x5f\x75\xf6\x6c\xef\x97\x7d\x20\xd6\x3f\xa5\xe5\xe3\xae\x5f\xa7\xf9\x87\xdb\x63\x9d\x23\xe8\x3b\x0a\x22\xd6\x3f\xa6\xe6\xf3\xc2\x9f\x96\x53\x98\xfd\xb7\x6a\xcd\x3f\xf2\x9d\xca\x20\xd6\x3f\xa6\x0d\x70\xde\x83\x3d\x48\x33\xae\x6f\x1f",
    b"\xc6\x4c\xa0\x0f\x70\x88\xfc\x2c\xfa\x43\xcc\x04\xea\x00\xe7\xdd\xd4\x7b\xae\x32\x9f\xe1\x78\x0e\x82\x98\x09\xd4\x01\xce\x77\x11\x7a\x1f\x60\xec\xa7\x98\x09\x3e\x80\x28\xc1\x08\x91\xf7\x5c\x6f\x3e\x47\xd4\x03\x88\xfd\xee\xac\x08\xa0\xcf\x6f\x51\x32\xc0\x77\x06\x48\xcc\x00\x89\x9d\x07\x10\x24\x78\x7c\x40\xf0\xb7\xf8\x1a\x20\x31\x03\x24\x66\x80\xc4\x4e\x04\x88\x11\x3c\x3c\x20\xfa\xef\x89\x34\x01\x1c\x9e\xfd\xfd\xde\x3f\x45\xfe\xfc\xc8\x19\x01\x87\x3f\xbe\xb1\xd8\xf7\xc9\xb3\x85\xfe\xa3\x54\xfb\x3b\x06\xd5\x80\xdf\xfb\x0c\x5f\x3f\x11\x41\xf8\x5f\xf5\xda\x3b\x54\x03\xce\x5f\xc6\x73\x9f\x6b\xff\x07\x0a\xe0\x80\xfb\xbb\xa6\xd5\x80\x5f\xad\x7e\x01\x6c\xff\xed\xf0\x70\xc0\x3d\x53\x35\xe0\x77\x7f\xbd\x3b\x35\x5f\xfe\x0a\x10\x22\xb8\x7b\xe5\xa8\x16\x70\x7e\xbd\x49\x12\xb0\xc3\x03\xee\x9e\x46\x2a\x01\x17\x2b\xc9\x5d\x58\x03\xe0\xf6\xd5\xf3\x3a\x40\xe7\x35\x77\xc9\x27\x91\x0d\x20\x48\x70\xbd\x0d\x56\x01\xba\xef\xe7\x12\x3c\x8d\xe9\x54\x00\x6e\x8e\x83\x35\x80\xeb\xf7\x63\xca\x9d\x48\x6b\x01\x5c\xfd\x09\xc8\x62\xc0\xfd\x9f\x8c\x14\xbb\x94\xdb\x01\xaa\xfa\xfb\x9a\x71\x40\x0d\x75\x06\x48\xcb\x00\x89\x79\x00\x35\x09\xaa\x07\xec\x0c\x90\x96\x01\x12\xf3\x02\x2a\x12\xd4\x0e\xd8\x19\x20\xad\x00\xa0\x1e\x41\xe5\x80\x9d\x01\xd2\x32\x40\x62\x41\x40\x35\x82\xba\x01\x3b\xfd\x80\xf1\xb7\xf8\xa2\x8b\x00\x6a\x11\xec\x7d\x80\xed\x5f\x26\xca\xab\x3b\x00\x60\xfc\x63\x0e\xe0\xa2\x80\x4a\x04\xbd\x7f\x18\x48\xe4\xed\x1a\xe9\xba\x23\x00\x46\x3f\xea\x05\x2e\x01\xa8\x45\x70\xf7\x69\xa4\x5b\xfa\x77\x44\xda\x7a\x69\x05\x8c\x7c\xdc\x15\x5b\x12\x50\xa7\xa0\x5a\x3f\xbd\x80\xc1\x8f\xfc\x63\xcb\x00\xd4\x23\xe8\xfd\xd2\x09\x6c\x7b\x2d\xcd\x80\x63\x83\x1e\xbc\xb1\x2c\x40\x5d\x82\xaa\xf2\x60\x19\x60\x49\x99\x80\x26\x18\xc8\x67\x65\x80\x05\x65\x03\x9a\xa0\x37\x2f\x95\x01\xe6\x57\x00\x68\x82\x9e\xfc\x52\x01\x40\x13\xdc\x15\x80\x32\xc0\xdc\x0a\x01\x4d\x70\x53\xc8\x29\x08\x68\x82\xab\x82\x4c\x06\x98\x57\x05\xa0\x09\x3a\x85\x95\x0c\x30\xab\x2a\x40\x13\x9c\x8b\x20\xc5\x00\x4d\xf0\x53\xcc\xc8\x00\x33\xaa\x06\x34\xc1\xa9\x28\x51\x1c\xd0\x04\xff\x25\xfc\x52\x80\x26\x98\xf0\x33\xc0\x64\x44\xc0\xcb\x0b\xa6\x7c\x92\x80\x17\x17\x4c\xf2\xa4\x01\x2f\x2d\x98\xd6\x31\xc0\x68\x2c\x80\x17\x16\xcc\xc0\xc9\x01\xbc\xac\x60\x8e\x4d\x16\xe0\x45\x05\xb3\x68\xf2\x00\x2f\x29\x98\x27\x93\x09\x78\x41\xc1\x4c\x18\x03\x0c\xc5\x0c\x78\x39\xc1\x5c\x97\x6c\xc0\x8b\x09\x66\xb3\xe4\x03\x5e\x4a\x30\x5f\xa5\x00\xf0\x42\x82\x05\x28\x25\x80\x97\x11\x2c\x31\x29\x02\xbc\x88\x60\x11\x49\x19\xe0\x25\x04\xcb\x44\x0a\x01\x2f\x20\x58\x08\x52\x0a\x78\x7a\xc1\x52\x8f\x62\xc0\x93\x0b\x16\x73\x94\x03\x9e\x5a\xb0\x5c\xa3\x02\xf0\xc4\x82\x15\x18\x35\x80\xa7\x15\xac\xb1\xa8\x02\x3c\xa9\x60\x15\x45\x1d\xe0\x29\x05\xeb\x24\x2a\x01\xcf\x47\x58\xeb\x50\x0d\x78\x32\xc1\x6a\x86\x7a\xc0\x53\x09\xd6\x2b\x10\x00\x4f\x24\x48\x40\xa0\x00\x9e\x46\x90\x62\x40\x02\x3c\x07\x21\x4d\x80\x08\x78\x02\x41\x22\x00\x15\xf0\xf0\x82\xd4\xf9\xc9\x80\xc7\x26\xa4\x4f\xcf\x00\x78\x60\x41\x86\xe1\x39\x00\x0f\x2b\xc8\x31\x3b\x0b\xe0\x31\x09\x79\x26\x67\x02\x3c\xa0\x20\xd3\xe0\x5c\x80\x47\x23\x64\x1b\x9b\x0f\xf0\x48\x84\x8c\x43\x73\x02\x1e\x46\x90\x73\x66\x56\xc0\x63\x10\xf2\x4e\xcc\x0c\x78\x00\x41\xe6\x81\xb9\x01\xb5\x13\xb2\x8f\xcb\x0f\xa8\x99\xb0\xc1\xb0\x2d\x00\xb5\x12\x36\x19\xb5\x0d\xa0\x46\xc2\x46\x83\xb6\x02\xd4\x46\xd8\x6c\xcc\x76\x80\x9a\x08\x1b\x0e\xd9\x12\x50\x0b\x61\xd3\x11\xdb\x02\x6a\x20\x6c\x3c\x60\x6b\x40\x34\x61\xf3\xf1\xda\x03\x76\x38\x43\x89\xd9\x44\x00\x31\x84\x32\x93\x09\x01\x76\xd2\x86\x62\x63\xc9\x01\x76\x72\x86\x92\x33\x89\x02\x76\x12\x86\xc2\x03\x49\x03\x76\x6d\x0d\xe5\xa7\x01\x00\x8e\x9d\x03\x6f\x0c\x04\xd8\x71\x1b\xc2\xc6\xc0\x01\x4e\x1d\xda\x6e\x0a\x0c\x38\x75\x54\xbb\x29\x0d\x80\xef\x0e\x47\xf7\x4e\x0f\xe0\xb7\x83\xc0\x7d\xfb\x0f\x59\xc8\x30\x9d\xbf\x0f\x7a\x0a\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82\x46\x18"
]

chunked_img_packet = [
    b"\x03\x0b\xbb\x54\x54\x00\x01\x71\x00\x01\x00\x00\x0b\xb5\x00\x00\x00\x0d\x00\x00\x00\x00\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\x00\x01\x40\x00\x00\x01\x40\x08\x03\x00\x00\x00\xfa\x4e\x55\x98\x00\x00\x01\x17\x50\x4c\x54\x45\xd9\xd9\xd9\x00\x00\x00\x66\x66\x66\xff\xff\xff\xff\x66\xff\xcc\x51\xcc\xaa\xaa\xaa\x99\x99\x99\x33\x33\x33\x00\x00\x00\xe0\xe0\xe0\xcc\xcc\xcc\xde\xde\xde\xf0\xf0\xf0\xff\xff\xff\xfb\xfb\xfb\xf7\xf7\xf7\xa6\xa6\xa6\x99\x3d\x99\x8c\x8c\x8c\xe9\xe9\xe9\x73\x73\x73\xe0\x59\xe1\xf4\xf4\xf5\xf2\xf2\xf3\xe4\xe4\xe5\x70\x70\x71\xfa\xfa\xfb\xd4\xd4\xd5\xc1\xc1\xc2\xe1\xe1\xe2\xa3\x72\x27\xb3\xcb\x35\x00\x6c\x87\xeb\xeb\xec\x80\x39\x08\x00\x5b\x89\x2d\x63\xa7\xb7\x49\xb8\x00\x8a\x90\xbc\x84\x2d\x00\x80\x99\x00\x9c\xa2\x23\x4d\x80\xa4\x00\x00\xa5\x00\x00\xc0\xd8\xe8\xd8\xe4\xf0\xb0\xc8\x80\x03\x60\x33\xb2\x83\x00\xff\x00\xcc\x00\x99\xb8\x46\x99\xff\x3d\x85\x06\x00\xb7\xbd\x98\xc0\xd8\xcc\x5a\x0c\xfb\xb0\x3b\x7a\x5b\xb8\x88\x66\xcc\xa8\xcc\xe0\x48\x62\x81\xc9\x98\x00\x00\xaa\xcc\xce\x00\x00\x52\xb1\x07\xaa\x80\xff\xd8\xa7\x00\x7e\x58\x1e\x00\xba\xe1\x3b\x82\xd9\x00\x5d\x63\x06\xb6\x63\xd5\x95\x33\xff\x00\x99\x67\x00\x00\xe7\xb6\x00\xff\x71\x10\x34\x73\xc0\x95\x70\xe1\x5a\x7b\xa2\xff\x30\x07\x26\xa7\xdf\x2d\x3e\x51\x00\x78\x7f\xff\xcc\x00\x66\x4c\x99\x00\xd4\xff\xff\xcc\x00\x00\xdc\xff\x00\xcc\xff\x00\xe7\xff\xb9\xb9\x2f\xbf\x00\x00\x0a\x51\x49\x44\x41\x54\x78\x9c\xed\xdd\x4b\x92\xab\x3a\x0c\x06\xe0\x9e\x66\x72\x2a\x2b\x21\xa3\x54\x65\x42\x55\xf6\xc0\xfe\xf7\x72\x9a\xa4\x01\x83\x1f\xd8\x96\xa5\x5f\x80\xfe\xd9\xed\x9c\x5c\xa4\xaf\x0c\xe6\x9d\x9f\x9b\xb6\xbc\x93\x41\x57\xe7\xe5\x07\x5d\xc0\x9c\x34\x9c\x5a\x48\x0d\x80\x65\x74\xca\x18\xc1\x80\xf5\x76\x5a\x14\x71\x80\x2d\xec\x14\x28\x82\x00\xdb\xea\x21\x0d\x01\x80\x1c\x78\x38\x44\x69\x40\x4e\x3d\x88\xa1\x28\x20\xbf\x9e\xbc\xa1\x1c\xa0\x94\x9e\xb0\xa1\x10\xa0\xac\x9e\xa4\xa1\x08\x20\x82\x4f\x8a\x90\x1f\x10\xa5\x27\x64\xc8\x0d\x88\xe5\x13\x20\xe4\x05\x44\xe3\x7d\xc3\xda\x22\x27\x20\x1a\x6e\x09\x63\x93\x7c\x80\x68\xb4\x75\xd8\xda\xe4\x02\x44\x83\xf9\x61\x6a\x94\x07\x10\x8d\x15\x0e\x4b\xab\x1c\x80\x68\xa8\x78\x18\x9a\x6d\x0f\x88\x46\x4a\xa7\x79\xbb\xad\x01\xd1\x40\xfb\x69\xdc\x70\x63\x40\xb4\x4e\x4e\xda\x76\xdc\x14\x10\x4d\x93\x9b\x96\x3d\xb7\x04\x44\xbb\xe4\xa7\x61\xd3\xed\x00\xd1\x28\x65\x69\xd6\x76\x2b\x40\x34\x48\x79\x1a\x35\xde\x08\x10\xad\x51\x93\x36\x9d\x37\x01\x44\x53\xd4\xa6\x45\xef\x2d\x00\xd1\x0e\xf5\x69\xd0\x7c\x03\x40\xb4\x02\x25\x0a\x00\xd1\x04\xd4\xa0\x01\xd1\xfd\xd3\x83\x05\x44\x77\xdf\x22\x40\x40\x74\xeb\xad\x82\x02\x44\xf7\xdd\x2e\x18\x40\x74\xd7\x2d\x83\x00\x44\xf7\xdc\x36\xf2\x80\xe8\x8e\x5b\x47\x18\x10\xdd\x2e\x47\x24\x01\xd1\xbd\xf2\x44\x0e\x10\xdd\x29\x57\xa4\x00\xd1\x7d\xf2\x45\x06\x10\xdd\x25\x67\x24\x00\xd1\x3d\xf2\x86\x1f\x10\xdd\x21\x77\xb8\x01\xd1\xfd\xf1\x87\x17\x10\xdd\x9d\x44\x38\x01\xd1\xbd\xc9\x84\x0f\x10\xdd\x99\x54\xb8\x00\xd1\x7d\xc9\x85\x07\x10\xdd\x95\x64\x38\x00\xd1\x3d\xc9\xa6\x3d\x20\xba\x23\xe9\xb4\x06\x44\xf7\x23\x1f\x03\x24\xa6\x2d\x20\xba\x1b\x44\x5a\x02\xa2\x7b\xc1\xa4\x1d\x20\xba\x13\x54\x5a\x01\xa2\xfb\xc0\xa5\x0d\x20\xba\x0b\x64\x0c\x90\x98\x16\x80\xe8\x1e\xb0\xa1\x03\xa2\x3b\x40\x87\x0a\x88\xae\x1f\x1f\x03\x24\x86\x06\x88\xae\x5e\x43\x28\x80\xe8\xda\x75\xa4\x1e\x10\x5d\xb9\x96\x18\x20\x31\xb5\x80\xe8\xba\xf5\xa4\x0e\x10\x5d\xb5\xa6\x18\x20\x31\x35\x80\xe8\x9a\x75\xc5\x00\x89\x29\x07\x44\x57\xac\x2d\xa5\x80\xe8\x7a\xf5\xc5\x00\x89\x29\x03\x44\x57\xab\x31\x25\x80\xe8\x5a\x75\xc6\x00\x89\xc9\x07\x44\x57\xaa\x35\x06\x48\x4c\x2e\x20\xba\x4e\xbd\x31\x40\x62\xf2\x00\xd1\x55\x4e\x79\xf6\xdd\xbf\x4f\xba\xfe\x89\xae\x65\xca\x81\x00\x5f\x8f\x7f\x4e\x1e\x2f\x74\x3d\xdf\xe4\x00\xa2\x6b\xfc\xe4\x79\xff\xb7\xc9\x5d\xc7\x28\x3c\x08\x60\xbf\xe5\x1b\xd3\xa3\xab\x1a\xb3\x0f\x88\xae\x70\xcc\x23\xe4\xf7\xbb\x1e\xa3\xeb\x1a\x73\x04\xc0\x88\x9f\x0e\xc1\x3d\x40\x74\x7d\xbf\xe9\x62\x7e\xbf\xf3\x31\xba\xb6\xb7\x27\xa8\x0f\xf0\x15\xf7\xfb\xf7\x4f\xc1\x64\x9c\x06\x44\x57\xf7\x7e\x0f\xab",
    b"\xf9\xf7\xde\x75\xeb\xff\x1e\xd0\xf5\x6d\x05\xd5\x01\xba\x13\x70\xff\xe1\x1a\x56\x7f\x42\xd7\x97\x06\x44\xd7\xf6\x1b\x67\xca\x98\x47\xdb\xe0\x4c\x2b\xc8\xda\xfe\x02\x03\x1c\x32\xb2\x8c\xb6\xd5\x94\xbb\x08\xf6\x39\xff\x17\xde\x3e\xe2\x80\xbc\xcb\x4d\x4f\x0f\xdb\xdc\xd7\xdf\xf5\x8e\x4c\x52\xe1\x9e\x6a\x50\x80\x43\x09\xc2\xe6\xc8\xed\x59\xf2\x5d\xee\x99\xe6\x08\x80\xf7\xed\x97\x4b\x86\x20\x0a\x90\x79\xb1\x89\x43\x0c\x3f\xde\x2e\x73\x97\xff\x5d\xfe\x03\x16\x14\x60\xc1\x7a\xe8\x6d\xc6\x0a\x36\xa0\xfc\xe7\x6d\xc2\x80\xec\x8b\x2d\x19\x82\x04\x40\x89\x23\x66\x14\x60\xfe\x56\xd0\xdb\x61\x0e\x9e\xe1\x0a\x46\xe2\x60\x05\x05\x98\xbf\x12\x7b\xc3\x28\x7b\xf0\x8a\x9c\x78\x0d\x01\x4a\x2c\x37\x74\xaa\x39\x6f\x1c\xe5\x8e\x5d\xa9\x13\xd7\x30\xc0\xf5\x91\x6d\x22\x9b\x69\xb8\xcb\xfb\x56\x2f\x75\xb2\x01\x07\xf8\x4b\xf8\xea\xbb\x68\x96\x35\x75\x35\x94\x96\x55\xff\x11\xff\x6e\xff\x92\x3b\x57\xe3\x03\x8a\x2d\x3a\x1d\x67\x23\xf9\xdc\xfb\x2b\x34\x5a\x01\xdd\xc9\x62\x9e\x89\x9d\xb5\x5e\xc3\x59\xfd\x4f\xd4\x02\xba\xf3\xf4\xbd\x7f\x0e\xc3\xb3\x77\xe7\x1d\x2d\x03\xd0\x03\x44\xd7\xb3\x24\xb9\xbf\xa2\x66\x00\xce\x82\xfa\x00\x87\xc4\x8e\x8e\x86\x33\xfa\x53\xd4\x02\xa6\x76\xb6\xd5\xac\xc0\xef\x2d\x20\xba\x9a\x55\xa2\x82\x9a\xfc\x26\x41\x8d\x80\x31\x41\x5d\x7e\x9a\x01\x57\x57\x91\xe6\xf9\x43\xd1\xf6\xef\x13\xcd\x80\xef\xf7\x6b\x33\x95\xdc\x15\x5c\x52\xdf\xc4\x05\x44\xd7\x12\x8a\x7b\x83\xa0\x96\xdb\x03\xd7\xd1\x02\x38\x3c\x5f\x7f\xf1\x3f\x18\x0f\x71\x5f\xcf\xed\xca\x3b\xfd\x7b\xef\x03\xd9\xe8\x00\x74\xd7\xd5\xcc\x7b\x87\x3a\x25\x6b\xf6\x02\x88\xab\x61\x73\x7a\x30\xeb\xc6\x8d\xf5\xf9\x30\xe4\x9d\xab\x78\x40\xef\xdc\x60\x86\x60\xcd\x77\x98\x02\x07\x0c\x5c\x28\xda\x3d\xd8\x0d\xec\xe0\xc0\x56\x63\x34\x60\xf0\x34\x7d\xfa\x70\x37\x7c\xa0\x8c\x9a\x4b\xd0\x80\x5d\x08\x23\xb9\x4a\x46\x2e\x07\xa0\x6e\x5c\x9d\x00\x41\x8b\x8f\x5e\x27\x8a\x4d\xad\xdb\x9d\x6b\x15\x43\x10\x08\x98\xb8\xba\x74\xf7\x2f\x0e\x0d\x7d\xe2\x34\x17\x6a\x1e\xc1\x02\x76\x71\x90\xdf\x3c\xfa\x65\x37\x79\x78\xf6\xe9\xcb\xc2\xc0\x75\x18\x08\x98\x71\x85\xf8\xb1\xbe\x50\x17\x8d\x77\x2f\x97\x50\xb0\x80\xfb\x2e\xf9\x01\xb5\xf0\x05\x04\x2d\xfc\x0c\x80\x6f\x03\x24\xc6\x00\x89\xd1\x03\xd8\x3d\xc7\xc9\x36\xeb\x16\xac\xc7\x38\x3d\x3f\x3b\x03\x74\x01\xa6\x5d\xe7\x8c\x3b\x8f\xa6\x7d\xbe\xd5\x81\x34\xaa\x07\x2d\x80\xcb\xa1\xc7\x7a\x60\x05\xb2\xec\xf2\xb9\x82\x88\xfa\xc7\x8c\x80\xa8\x65\xbb\xcf\x24\x2d\x7f\xdc\xbd\x0f\xd0\x39\x44\xd1\xf0\xfc\x92\x0e\x40\xf7\xd8\x77\x67\x08\xba\xc7\x1c\xce\x10\x94\xae\x7d\x8e\x0e\x40\xf7\xc0\x77\xe7\x66\x72\xd7\xda\x19\xad\xd2\xb5\xcf\x31\x40\x62\x74\x00\xba\x97\x35\x76\xe6\x61\xf7\xbc\x8b\x73\x03\x83\x74\xed\x73\x74\x00\xba\x1b\xb6\x9d\x5d\x41\xf7\x94\x7f\x67\x80\x53\x96\x75\x78\xf7\x79\x9a\x65\x1d\x76\x27\x6c\x44\xfd\x9f\x28\x01\x9c\x2f\x84\x64\x3c\x47\x32\xfd\xd3\xd5\xe5\x11\x54\x0f\xbf\x80\xb0\x45\xaf\x8e\x44\xfe\xae\xee\x66\x3d\xcf\xf5\x1d\x83\xeb\x2b\xca\xb8\x2e\x7e\x70\x8b\x5e\xb3\xdc\xbb\xae\xcb\xe1\x1b\xd3\x6d\x5e\x45\x61\x80\xe4\xe0\xba\xf8\xc1\x2d\xda\x00\x89\x31\x40\x62\x0c\x90\x18\x03\x24\xc6\x00\x89\x31\x40\x62\x0c\x90\x18\x03\x24\xc6\x00\x89\x31\x40\x62\x0c\x90\x18\x03\x24\xc6\x00\x89\x31\x40\x62\x0c\x90\x18\x03\x24\xc6\x00\x89\x31\x40\x62\x0c\x90\x18\x03\x24\xc6\x00\x89\xd9\x67\x79\x74\xe3\x73\xe9\x39\x0f\x8a\xe0\xba\xf8\xc1\x2d\x7a\xc7\xc4\xfd\x25\xaa\xe7\xde\xad\xbf\xb8\x2e\x7e\x70\x8b\x4e\x81\xf8\xcf\x1b\xc6\x9f\x34\x34\x40\x3f\xc1\x67\xdf\x3a\x03\x5c\x27\x3e\xfc\x22\xaf\x41\x48\xbc\x7f\x55\xb6\x72\x37\x3f\xb8\x45\x47\xfd\xa2\x4f\xff\xc6\x5f\xec\x26\x59\xf7\x3a\x3a\x6e\x6f\xcb\xf3\x4b\x08\xca\x55\xbd\x89\x92\xfb\x03\x33\xfd\xe2\x82\x52\x35\x7b\xd1\x07\xb8\xf3\x0a\x8e\xc8\x1d\x84\x32\x15\x07\xa2\x0e\x70\xf7\xd9\xf3\xce\x00\xa7\x04\x25\xb6\x2b\xb0\xf7\xf3\x3e\xe1\x47\x99\xa4\x6a\xf6\xa2\x0d\x70\xf5\xf6\x88\xe1\xfb\xa6\x84\xc7\xfa\x0d\x14\xc1\x83\x12\xd9\xca\x9d\x68\x03\x74\xa8\x06\x67\x65\xed\xdc\xbf\x1b\xe0\x5f\x02\x0e\xee\x53\x87\xd1\x1f\xe4\x0b\x9d\x5b\x90\xaf\xfe\x2f\x4a\x1e\x77\x9d\xe2\x3c\x04\xb2\x7d\x83\x65\xfa\x51\x12\x44\xfd",
    b"\x63\xb4\x3c\x2f\x3c\x65\x51\xf2\x7f\xa0\x79\xfe\x28\xb4\x0e\x23\xea\x1f\xa3\x0d\x70\xfe\x2c\x30\x53\xf4\x59\x5f\x14\x8e\x32\xc0\x79\x13\x18\x9c\x28\xe6\xe1\x19\xd8\x08\x62\x3a\x50\x07\x38\xef\x45\x07\x8f\x37\xe6\x0d\x64\x67\x80\x9f\x24\x00\x03\x44\xe9\x4f\x37\xff\x6b\x99\xdf\xd8\x7c\xff\x01\xea\x79\xf5\xd3\x4c\x14\xbc\x0a\x32\xaf\xe0\x7b\x80\xcb\x6b\x81\xb9\x5f\xf3\xab\xed\xdd\x59\x5d\xfc\x23\x57\x29\x0d\xb8\xf0\xf1\x13\x9e\x11\x70\x78\x6d\xc2\x29\x78\x42\x40\xcf\x8f\x55\xf0\x84\x80\x4f\x1f\x90\xf1\x45\xd3\xd8\x97\xd0\x72\x00\x06\x06\x20\xe3\x10\x04\xbf\xc5\x97\x03\x30\xe4\xe7\xbd\xa3\xbf\x59\xce\x07\x18\x1c\x80\x7c\x43\xf0\x7c\x80\x81\x2d\x20\xe7\x56\xf0\x7c\x80\x61\x3f\xb6\x75\x18\xfc\x73\x18\x87\x07\x44\xff\x9e\x88\x7f\x89\xb7\x1a\x70\x3a\x59\x78\x2d\x40\xdf\xa1\x1a\x70\xfa\x22\x0c\x10\x22\xe8\x9f\x34\xad\x06\x9c\x5f\x0b\x2a\x09\x08\xff\x55\x2f\xff\xac\x69\x35\xe0\xfc\x3a\xa8\xb0\x1f\xcf\x6e\x0c\x1c\xd0\x87\xa8\x05\x9c\xbf\x77\x31\x40\x6f\x08\xd6\x02\x2e\x40\xc1\x1d\x41\xa6\xdd\xc0\x15\x20\x46\x70\x7b\xe6\xbe\x12\xd0\xd9\xc4\x09\x1e\x0b\xdf\x14\x00\x6e\xe7\x91\x3a\xc0\xd5\xed\x20\x72\x67\x63\x54\x00\x6e\x6e\x1d\xaf\x01\xdc\xdc\x8e\x3e\x78\x82\x5c\xe7\xa4\x37\x80\xb0\xdf\x05\xea\x43\x3f\xcc\x97\x0d\xe8\xff\xf4\xcd\x56\x90\xd9\x0f\x0e\xf8\x76\xb7\x5b\xf3\xca\x96\x06\x5c\x88\x82\x38\xab\xed\x20\xeb\xb9\x40\x25\x80\x81\xa4\x01\xf7\x32\xcc\x84\x8c\x17\x36\x3d\x40\x55\x82\x34\xc0\xf7\x74\x61\x98\xad\xbe\xc5\xef\xac\x80\xec\x31\x40\x62\x02\x80\x9a\x04\xd5\x03\xde\x0c\x90\x16\x03\x24\x26\x08\xa8\x48\x50\x3b\xe0\xcd\x00\x69\x89\x00\xea\x11\x54\x0e\x78\x33\x40\x5a\x0c\x90\x98\x28\xa0\x1a\x41\xdd\x80\x37\xfd\x80\xe9\x5b\x7c\xd1\x49\x00\x6a\x11\xec\x42\x80\xbb\x4f\xc2\x0a\xe5\x76\x00\xc0\xf4\x63\x0e\xe0\x24\x01\x95\x08\xa6\x1f\xb4\xc1\xe6\x76\x04\xc0\xf4\xa3\x5e\xd8\xec\x00\x6a\x11\x4c\x3c\x6c\x88\xcd\xd6\x4b\x2b\x60\xe2\x71\x57\x6c\x76\x01\x75\x0a\xaa\xf5\xd3\x0b\xb8\xda\x97\xd1\xb2\x07\x93\x05\xa8\x47\x30\xfc\xd2\x09\x68\x7c\x2d\xcd\x80\x0a\x93\x05\x68\x82\xd1\x04\xb0\x0c\xb0\x24\x99\x80\x26\x18\x49\xc8\xca\x00\x0b\x92\x0d\x68\x82\xc1\x04\xa9\x0c\x30\x3f\x05\x80\x26\x18\x48\x58\x2a\x02\x68\x82\x5e\x22\x50\x06\x98\x9b\x42\x40\x13\xdc\x24\xe6\x14\x05\x34\xc1\x55\xa2\x4c\x06\x98\x97\x0a\x40\x13\x74\x12\x57\x32\xc0\xac\x54\x01\x9a\xe0\x9c\x04\x52\x0a\xd0\x04\xff\x92\x32\x32\xc0\x8c\x54\x03\x9a\xe0\x27\x49\xa2\x34\xa0\x09\xbe\x77\xfc\xf6\x00\x4d\x70\xc7\xcf\x00\x77\x43\x04\xbc\xbc\xe0\x9e\xcf\x2e\xe0\xc5\x05\x77\x79\xf6\x01\x2f\x2d\xb8\xaf\x63\x80\xc9\x34\x01\xbc\xb0\x60\x06\x4e\x0e\xe0\x65\x05\x73\x6c\xb2\x00\x2f\x2a\x98\x45\x93\x07\x78\x49\xc1\x3c\x99\x4c\xc0\x0b\x0a\x66\xc2\x18\x60\x2c\x8d\x01\x2f\x27\x98\xeb\x92\x0d\x78\x31\xc1\x6c\x96\x7c\xc0\x4b\x09\xe6\xab\x14\x00\x5e\x48\xb0\x00\xa5\x04\xf0\x32\x82\x25\x26\x45\x80\x17\x11\x2c\x22\x29\x03\xbc\x84\x60\x99\x48\x21\xe0\x05\x04\x0b\x41\x4a\x01\x4f\x2f\x58\xea\x51\x0c\x78\x72\xc1\x62\x8e\x72\xc0\x53\x0b\x96\x6b\x54\x00\x9e\x58\xb0\x02\xa3\x06\xf0\xb4\x82\x35\x16\x55\x80\x27\x15\xac\xa2\xa8\x03\x3c\xa5\x60\x9d\x44\x25\xe0\xf9\x08\x6b\x1d\xaa\x01\x4f\x26\x58\xcd\x50\x0f\x78\x2a\xc1\x7a\x05\x02\xe0\x89\x04\x09\x08\x14\xc0\xd3\x08\x52\x0c\x48\x80\xe7\x20\xa4\x09\x10\x01\x4f\x20\x48\x04\xa0\x02\x1e\x5e\x90\xda\x3f\x19\xf0\xd8\x84\xf4\xee\x1b\x00\x1e\x58\xb0\x41\xf3\x2d\x00\x0f\x2b\xd8\xa2\xf7\x26\x80\xc7\x24\x6c\xd3\x79\x23\xc0\x03\x0a\x36\x6a\xbc\x15\xe0\xd1\x08\x9b\xb5\xdd\x0e\xf0\x48\x84\x0d\x9b\x6e\x09\x78\x18\xc1\x96\x3d\x37\x05\x3c\x06\x61\xdb\x8e\x1b\x03\x1e\x40\xb0\x71\xc3\xad\x01\xb5\x13\x36\x6f\xb7\x3d\xa0\x66\x42\x86\x66\x39\x00\xb5\x12\xb2\xb4\xca\x03\xa8\x91\x90\xa9\x51\x2e\x40\x6d\x84\x6c\x6d\xf2\x01\x6a\x22\x64\x6c\x92\x13\x50\x0b\x21\x6b\x8b\xbc\x80\x1a\x08\x99\x1b\xe4\x06\x44\x13\xb2\xb7\xc7\x0f\x78\xc3\x19\x4a\xf4\x26\x02\x88\x21\x94\xe9\x4c\x08\xf0\x26\x6d\x28\xd6\x96\x1c\xe0\x4d\xce\x50\xb2\x27\x51\xc0\x9b\x84\xa1\x70\x43\xd2\x80\x37\x5e\x43\xf9\x6e\x00\x80\x63\xce\x81\x37\x06\x04\x78\x6b\x6d\x08\x6b\x03\x07\xf8\xc9\xa1\xed\x3e\x01",
    b"\x03\x7e\x72\x54\xbb\x4f\x34\x00\x7e\x73\x38\xba\x6f\xf4\x00\x4e\x39\x08\xdc\x94\xff\x1f\xff\x3b\x53\x28\x82\x83\x99\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82",
    b"\x65\x8a"
]


@pytest.fixture(params=[img_packet, chunked_img_packet])
def img_packet(request):
    return request.param


def test_ac():
    payload = b"\x00\x00\x04\x54\x54\x00\x00\xac\x00\x01\x00\x01\x00\x02"
    p = TTPacket.parse(payload)
    assert p.bytes_to_read == 0
    assert p.is_valid()
    assert p.type == TYPE_INIT
    assert p.header == b"\x00\x00\xac"
    assert p.payload_length == 4


def test_img(img_packet):
    p = TTPacket.parse(img_packet[0])
    for pt in img_packet[1:]:
        assert p.bytes_to_read > 0
        p.hydrate(pt)

    assert p.bytes_to_read == 0, p.bytes_to_read
    assert p.type == TYPE_FRAMES, p.type
    assert p.is_valid(), '%d vs %d' % (p.calculate_checksum(), p.checksum)
    assert p.header == b"\x00"+i2b(calculate_header(len(p.payload) - 14))


def test_ttframes():
    payload = b"\x00\x0b\x00\x00\x00\x00\x00\x00\x33\x00\x1b\x00\x12"
    p = TTPacket(calculate_header())