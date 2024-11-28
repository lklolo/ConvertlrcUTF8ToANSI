import os

lrc_files = []
lose_files = []

def convert_utf8_to_ansi_inplace():
    for lrc_file in lrc_files:
        try:
            with open(lrc_file, "r", encoding="utf-8") as src_file:
                content = src_file.read()

            with open(lrc_file, "w", encoding="gb2312", errors="ignore") as tgt_file:
                tgt_file.write(content)

            print(f"成功转换并替换: {lrc_file}")
        except Exception as e:
            print(f"转换失败: {lrc_file}，错误: {e}")
            lose_files.append(lrc_file)

def walk_lrc_files(folder, recursive):
    if recursive:
        for dirpath, _, filenames in os.walk(folder):
            for filename in filenames:
                if filename.endswith(".lrc"):
                    file_path = os.path.join(dirpath, filename)
                    lrc_files.append(file_path)
    else:
        for filename in os.listdir(folder):
            if filename.endswith(".lrc"):
                file_path = os.path.join(folder, filename)
                lrc_files.append(file_path)

if __name__ == "__main__":
    folder = input("请输入要遍历的文件夹路径: ")
    if input("是否递归遍历子文件夹? (y/n, default:no): ") not in ["y", "yes"]:
        walk_lrc_files(folder, False)
    else:
        walk_lrc_files(folder, True)

    for index, lrc_file in enumerate(lrc_files):
        print(f"{index}: {lrc_file}")

    if input("是否转换上述" + str(len(lrc_files)) + "个文件? (y/n, default:y): ") not in ["y", "", "yes"]:
        exit()
    convert_utf8_to_ansi_inplace()
    print("所有文件转换完毕，转换失败" + str(len(lose_files)) + "个文件\n失败文件：")
    for index, lose_files in enumerate(lose_files):
        print(f"{index}: {lose_files}")