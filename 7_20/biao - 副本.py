import pymysql


conn = pymysql.connect(
    host='192.168.0.45',
    port=3306,
    user='root',
    password='123456',

    charset='utf8'
)
cursor = conn.cursor()


sql1 = "CREATE DATABASE IF NOT EXISTS ds2_db DEFAULT CHARACTER SET utf8mb4;"
# sql2 = "CREATE DATABASE IF NOT EXISTS student_db DEFAULT CHARACTER SET utf8mb4;"
sql2 = "USE ds2_db;"
sql3 = """CREATE TABLE IF NOT EXISTS student (
    id INT PRIMARY KEY AUTO_INCREMENT COMMENT '主键自增ID',
    name VARCHAR(50) NOT NULL COMMENT '学生姓名',
    age TINYINT COMMENT '年龄',
    score DECIMAL(5,2) COMMENT '分数',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""




cursor.execute(sql1)
print("数据库成功建立")
cursor.execute(sql2)
cursor.execute(sql3)
# cursor.execute(sql2)
print("biao成功建立")


cursor.close()
conn.close()