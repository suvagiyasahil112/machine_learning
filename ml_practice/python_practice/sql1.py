import mysql.connector
import pandas as pd
import random

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db1'

)
cursor=conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS db1")
# conn.commit()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS STUDENT(
               id INT AUTO_INCREMENT PRIMARY KEY,
               name varchar(100),
               age INT,
               department VARCHAR(100)
               )
''')

conn.commit()
# cursor.execute("INSERT INTO STUDENT(name,age,department)VALUES(%s,%s,%s)",('sahil ',20,'CSE'))
# conn.commit()


names = [chr(i) for i in range(97, 123)]  # Generating names from 'a' to 'z'
departments = [
    "civil", "mechanical", "it", "electrical", "computer science", "electronics",
    "aerospace", "biomedical", "chemical", "industrial", "environmental",
    "software", "robotics", "automobile", "marine", "petroleum", "agricultural",
    "metallurgical", "telecommunication", "nanotechnology"
]
students = [(random.choice(names), random.randint(18, 30), random.choice(departments)) for _ in range(100)]
# for student in students:
#     print(student)

# students=[
#     ('a',25,'civil'),
#     ('e',25,'mechenical'),
#     ('t',15,'it'),
# ]

# cursor.executemany("INSERT INTO STUDENT (name,age,department) VALUES (%s,%s,%s)",students)
# conn.commit()

# query = cursor.execute("SELECT * FROM STUDENT")

# data = pd.DataFrame(query)
# print(data)


# rows= cursor.fetchall()
# for i in rows :
#     print(i)
# query="SELECT * FROM STUDENT"

# df=pd.read_sql(query,conn,index_col="id")
# print (df)

# cursor.execute("SELECT * FROM STUDENT WHERE department =%s",('CSE',))
# rows = cursor.fetchall()
# for i in rows :
#     print(i)
# conn.commit()   

# cursor.execute("SELECT * FROM STUDENT ORDER BY age DESC")
# rows=cursor.fetchall()
# conn.commit()
# query="SELECT * FROM STUDENT"
# df=pd.read_sql(query,conn,index_col="id")
# print (df)


# cursor.execute("SELECT * FROM STUDENT ORDER BY id DESC LIMIT 4 ")
# conn.commit()
# rows = cursor.fetchall()
# for i in rows:
    # print(i)
# conn.commit()    

# cursor.execute("UPDATE STUDENT SET age = %s WHERE id = %s" ,(55,11))
# cursor.execute("UPDATE STUDENT SET age = %s WHERE name = %s", (32, 'sahil'))


# cursor.execute("UPDATE STUDENT SET name = %s WHERE AGE < %s",('oasdhc',10))
# rows = cursor.fetchall()
# for i in rows:
#     print(i)
# conn.commit()


# cursor.execute("DELETE FROM STUDENT WHERE department =%s",('fsdc aqw',))
# conn.commit()

# cursor.execute("DELETE FROM student")
# conn.commit()

# cursor.execute("ALTER TABLE STUDENT ADD email VARCHAR (100)")
# conn.commit()

# cursor.execute("ALTER TABLE STUDENT DROP COLUMN email")
# conn.commit()


# cursor.execute("ALTER TABLE STUDENT MODIFY COLUMN age INT NOT NULL")
# conn.commit()

# cursor.execute('''
#                CREATE TABLE IF NOT EXISTS DEPARTMENTS
#                (
#                id INT AUTO_INCREMENT PRIMARY KEY,
#                name VARCHAR(100)
#                )
#                ''')
# conn.commit()   

# cursor.execute('''
#                INSERT INTO DEPARTMENTS (name) VALUES ('civil'),
#     ('mechanical'),
#     ('it'),
#     ('electrical'),
#     ('computer science'),
#     ('electronics'),
#     ('aerospace'),
#     ('biomedical'),
#     ('chemical'),
#     ('industrial'),
#     ('environmental'),
#     ('software'),
#     ('robotics'),
#     ('automobile'),
#     ('marine'),
#     ('petroleum'),
#     ('agricultural'),
#     ('metallurgical'),
#     ('telecommunication'),
#     ('nanotechnology')''')
# conn.commit()

# cursor.execute('''
#     SELECT STUDENT.name,STUDENT.age,DEPARTMENTS.id,DEPARTMENTS.name 
#                FROM STUDENT INNER JOIN DEPARTMENTS ON STUDENT.department = DEPARTMENTS.name
#  ''')
# rows = cursor.fetchall()
# for i in rows :
#     print(i)

cursor.execute("SELECT department , COUNT(*) FROM STUDENT GROUP BY department")
rows=cursor.fetchall()
for row in rows:
        print(f"{row[0]} : {row[1]} students")

    