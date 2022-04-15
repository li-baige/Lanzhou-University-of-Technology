#--*coding:utf8* --
import pymysql

try:
    connection = pymysql.connect(
        host='101.35.252.249', # 主机名
        #user = 'user_test', # 数据库用户名
        user = 'user_test',
        #password = 'passwd.666', # 数据库密码
        password = 'passwd.666',
        db = 'testdb', # 数据库名
        charset = 'utf8', # 编码格式
        cursorclass = 'pymysql.cursors.DictCursor' # 游标类型
    )
    print(connection)
except Exception as e:
    print(e)
    
