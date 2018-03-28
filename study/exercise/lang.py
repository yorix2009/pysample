# coding: UTF-8
"""
这种形式对应__doc__,可以使用内置的帮助来展现
关于Python语言的基础知识
"""
# 全局的变量
import math
from exercise.common import show_title

version = 1.0

# 数字的处理常用用法
# 在3.0中不用在使用L结尾的标识长整型
show_title('数字的处理')
nums = []
nums.append(123)
nums.append(123)
nums.append(123.23)
nums.append(123e2)
nums.append(0x123)
nums.append(0b1010)  # 二进制
nums.append(0o67010)  # 八进制
nums.append(3 + 4j)  # 复数
for num in nums: print(" - ", num)
print("12的平方= %d" % 12 ** 2)
print("13/3= {}".format(13 / 3))
print("13//3地板除法= {}".format(13 // 3))  # floor除法
print("13%3= {}".format(13 % 3))
print("round(13/3,2)= {}".format(round(13 / 3, 2)))
print("math.ceil(13/3)= {}".format(math.ceil(13 / 3)))
print("PI=", math.pi)
print("不同的进制转换{}，{}，{} {} {} {}".format(123, hex(123), oct(123), bin(123), float(123), int('0x7b', 16)))
print("\n" * 2)

##字符串的处理
show_title('字符串的处理')
#字符串默认转换为一个列表
# print 格式化输出
# 转换类型          含义
#
# d,i                 带符号的十进制整数
# o                   不带符号的八进制
# u                   不带符号的十进制
# x                    不带符号的十六进制（小写）
# X                   不带符号的十六进制（大写）
# e                   科学计数法表示的浮点数（小写）
# E                   科学计数法表示的浮点数（大写）
# f,F                 十进制浮点数
# g                   如果指数大于-4或者小于精度值则和e相同，其他情况和f相同
# G                  如果指数大于-4或者小于精度值则和E相同，其他情况和F相同
# C                  单字符（接受整数或者单字符字符串）
# r                    字符串（使用repr转换任意python对象)
# s                   字符串（使用str转换任意python对象）
# 不换行，在后面增加end=''
strs = []
strs.append('abc')
strs.append('ab\'c')
strs.append('ab"c')
strs.append(b"abc\x01am")
strs.append(r"abc\x01am")
strs.append(u"测试abc\x01am")
strs.append("""
hello world
换行字符串
""")
strs.append('*' * len(strs))


concat_str = ''
for s in strs:
    if isinstance(s, str):
        concat_str += s
    elif isinstance(s, bytes):
        concat_str += str(s)
    else:
        concat_str += str(s)
    print(" - ", s)
concat_str = concat_str.replace('\n', '')
print('join的字符串=', concat_str)
print('分片的用法 {1}\n，{0}\n，{2}\n，{3}\n'.format(concat_str[1:2], concat_str[:], concat_str[1:-1], concat_str[-1]))
print("字符串格式化%s %d %.2f" % ('hello', 123, 23.5438))
print("基于字典的字符串格式化%(name)s  %(v2).2f v1=%(v1)d" % {'name': 'james', 'v1': 123, 'v2': 34.657})
print("基于字典的字符串格式化{name} {v1} {v2}".format(name='james', v1=123, v2=34.56))
# 更复杂的用法可以在v2=list() dict()等，同时在里面使用属性值来访问
# format方法拥有%一些没有的处理方式
print('\n' * 2)


