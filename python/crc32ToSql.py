import zlib

import pymysql

conn = pymysql.connect(host="***", user="***",password="****************",database="******",charset="******")
cursor = conn.cursor()
for i in range(1,600000000):
    try:
        s = zlib.crc32(str(i).encode('utf8'))
        sql = "insert into BilibiliUserCrc32b(id,crc32b) values('{}','{}')"
        cursor.execute(sql.format(i,s))
        conn.commit()
    except:continue


