# coding: UTF-8
import os.path as path
import os
from exercise.common import show_title

# 文件处理
show_title('文件处理')


def viewfile(filename):
    with open(filename) as f:
        print(f.read())


def view_lines(filename):
    with open(filename) as f:
        i = 1
        for line in f:
            print(i, ' ', line.rstrip())
            i += 1
        # 重新读取文件
        f.seek(0)
        lines = f.readlines()
        func = lambda txt: 'http' in txt
        res = filter(func, lines)
        for x in list(res):
            print(x.strip())


# 文件系统扫描处理
def print_files(path):
    # 直接使用os.walk处理
    for dirpath, dirnames, filenames in os.walk(path):
        # print(dirpath)
        # print('>',dirnames)
        print('>>', filenames)
    for dir in os.scandir(path):
        if dir.is_dir():
            print('d ', dir.name)
        else:
            print('f ', dir.name, dir.stat().st_size)


if __name__ == '__main__':
    filename = os.environ['HOME'] + "/Program/hivemq-3.3.2/conf/config.xml"
    if path.exists(filename):
        view_lines(filename)
    pdir = path.dirname(filename)
    print_files(pdir)
    print('系统环境变量')
    for k, v in os.environ.items():
        print(k, '=>', v)
