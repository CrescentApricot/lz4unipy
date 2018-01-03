# lz4unipy
unity3d compatible lz4 pack/unpack library in Python3.

## About

lz4unipyはPython3で動作するunity3d互換の圧縮/展開ライブラリです。<br>
unity3d互換のlz4ファイルを作ったり圧縮するための関数や簡単なコマンドラインツールを内包しています。<br>

## Install

```bash
pip3 install git+ssh://git@github.com/Cryptomelone/lz4unipy.git
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
