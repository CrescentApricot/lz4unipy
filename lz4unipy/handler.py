# -*- coding: utf-8 -*-

import lz4.block
from io import BytesIO
from struct import pack, unpack


def compress(data: bytes) -> bytes:
    buf = lz4.block.compress(data, mode="high_compression")[4:]
    with BytesIO() as bio:
        bio.write(b'd\x00\x00\x00')
        bio.write(pack('i', len(data)))
        bio.write(pack('i', len(buf)))
        bio.write(b'\x01\x00\x00\x00')
        bio.write(buf)
        return bio.getvalue()


def decompress(data: bytes) -> bytes:
    return lz4.block.decompress(data[16:], uncompressed_size=unpack("i", data[4:8])[0])


def is_compressed(data: bytes) -> bool:
    if 4 <= len(data):
        if unpack("i", data[:4])[0] is 100:
            return True
    return False
