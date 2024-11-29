import os

files = []
lose_files = []
def convert():
    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as src_file:
                content = src_file.read()

            with open(file, "w", encoding="gb2312", errors="ignore") as tgt_file:
                tgt_file.write(content)

            print(f"成功: {file}")
        except Exception as e:
            print(f"失败: {file}，错误: {e}")
            lose_files.append(file)

def walk_files(folder, recursive):
    if recursive:
        for dirpath, _, filenames in os.walk(folder):
            for filename in filenames:
                if filename.endswith(".lrc"):
                    file_path = os.path.join(dirpath, filename)
                    files.append(file_path)
    else:
        for filename in os.listdir(folder):
            if filename.endswith(".lrc"):
                file_path = os.path.join(folder, filename)
                files.append(file_path)

if __name__ == "__main__":
    while 1:
        folder = input("请输入文件夹路径: ")
        if input("是否递归遍历子文件夹? (y/n, default:no): ") not in ["y", "yes"]:
            walk_files(folder, False)
        else:
            walk_files(folder, True)

        for index, lrc_file in enumerate(files):
            print(f"{index}: {lrc_file}")

        if input("是否转换上述" + str(len(files)) + "个文件? (y/n, default:y): ") not in ["y", "", "yes"]:
            break
        convert()
        if len(lose_files) != 0:
            print("失败文件：")
            for index, lose_files in enumerate(lose_files):
                print(f"{index}: {lose_files}")
        print("所有文件转换完毕，转换失败" + str(len(lose_files)) + "个文件")
        if input("输入任意内容退出，输入(c)继续...") == "c":
            break
        exit()
