# -*- coding: utf-8 -*-

import lz4
from io import BytesIO
from struct import pack, unpack


def compress(data: bytes) -> bytes:
    buf = lz4.block.compress(data, mode="high_compression")[4:]
    with BytesIO() as bio:
        bio.write(pack('i', 100))
        bio.write(pack('i', len(data)))
        bio.write(pack('i', len(buf)))
        bio.write(pack('i', 1))
        bio.write(buf)
        return bio.getvalue()


def decompress(data: bytes) -> bytes:
    with BytesIO() as bio:
        bio.write(data[4:8])
        bio.write(data[16:])
        stream = bio.getvalue()
    return lz4.block.decompress(stream)


def is_compressed(data: bytes) -> bool:
    if 4 <= len(data):
        if unpack("i", data[:4])[0] is 100:
            return True
    return False
