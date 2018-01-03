import unittest
import os
import lz4unipy


class TextSample(unittest.TestCase):
    def setUp(self):
        self.abspath = os.path.dirname(os.path.abspath(__file__))

    def test_pack(self):
        with open(os.path.join(self.abspath, "sample.png"), "rb") as f:
            data = f.read()
            with open(os.path.join(self.abspath, "sample.png.lz4"), "wb") as w:
                w.write(lz4unipy.compress(data))
            print("sample.pngの圧縮に成功しました。")

    def test_unpack(self):
        with open(os.path.join(self.abspath, "sample.png.lz4"), "rb") as f:
            data = f.read()
            with open(os.path.join(self.abspath, "sample.png"), "wb") as w:
                w.write(lz4unipy.decompress(data))
            print("sample.png.lz4の展開に成功しました。")
