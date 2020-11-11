# Using mysql-connector package import to use with python
#import mysql.connector

#servername = "127.0.0.1:3306"
#username   = "root"
#password   = "vNett3ch#."
#database   = "VxLIBSTATS-DIR"

# Establish DB connection
#myPyDB = mysql.connector.connect(servername, username, password, database)
#print(myPyDB)



#Using Python Web Framwork Flask
#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello, World!'



# HTTP example with urllib
#import urllib.request

#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())




# HTTP example with socket
#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()

#mysock.send(cmd)

#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')

#mysock.close()





# Mysql connector example
import mysql.connector


mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "vNett3ch#.",
    database = "VxLIBSTATS-DIR"
)

# Now how do we comm w/db
# Need a ptr so we call method cursor
myPtr = mydb.cursor()

# And to issue commands to the db use the ptr.execute
# myPtr.execute() or executemany(<args>)

# Can create a sqlQ = "Select...."
libID="US_VA_MCPL"
sqlQ = "SELECT vxstatsDB as statsDB, node, systemID  FROM Libraries WHERE libraryID = 'US_VA_MCPL'";
print(f"This is my selection of libID {libID} in sql Query {sqlQ}")
# Then  pass the variable to execute => myPtr.execute(sqlQ)
myPtr.execute(sqlQ)
myQrslt = myPtr.fetchall()
#print(f"Got the statsdb {myQrslt[vxstatsDB]}")
# The result captured to some var, e.g. myRslt = myPtr.fetchall()
# Then can process each row of all fetched data by myRslt
for row in myQrslt:
    print(f"got this statsDB from row {row[0]} out of {len(row)} ")


# complete communication with mysql
#mydb.commit()