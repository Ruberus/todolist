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

#Create a cursor object
cursor = conn.cursor()

#Execute a query
cursor.execute("SELECT DATABASE();")
result = cursor.fetchone()
print("Connected to database:", result)

cursor.close()
conn.close()
