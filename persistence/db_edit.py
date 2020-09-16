import sys
sys.path.insert(0,"/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages")
import pymysql

def edit_preferences ():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    
    cursor.execute("SELECT person_id, first_name FROM people")
    rows = cursor.fetchall()
    for row in rows:
        print("\t ID Number: " + str(row[0]) + "\t Name: " + row[1])
   
    id_num= str(input("Please enter your Unique ID Number:   "))
    pref= f"SELECT drinks.drink_name FROM people LEFT JOIN drinks ON people.fave_drink= drinks.drink_id WHERE person_id = {id_num}"
    cursor.execute(pref)
    new_pref= cursor.fetchone()
    current_pref = (new_pref[0])
    print(f"Your Current Preference is: {current_pref}")

    update= input("Do you want to edit your drink preference?  Y or N    ")
    if update == "Y" or update == "y":
        cursor.execute("SELECT drink_id, drink_name FROM drinks")
        rows = cursor.fetchall()
        for row in rows:
            print("\t Drink ID: " + str(row[0]) + "\t Drink Name:  " + row[1])
        new_drink = str(input("Please enter the Unique ID of your preferred drink:   "))
        change_pref= f"UPDATE people SET fave_drink ={new_drink} WHERE person_id = {id_num}"
        cursor.execute(change_pref)
        connection.commit()
        print("Preference Updated")
        cursor.close
        connection.close
    else:
        print ("No Problem!")
