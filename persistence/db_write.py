import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")

import pymysql

def add_people ():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
   
    p_first_name= input("Please enter your first name:   ")
    p_surname= input ("Please enter your surname:   ")
    p_age= int(input("Please enter your current age:   "))
    
    sql = "INSERT INTO people (first_name, surname, age) VALUES (%s, %s, %s)"
    cursor.execute(sql, (p_first_name, p_surname, p_age))
    
    connection.commit()
    print("Entry Added")
    
    cursor.close
    connection.close
    
def add_drinks ():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
   
    d_name= input("Please enter name of drink:   ")
    
    cat_list= "SELECT cat_id, cat_name FROM categories"
    cursor.execute(cat_list)
    rows = cursor.fetchall()
    for row in rows:
        print("\t " + str(row[0]) + ":  " + row[1])
   
    d_cat= int(input ("Please select the drink category from above list:   "))
    d_temp= input("Is this drink hot or cold?:   ")
    d_price= float(input("How much does this drink cost?   "))
    d_alco = bool(input("Is this drink alcoholic? Type True or False:   "))
    
    sql = "INSERT INTO drinks (drink_name, category, temp, price, alcoholic) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (d_name, d_cat, d_temp, d_price, d_alco))
    
    connection.commit()
    print("Entry Added")
    
    cursor.close
    connection.close