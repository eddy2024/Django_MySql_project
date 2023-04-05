import  mysql.connector

dataBase = mysql.connector.connect(
    
    host ='localhost',
    user = 'root',
    password = '2023$Nu66et'    
)
#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE mogodb")

print("All done!")