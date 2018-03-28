# coding: UTF-8
import sys
from functools import reduce
from exercise.common import show_title

# lambda
show_title('lambda')
add_method = lambda x, y: x + y
print(add_method(1, 2))
data = list(range(100))

# filter过滤数据方法
sdata = list(filter(lambda x: x < 40 and x > 30, data))
print(sdata)

# map方法
mapdata = map(lambda x: x + 2, sdata)
listdata = list(mapdata)
print("list(mapdata)=", listdata)
# 对于打印输出的lambda
lprint = lambda x: sys.stdout.write(x + '\n')
lprint("lambda x: sys.stdout.write(x+'\\n')")

# reduce方法
# 从左到右对一个序列的项累计地应用有两个参数的函数，以此合并序列到一个单一值
res = reduce(lambda x, y: x + y, listdata, 0)
print(res)
