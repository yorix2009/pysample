count = 1


def show_title(msg):
    global count
    print('\n')
    print('#' * 30)
    print(count, '.', msg)
    print('#' * 30)
    count += 1
