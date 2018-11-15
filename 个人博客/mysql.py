import pymysql
db = pymysql.connect(host='134.175.53.90',user = 'root',password = '123456',db='skk',port=3306)
cur=db.cursor()
cur.execute('SELECT VERSION()')
data = cur.fetchall()
print(data)
db.close()