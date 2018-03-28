from exercise.common import show_title
import collections

# 列表的处理
show_title('列表的处理')
lists = []
lists.append([])
lists.append([1, 2, 3, 't'])
lists.append(list('text'))  # 字符串打散变成list
for x in lists: print(x)
data = lists[2] + lists[1], lists[1] * 2
print(data)
if 't' in lists[2]:
    print('t in data=True')
else:
    print('t in data=False')
print("列表也支持分片的用法")
print('\n' * 2)

# 字典的处理
show_title('字典的处理')
dict1 = {'v1': 123, 'v2': 23.45}
dict1['name'] = 'tom'
for (k, v) in dict1.items():
    print(k, v)
print(",".join(dict1.keys()))
# 使用*解包对象
print(*list(dict1.values()), end='', sep=',')
print("\ndict1 size=", len(dict1))
dict2 = dict(zip(dict1.keys(), dict1.values()))
print(dict2)
print(dict2.fromkeys(['name']))
print(dict2.get('vv', '--none--'))
print('\n' * 2)

# 元组的处理
show_title('元组的处理')
tudata = (1, 2, 3)
print(tudata)
print(tuple('hello') + tuple('world'))
print("这了个不一样：", (40), (40,))
print('\n' * 2)

# nametuple元组的处理
# namedtuple创建一个和tuple类似的对象，而且对象拥有可访问的属性
show_title('nametuple元组的处理')
User = collections.namedtuple('UserObject', 'name,age,sex')
o = User('tom', age=20, sex='男')
print(o._asdict())
# o.name='james'  设置失败，仅仅只读
print(o.name, o.sex, type(o), isinstance(o, User))
print('\n' * 2)

# counter的处理
# counter实现了一个快速的统计计算工具
show_title('counter的处理')
cnt = collections.Counter()
list=['red', 'blue', 'red', 'green', 'blue', 'blue']
for word in list:
    cnt[word] += 1
print(cnt)
print('实现词频统计：',collections.Counter(list).most_common(1))


#其他的数据对象
# 双端队列 deque
# 缺省数据字典，支持缺省值的处理
# 排序数据字典，支持按照加入顺序排队