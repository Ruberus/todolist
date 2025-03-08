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

while True:
    opt=int(input('What do you want to do?\n1. Add tasks\n2. View tasks\n3. Remove a task\n4. Mark task as done: '))
    
    def addtask(cursor,conn):
        newtask=input('Enter your task:')
        date= input('Enter the date (YYYY-MM-DD):')
        taskq='''INSERT INTO todolist (Status,TaskName,Date) VALUES
    (%s,%s,%s)'''
        values=('',newtask,date)
        cursor.execute(taskq,values)
        conn.commit()

    def viewtasks(cursor,conn):
        cursor.execute("SELECT * FROM todolist;")
        data=cursor.fetchall()
        print(data)

    def deltask(cursor,conn):
        que=int(input('Enter the serial number of task you want to delete: '))
        taskd=''' DELETE FROM todolist 
        WHERE SerialNumber=%s;'''
        cursor.execute(taskd,(que,))
        conn.commit()

    def marktask(cursor,conn):
        taskw=int(input('Enter the Serial Number of the task:'))
        taskq='''UPDATE todolist
        SET Status='✓'
        WHERE SerialNumber=%s;'''
        cursor.execute(taskq,(taskw,))
        conn.commit()

    

    
    
    if opt!=1 and opt!=2 and opt!=3 and opt!=4:
        print("please choose a valid option")
    elif opt==1:
        viewtasks(cursor,conn)
        addtask(cursor,conn)
    elif opt==2:
        viewtasks(cursor,conn)
    elif opt==3:
        viewtasks(cursor,conn)
        deltask(cursor,conn)
    elif opt==4:
        marktask(cursor,conn)
        viewtasks(cursor,conn)
       

    opt3=input('Do you want to end the program? Y/N:')
    if opt3=='Y' or opt3=='y':
        break





cursor.close()
conn.close()
