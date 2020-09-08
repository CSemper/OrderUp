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

def create_order():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    
    people_list= "SELECT person_id, first_name FROM people"
    cursor.execute(people_list)
    rows = cursor.fetchall()
    for row in rows:
        print("\t " + str(row[0]) + ":  " + row[1])
    person = int(input("Please Enter the Unique ID of the person making the order:   "))
    age_check = f"SELECT age FROM people WHERE person_id = {person}"
    cursor.execute(age_check) 
    get_age = cursor.fetchone()
    age = (get_age[0])
    if age <= 17:
        adjusted_drink_list = "SELECT drink_id, drink_name, price FROM drinks WHERE alcoholic = 'FALSE' "
        cursor.execute(adjusted_drink_list)
        adl= cursor.fetchall()
        for entry in adl:
            print ("\t" + str(entry[0]) + ": " + entry[1] + " @ £" + str(entry[2]))
    else:
        full_drink_list= "SELECT drink_id, drink_name, price FROM drinks"
        cursor.execute(full_drink_list)
        fdl= cursor.fetchall()
        for entry in fdl:
            print ("\t" + str(entry[0]) + ": " + entry[1] + " @ £" + str(entry[2]))
    
    print("Each order is limited to a maximum of 4 drinks!\n")
    choice_1= int(input("Please select the first drink for this order from above list:   "))
    choice_2= int(input("Please select the second drink for this order from above list:   "))
    choice_3= int(input("Please select the third drink for this order from above list:   "))
    choice_4= int(input("Please select the final drink for this order from above list:   "))
    
    sql = "INSERT INTO orders (date, person_id, drink1, drink2, drink3, drink4) VALUES (now(), %s, %s, %s, %s, %s)"
    cursor.execute(sql, (person, choice_1, choice_2, choice_3, choice_4))
    connection.commit()
    print("Order Recorded")
    
    cursor.close
    connection.close
   
create_order()