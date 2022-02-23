import sqlite3
import mysql.connector

conn = mysql.connector.connect(host='localhost',
                              database='docker',
                              user='docker',
                              password='docker')

mysql_create_table=""" CREATE TABLE docker (value int(5))"""

cursor=conn.cursor()
cursor.execute(mysql_create_table)
