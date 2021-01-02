# 파이썬 DB연동 (SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

#삽입 날짜 생성

now = datetime.datetime.now()


nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S") ## 날짜 포메팅
print(nowDatetime)

# sqlite3

print('sqllite3.version : ', sqlite3.version)
print('sqllite3.sqlite_version : ', sqlite3.sqlite_version)
'''
sqllite3.version :  2.6.0
sqllite3.sqlite_version :  3.30.0
'''

# DB생성 및 Auto commit , Rollback

conn = sqlite3.connect('database.db', isolation_level=None)

conn.commit()

# Cursorc

c = conn.cursor()


print('Cursor type' , type(c)) # Cursor type <class 'sqlite3.Cursor'>

# Create Table

# DataTyoe in SQLite

# TEXT, NUMERIC, INTEGER, REAL, BLOB

c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, phone text,  \
    website text, regdate text)"
)

# 데이터 삽입 CRUD : 

# c.execute("INSERT INTO users VALUES(1, 'KIM', 'example@exmaple.com', '000-0000-0000', \
#     'test.com', ?)", (nowDatetime,))

# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)",
# (2, 'park', 'park@com.com', '010-1111-1111', 'park.com', nowDatetime))

