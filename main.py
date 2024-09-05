import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Peppapig@123",
  database="systembase"
)

mycursor = mydb.cursor()
