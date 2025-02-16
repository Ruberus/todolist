#add dates automatically(?)

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  # Load environment variables from .env file

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)

cursor = conn.cursor()

cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()
print("Connected to database:", result)

creation='''CREATE TABLE IF NOT EXISTS todolist(SerialNumber INTEGER PRIMARY KEY,
Status VARCHAR(4),
TaskName VARCHAR(1000) NOT NULL,
Date DATE);'''
cursor.execute(creation)

def addtask(cursor,conn):
    newtask=input('Enter your task:')
    date= input('Enter the date (YYYY-MM-DD):')
    taskq='''INSERT INTO todolist (Status,TaskName,Date) VALUES
(%s,%s,%s)'''
    values=('',newtask,date)
    cursor.execute(taskq,values)
    conn.commit()


addtask(cursor,conn)

cursor.execute("SELECT * FROM todolist;")
data=cursor.fetchall()
print(data)






cursor.close()
conn.close()
