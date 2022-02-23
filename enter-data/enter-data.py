import pyodbc
import pandas as pd
import mysql.connector

n = int(input("how many values will you provide (integer): "))

list1= []
for i in range(n):
    value=int(input("enter the value: "))
    list1.append(value)

print("list values are: ",list1)

conn = mysql.connector.connect(host='localhost',
                              database='docker',
                              user='docker',
                              password='docker')

mysql_insert=""" INSERT INTO docker (values) VALUES (%s) """

cursor=conn.cursor()
cursor.execute(mysql_insert, list1)
