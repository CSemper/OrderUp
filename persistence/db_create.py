import pymysql

def sum_list(l):
    sum = 0
    for x in l:
        sum += x
    return sum

def create_receipt():
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    order_id= int(input("Please enter your Order ID to retrieve your receipt:   "))
    
    drink1 = (f"SELECT d.drink_name, d.price FROM orders as o LEFT JOIN drinks as d ON o.drink1 = d.drink_id WHERE o.order_id={order_id}")
    cursor.execute(drink1)
    drink_info_1 = cursor.fetchone()
    drink_1_name = (drink_info_1[0])
    drink_1_price = (drink_info_1[1])
    
    drink2 = (f"SELECT d.drink_name, d.price FROM orders as o LEFT JOIN drinks as d ON o.drink2 = d.drink_id WHERE o.order_id={order_id}")
    cursor.execute(drink2)
    drink_info_2 = cursor.fetchone()
    drink_2_name = (drink_info_2[0])
    drink_2_price = (drink_info_2[1])
    
    drink3 = (f"SELECT d.drink_name, d.price FROM orders as o LEFT JOIN drinks as d ON o.drink3 = d.drink_id WHERE o.order_id={order_id}")
    cursor.execute(drink3)
    drink_info_3 = cursor.fetchone()
    drink_3_name = (drink_info_3[0])
    drink_3_price = (drink_info_3[1])
    
    drink4 = (f"SELECT d.drink_name, d.price FROM orders as o LEFT JOIN drinks as d ON o.drink4 = d.drink_id WHERE o.order_id={order_id}")
    cursor.execute(drink4)
    drink_info_4 = cursor.fetchone()
    drink_4_name = (drink_info_4[0])
    drink_4_price = (drink_info_4[1])
    
    receipt_info=(f"SELECT o.date, p.first_name FROM orders as o LEFT JOIN people as p ON o.person_id = p.person_id WHERE order_id={order_id}")
    cursor.execute(receipt_info)
    receipt= cursor.fetchone()
    date= str(receipt[0])
    name = (receipt[1])
    
    total = (drink_1_price + drink_2_price + drink_3_price + drink_4_price)
    
    print("=============================================")
    print("****************** RECEIPT ******************")
    print(f"Date: {date}     \t Ordered By: {name}")
    print("=============================================")
    print("Drinks Ordered: \n")
    print(f"{drink_1_name} \t \t \t £{drink_1_price}")
    print(f"{drink_2_name} \t \t \t £{drink_2_price}")
    print(f"{drink_3_name} \t \t \t £{drink_3_price}")
    print(f"{drink_4_name} \t \t \t £{drink_4_price}")
    print("---------------------------------------------")
    print(f"Total Due: \t \t \t £{total}")
    print("=============================================")
    
def create_round():
    round_id = int(input("Please Enter The Unique ID Number of Your Round:     "))
    
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    cursor.execute("SELECT  p.first_name, p.age, d.drink_name, d.drink_id FROM people as p LEFT JOIN drinks as d ON p.fave_drink = d.drink_id")
    rows = cursor.fetchall()
    for row in rows:
        person_name=(row[0])
        age= int(row[1])
        fave= (row[2])
        drink_id=(row[3])
        print(person_name + ":")
        choice= input(f"Your pre-selected preference is {fave}. Would you like to order this? Y or N:   ")
        if choice == "Y" or choice =='y':
            sql = "INSERT INTO rounds (date, round_id, person, drink_id) VALUES (now(), %s, %s, %s)"
            cursor.execute(sql, (round_id, person_name, drink_id))
            connection.commit()
            
        elif choice == "N" or choice =="n":
            print ("\t Please choose from the following list of drinks:  ")
            
            if age >= 18:
                full_drink_list= "SELECT drink_id, drink_name, price FROM drinks"
                cursor.execute(full_drink_list)
                fdl= cursor.fetchall()
                for entry in fdl:
                    print ("\t" + str(entry[0]) + ": " + entry[1] + " @ £" + str(entry[2]))
            else:
                adjusted_drink_list = "SELECT drink_id, drink_name, price FROM drinks WHERE alcoholic = 'FALSE' "
                cursor.execute(adjusted_drink_list)
                adl= cursor.fetchall()
                for entry in adl:
                    print ("\t" + str(entry[0]) + ": " + entry[1] + " @ £" + str(entry[2]))
            
            alternate= int(input("Please select your chosen drink for this order from above list:   "))
            sql = "INSERT INTO rounds (date, round_id, person, drink_id) VALUES (now(), %s, %s, %s)"
            cursor.execute(sql, (round_id, person_name, alternate))
            connection.commit()
            
            print(f"Round {round_id} Complete")

def round_receipt():
    drink_list=[]
    connection = pymysql.connect("localhost", "root", "Chenyse2017!", "miniproject")
    cursor = connection.cursor()
    unique_id= int(input("Please enter your Unique Round ID to retrieve your receipt:   "))
    
    print("=============================================")
    print("****************** RECEIPT ******************")
    print(f"Order ID: {unique_id}")
    print("=============================================")
    print("Drinks Ordered: \n")
    
    info=(f"SELECT d.drink_name, d.price FROM rounds as r LEFT JOIN drinks as d ON r.drink_id = d.drink_id WHERE r.round_id={unique_id}")
    cursor.execute(info)
    rows = cursor.fetchall()
    for row in rows:
        drink_name= (row[0])
        drink_price=(row[1])
        drink=(f"{drink_name} \t \t \t £{drink_price}")
        print(drink)
        drink_list.append(drink_price)
    
    print("---------------------------------------------")
    total=sum_list(drink_list)
    print(f"Total Due: \t \t \t £{total}")
    print("=============================================")
