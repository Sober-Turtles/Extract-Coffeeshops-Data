import mysql.connector
from mysql.connector import Error

try:
	connection = mysql.connector.connect(host='37.32.5.76',database='group1',user='user_group1',password='ZgAth4EWY^)AnT9X')
	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Connected to MySQL Server version ", db_Info)
		cursor = connection.cursor()
		cursor.execute("Show tables;")
		tables = cursor.fetchall()
		for x in tables:
			print(x)

except Error as e:
	print("Error while connecting to MySQL", e)