# coding: UTF-8
from exercise.common import show_title

show_title('类的处理')
x = 1
if x == 1:
    print(x)
elif x == 2 and x < 10:
    print(x)
elif x in (1, 2, 3):
    print(x)
elif x is not 3:
    print(x)
else:
    print(x)
while x < 10:
    print(x)
    x += 1
    if x==5:
        continue
    elif x==6:
        print('break while')
        break
for x in range(100):
    print(x,end='')

def func(): pass
