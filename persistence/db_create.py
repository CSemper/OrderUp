import pymysql

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
    
    