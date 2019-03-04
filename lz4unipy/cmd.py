import pathlib
import argparse
import traceback
from . import handler


prefix = "[lz4unipy]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", nargs="+", help="ファイルを指定します（複数可）。")
    parser.add_argument("--dir", required=False, default=False, help="結果の出力先ディレクトリを指定します。")
    args = parser.parse_args()
    current_dir = pathlib.Path().parent
    if args.dir:
        save_dir = pathlib.Path(args.dir)
        if not save_dir.is_dir():
            i = input(f"{prefix} 指定されたディレクトリが見つかりませんでした。カレントディレクトリ({current_dir.absolute()})を出力先ディレクトリとして使用します。よろしいですか？[Y/n]: ")
            while True:
                if "y" in i.lower():
                    save_dir = current_dir
                    break
                elif "n" in i.lower():
                    print(f"{prefix} 処理を中断します。")
                    exit()
                else:
                    i = input(f"{prefix} Y/nで入力してください。")
                    continue
    else:
        save_dir = current_dir
    print(f"{prefix} 出力先フォルダ: {save_dir.absolute()}")

    for filename in args.infile:
        file = pathlib.Path(filename)
        if file.is_file():
            print(f"{prefix} ファイル、 {file.absolute()} の処理を開始します。")
            with open(file, "rb") as f:
                binary = f.read()
                if handler.is_compressed(binary):
                    print(f"{prefix} このファイルはunitylz4形式で圧縮されています。展開を試みます。")
                    if file.suffix == ".lz4":
                        output = save_dir / file.stem
                    else:
                        output = save_dir / (file.name + ".dat")
                    while True:
                        if output.is_file():
                            output = save_dir / (output.name + ".dat")
                            continue
                        else:
                            break
                    print(f"{prefix} 出力先: {output.absolute()}")
                    try:
                        dec = handler.decompress(binary)
                        with open(output, "wb") as w:
                            w.write(dec)
                        print(f"{prefix} 展開に成功しました。")
                    except Exception as _:
                        print(f"{prefix} 展開に失敗しました。")
                        traceback.print_exc()
                else:
                    print(f"{prefix} このファイルは圧縮されていません。圧縮を試みます。")
                    output = save_dir / (file.name + ".lz4")
                    while True:
                        if output.is_file():
                            output = save_dir / (output.name + ".lz4")
                            continue
                        else:
                            break
                    print(f"{prefix} 出力先: {output.absolute()}")
                    try:
                        com = handler.compress(binary)
                        with open(output, "wb") as w:
                            w.write(com)
                        print(f"{prefix} 圧縮に成功しました。")
                    except Exception as _:
                        print(f"{prefix} 圧縮に失敗しました。")
                        traceback.print_exc()
