# lz4unipy

## 概要

`lz4unipy` は `unity-lz4` 互換の展開/圧縮を行うコマンドラインツールと簡易なライブラリです。

## インストール

```bash
pip3 install lz4unipy
```

## 使い方

### コマンドライン

```bash
lz4unipy [-h] [--dir DIR] infile [infile ...]
```

指定したファイルより自動的に動作モードを、パスより自動的に出力ファイル名を決定します。

### ライブラリ

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

## テスト

```bash
git clone git@github.com/CrescentApricot/lz4unipy.git
cd lz4unipy
python3 setup.py test
```

### 謝辞
テスト用ファイル [sample.png](/tests/sample.png) にはバンダイナムコエンターテインメント株式会社の提供するスマートフォン向けリズムゲーム、[アイドルマスターミリオンライブ！ シアターデイズ](https://millionlive.idolmaster.jp/theaterdays/)のゲーム内スクリーンショットを利用しています。この場を借りてお礼申し上げます。
