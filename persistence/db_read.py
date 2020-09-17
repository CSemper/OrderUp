from classes.Person import Person as Person
person_list =[]

import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")

import pymysql


def see_people ():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    cursor.execute("SELECT person_id, first_name, surname FROM people")
    rows = cursor.fetchall()
    
    for row in rows:
        new_person = Person(row[0], row[1], row[2])
        person_list.append(new_person)
        # print("\t ID Number: " + str(row[0]))
        # print("\t Full Name: " + row[1] + " " + row[2])
        # print("\n")
    cursor.close
    connection.close
    print(person_list)


def see_drinks():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    cursor.execute("SELECT d.drink_id, d.drink_name, d.price, categories.cat_name FROM drinks as d LEFT JOIN categories ON d.category = categories.cat_id")
    rows = cursor.fetchall()
    for row in rows:
        print("\t Drink ID: " + str(row[0]))
        print("\t Drink Info: " + row[1] + " @ £" + str(row[2]) + "  (" + row[3] + ") " )
        print("\n")
        
    cursor.close
    connection.close

def see_all_preferences():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    cursor.execute("SELECT people.first_name, drinks.drink_name FROM people LEFT JOIN drinks ON people.fave_drink = drinks.drink_id")
    rows = cursor.fetchall()
    print("List of Preferences: ")
    for row in rows:
        print("\t" + row[0]  + ":  " + row[1])
        print("\n")
        
    cursor.close
    connection.close

see_people()