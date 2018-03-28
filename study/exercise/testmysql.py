# coding: UTF-8
from exercise.common import show_title
import mysql.connector
from mysql.connector import errorcode
import time

# Mysql数据库操作
show_title('Mysql数据库操作')
print('安装驱动：pip3 install mysql-connector-python')


def query_data(cnx):
    cr = cnx.cursor()
    cr.execute('select * from wp_config limit 2')
    values = cr.fetchall()
    for r in values:
        print(r)
    cr.close()


def query_data_param(cnx):
    cr = cnx.cursor()
    cr.execute('select id,name,title from wp_config')  # 使用数组
    for id, name, title in cr:
        print(id, name, title)
    cr.close()


def query_data_tuple(cnx):
    cr = cnx.cursor(buffered=True, named_tuple=True)
    cr.execute('select id,name,title from wp_config')  # 使用数组
    for r in cr:
        print('named_tuple输出=', r.id, r.name, r.title)
    cr.close()


def query_data_all(cnx):
    cr = cnx.cursor(buffered=True)
    cr.execute('select id,name,title from wp_config where id= %s ', [1, ])  # 使用数组
    values = cr.fetchall()
    for r in values:
        print("fetchall输出=", r)
    cr.close()


def query_data_dict(cnx):
    cr = cnx.cursor(buffered=True, dictionary=True)
    cr.execute('select id,name,title from wp_config')  # 使用数组
    for r in cr:
        print("Dict输出=", r['id'], r['name'], r['title'])
    cr.close()


# 使用预备参数的模式，必须使用use_pure=True
def query_data_insert(cnx):
    cr = cnx.cursor(cursor_class=mysql.connector.cursor.MySQLCursorPrepared,dictionary=True)
    cr.execute('delete from wp_url')
    sql = 'insert into wp_url(url,short,status,create_time)values(?,?,?,?)' #可以使用？或%s
    c=0
    for x in range(10):
        cr.execute(sql, ('http://127.0.0.' + str(x), '测试', 1, time.time()))  # 使用数组
        c+=1
    cr.close()
    cr = cnx.cursor(buffered=True, named_tuple=True)
    cr.execute('select * from wp_url')  # 使用数组
    for r in cr:
        print('named_tuple输出=', r.id,r.short,r.url)
    print('插入数据：',c)

    cr.close()


if __name__ == '__main__':
    dbpm = {'user': 'root', 'password': '123', 'host': '127.0.0.1', 'database': 'webdb', 'use_pure': True, }
    try:
        cnx = mysql.connector.connect(**dbpm)
        funcs = list(filter(lambda s: s.startswith('query_data_insert'), dir()))
        for f in funcs:
            print('')
            print('=' * 20)
            print('调用：', f)
            print('=' * 20)
            eval(f + '(cnx)')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("用户名密码错误")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("数据库%s不存在" % dbpm['database'])
        else:
            print(err)
    else:
        cnx.close()
