# coding: UTF-8
import os.path as path
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
        lines=f.readlines()
        func=lambda txt:'http' in txt
        res=filter(func,lines)
        for x in list(res):
            print(x.strip())


if __name__ == '__main__':
    filename = "/Users/jiangfy/Program/hivemq-3.3.2/conf/config.xml"
    if path.exists(filename):
        view_lines(filename)
