import re
import mysql.connector
from mysql.connector import errorcode


def search_data(subject, expr):
    match = re.search(expr, subject)
    if match:
        result = match.group(1)
    else:
        result = None
    return result



if __name__ == '__main__':
    dbpm = {'user': 'sa', 'password': 'z4bpyhfma5EKR3b8', 'host': 'hlnhw.cn', 'database': 'webdb', 'use_pure': True, }
    try:
        cnx = mysql.connector.connect(**dbpm)
        cr = cnx.cursor(buffered=True, named_tuple=True)
        cr.execute('select id,actname from wp_activity_inv where  plandate is null')  # 使用数组
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
