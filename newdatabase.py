#Create new database
import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")

import pymysql

def database_view ():
    connection = pymysql.connect("localhost", "root", "root_password", "brew")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM person")
    rows = cursor.fetchall()
    
    for row in rows:
        print("\t ID Number: " + str(row[0]))
        print("\t Full Name: " + row[1] + " " + row[2])
        print("\n")
        
    cursor.close
    connection.close
    return ("Yes")

database_view()