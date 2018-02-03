# lz4unipy
unity3d compatible lz4 pack/unpack library in Python3.

## About

lz4unipy is unity3d compatible lz4 pack/unpack library working on Python3.<br>
It contains functions and simple command line tools for make/pack unity3d compatibled lz4 file.  

## Install

```bash
pip3 install lz4unipy
```

## Usage

### command line

```bash
lz4unipy [pack|unpack] target_file [target dir]
```

### import

```python
import lz4unipy

with open("target_file.unity3d.lz4", "rb") as f:
    data = f.read()
    if lz4unipy.is_compressed(data):
        with open("target_file.unity3d", "wb") as w:
            w.write(lz4unipy.decompress(data))
            
with open("target_file.unity3d", "rb") as f:
    data = f.read()
    if not lz4unipy.is_compressed(data):
        with open("target_file.unity3d.lz4", "wb") as w:
            w.write(lz4unipy.compress(data))
```

## Test

```bash
git clone git@github.com/Cryptomelone/lz4unipy.git
cd lz4unipy
pip3 install -r requirements.txt
python3 setup.py test
```

### Notice
テスト用ファイル [sample.png](/tests/sample.png) にはバンダイナムコエンターテインメント株式会社の提供するスマートフォン向けリズムゲーム、[アイドルマスターミリオンライブ！ シアターデイズ](https://millionlive.idolmaster.jp/theaterdays/)のゲーム内スクリーンショットを利用しています。この場を借りてお礼申し上げます。
