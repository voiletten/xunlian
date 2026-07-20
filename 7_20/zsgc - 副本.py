import pymysql


conn = pymysql.connect(
    host='192.168.0.45',
    port=3306,
    user='root',
    password='123456',
    db='ds2_db',
    charset='utf8mb4'
)
cursor = conn.cursor()


sql1 = "INSERT INTO student(id,name, age, score) VALUES (1,'张三', 18, 92.5);"
sql4 = "INSERT INTO student(id,name, age, score) VALUES (2,'张三2', 18, 92.5);"

sql3 = "DELETE FROM student WHERE id=2;"
sql2 = "UPDATE student SET score=96 WHERE name='张三';"
sql5 = "SELECT * FROM student;"





cursor.execute(sql1)
cursor.execute(sql4)
cursor.execute(sql3)
cursor.execute(sql2)
cursor.execute(sql5)





conn.commit()
cursor.close()
conn.close()