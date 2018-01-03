import sys
import os
from . import handler


def main():
    if len(sys.argv) <= 2:
        message("ファイルを指定して下さい。\nUsage: lz4unipy [pack|unpack] target_file [target dir]")
    elif 3 <= len(sys.argv) <= 4:
        if len(sys.argv) is 4:
            if not os.path.exists(sys.argv[3]):
                message(f"出力対象ディレクトリが存在しませんでした: {sys.argv[2]}")
                return False
            save_dir = sys.argv[3]
            message(f"出力対象ディレクトリ: {save_dir}")
        else:
            message("出力対象ディレクトリが指定されませんでした。カレントディレクトリに出力します。")
            save_dir = ""

        file_path = sys.argv[2]

        if not os.path.exists(file_path):
            message(f"入力ファイルが存在しませんでした: {file_path}")
            return False

        spl = file_path.split(".")

        set_mode = sys.argv[1]
        if set_mode == "pack":  # pack
            message("圧縮を開始します。")
            export_path = file_path + ".lz4"

            with open(file_path, "rb") as f:
                data = f.read()
                if handler.is_compressed(data):
                    message("このファイルは既にunity3d互換のlz4で圧縮されている可能性があります。圧縮を中止します。")
                    return False
                else:
                    if os.path.exists(os.path.join(save_dir, export_path)):
                        message(f"出力予定のファイルと同名のファイルが既に存在しています: {export_path}\n展開を中止します。")
                        return False
                    with open(os.path.join(save_dir, export_path), "wb") as w:
                        w.write(handler.compress(data))
                    message(f"圧縮を完了しました: {export_path}")
        elif set_mode == "unpack":  # unpack
            message("展開を開始します。")
            if len(spl) is 1:
                export_path = file_path + ".dat"
            else:
                if spl[-1] == "lz4":
                    export_path = file_path[:-4]
                else:
                    export_path = file_path + ".dat"

            with open(file_path, "rb") as f:
                data = f.read()
                if handler.is_compressed(data):
                    if os.path.exists(os.path.join(save_dir, export_path)):
                        message(f"出力予定のファイルと同名のファイルが既に存在しています: {export_path}\n展開を中止します。")
                        return False
                    with open(os.path.join(save_dir, export_path), "wb") as w:
                        w.write(handler.decompress(data))
                    message(f"展開を完了しました: {export_path}")
                else:
                    message("このファイルはunity3d互換のlz4で圧縮されていない可能性があります。展開を中止します。")
                    return False
        else:
            message("モード指定が誤っています。packまたはunpackで指定して下さい。")
            return False


def message(msg: str):
    print(f"[lz4unipy] {msg}")
