# coding: UTF-8

from graphics import *

# 设置画布窗口名和尺寸
win = GraphWin('CSSA', 700, 700)

# 画点
pt = Point(100, 100)
pt.draw(win)
Point(0,0).draw(win)

# 画圆
cir = Circle(Point(200, 200), 75)
cir.draw(win)
cir.setOutline('red')  # 外围轮廓颜色
cir.setFill('yellow')  # 填充颜色

# 画线
line = Line(Point(0, 0), Point(0, 1000))
line.setFill('red')
line.draw(win)
line=Line(Point(0, 0), Point(1000, 0))
line.setFill('red')
line.draw(win)

# 画矩形
rect = Rectangle(Point(300, 300), Point(400, 400))
rect.setFill('red')  # 填充颜色
rect.draw(win)

# 画椭圆
oval = Oval(Point(450, 450), Point(600, 600))
oval.setFill('red')  # 填充颜色
oval.draw(win)

# 显示文字
message = Text(Point(win.getWidth() / 2, 20), 'Click anywhere to quit.')
message.draw(win)

# 关闭画布窗口
win.getMouse()
win.close()