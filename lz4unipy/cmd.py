import sys
import os
from . import handler


def main():
    if len(sys.argv) <= 2:
        __message("Please specify file.\nUsage: lz4unipy [pack|unpack] target_file [target dir]")
    elif 3 <= len(sys.argv) <= 4:
        if len(sys.argv) is 4:
            if not os.path.exists(sys.argv[3]):
                __message(f"Target directory did not exist: {sys.argv[2]}")
                return False
            save_dir = sys.argv[3]
            __message(f"Target directory:: {save_dir}")
        else:
            __message("Target directory does not specified. Output to current directory.")
            save_dir = ""

        file_path = sys.argv[2]

        if not os.path.exists(file_path):
            __message(f"入力ファイルが存在しませんでした: {file_path}")
            return False

        spl = file_path.split(".")

        set_mode = sys.argv[1]
        if set_mode == "pack":  # pack
            __message("Starting pack.")
            export_path = file_path + ".lz4"

            with open(file_path, "rb") as f:
                data = f.read()
                if handler.is_compressed(data):
                    __message("This file is already may be compressed with unity3d compatible lz4. pack aborted.")
                    return False
                else:
                    if os.path.exists(os.path.join(save_dir, export_path)):
                        __message(f"A file with the same name as the file scheduled to be output already exists: {export_path}\npack aborted.")
                        return False
                    with open(os.path.join(save_dir, export_path), "wb") as w:
                        w.write(handler.compress(data))
                    __message(f"Pack completed: {export_path}")
        elif set_mode == "unpack":  # unpack
            __message("Staring unpack.")
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
                        __message(f"A file with the same name as the file scheduled to be output already exists: {export_path}\nunpack aborted.")
                        return False
                    with open(os.path.join(save_dir, export_path), "wb") as w:
                        w.write(handler.decompress(data))
                    __message(f"Unpack completed: {export_path}")
                else:
                    __message("This file is not may be compressed with unity3d compatible lz4. unpack aborted.")
                    return False
        else:
            __message("Specified mode was invalid. please spec `pack` or `unpack`.")
            return False


def __message(msg: str):
    print(f"[lz4unipy] {msg}")
