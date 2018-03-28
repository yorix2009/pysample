# coding: UTF-8
from exercise.common import show_title

# class
# __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
#
# _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
#
# __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。
show_title('类的处理')


class BaseUser:
    __version = 1.0  # 定义一个私有变量

    def __init__(self, oid):
        self._id = oid

    def __str__(self):
        return "用户id=%s %s" % (self._id, BaseUser.__version)


class DbUser(BaseUser):
    _name = None

    def __init__(self, oid, name):
        # BaseUser.__init__(self, oid)
        super().__init__(oid)
        self._name = name

    # 属性的定义
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    def __str__(self):
        return "用户id=%s name=%s" % (self._id, self._name)

    def test(self):
        print("测试：" + self._id, self._name)

    @staticmethod
    def calc(x, y):
        return x + y


o = DbUser('1000', '张三')
o.name = 'james'
print(o, o._name, o.name)
o.test()
print(DbUser.calc(1, 2))
b = BaseUser('1001')
print(b)
print('访问__的特殊方法', b._BaseUser__version)
