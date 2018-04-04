import re
import mysql.connector
from mysql.connector import errorcode
import uuid

def search_data(subject, expr):
    match = re.search(expr, subject)
    if match:
        result = match.group(1)
    else:
        result = None
    return result

def runtest():
    # 获取第一个匹配项
    m=re.search(r"(\d{1,3})","Hello no.100 to 200")
    if m:
        print("验证通过",m.start(),m.end(),m.groups(),m.group(1))

    else:
        print("验证失败")
    #循环获取所有的匹配项
    for match in re.finditer(r"(\d{1,3})", "Hello no.100 to 200"):
        print(match.group(1))
    #返回list
    data=re.findall(r'\d{1,3}','123,james,H345')
    print(data)
    data=re.split("\d{1,3}","Hello no.100 to 200,test300",0)
    print(data)
    print("uuid=>",str(uuid.uuid1()),uuid.uuid1().hex)

def process_db():
    dbpm = {'user': 'root', 'password': '123', 'host': '', 'database': '', 'use_pure': True, }
    try:
        cnx = mysql.connector.connect(**dbpm)
        cr = cnx.cursor(buffered=True, named_tuple=True)
        cr.execute('select id,actname from wp_activity_inv limit 10')  # 使用数组
        expr = "(\d{2}\.\d{2})"
        for r in cr:
            dt = search_data(r.actname, expr)
            if dt is not None:
                print("update wp_activity_inv set plandate='%s' where id=%s;" % (dt, r.id))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("用户名密码错误")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("数据库%s不存在" % dbpm['database'])
        else:
            print(err)
    else:
        cnx.close()


if __name__ == '__main__':
    runtest()