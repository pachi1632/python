import mysql.connector
import json
import os

cnx = mysql.connector.connect(user='root', password='CloudFirst@123',
                              host='127.0.0.1', database='realtor')
mycursor = cnx.cursor()
mycursor.execute("SELECT * FROM campaign")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)