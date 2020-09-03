from functions.menu import main_menu, start_up, clear_screen, person_list, drink_list, order_list, preference_list
from persistence.file_handling import save_people, save_order, save_drinks, save_preferences
from functions.edits import add_people, add_drinks
from classes.Person import Person as Person
from classes.Drink import Drink as Drink
from classes.Order import Order as Order
from classes.Preference import Preference as Preference
import csv

    
while True: 
    start_up()
    main_menu()
    selection = int(input("\n Please enter your selection here:  "))
    
    if selection == 1:
        for individual in person_list:
            print(individual)
        choice = input ("Would you like to add to this list? Y or N \n")
        if choice == "Y" or choice == "y":
            add_people()
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
        else:
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
        
    elif selection == 2:
        for drink in drink_list:
                print(drink)
        choice_2= input ("Would you like to add to this list? Y or N \n")
        if choice_2 == "Y" or choice_2== "y":
            add_drinks()
        else:
            input ("Press ENTER to return to the main menu")
            main_menu()
    
    elif selection == 3:
        for person in person_list:
            name= person.name
            print("\n" + name + ":")
            select = input (f"\n \t Does {name} want to order a drink? Y or N:   ")
            if select == "Y" or select == "7":
                print ("\t Please choose from the following list of drinks:  ")
                for drink in list(enumerate(drink_list, start=1)):
                    print(drink)
                    # drink_name= drink.kind
                    # print(drink_name)
                choice = input("Enter your choice here:   ")
                order= Order(name, choice)
                order_list.append(order)
            else:
                continue
        input ("Press ENTER to return to the main menu")
        main_menu()

    elif selection == 4:
        for order in order_list:
            print(order)
            
    elif selection == 5:
        for person in person_list:
            name = person.name
            print("\n" + name + ":")
            print ("\n \t Please choose from the following list of drinks:  ")
            for drink in drink_list:
                kind= drink.kind
                print("\t" + " ** " + kind)
            record = input("Enter your choice of drink here:   ")
            temp = input("What temperature do you prefer this drink?   ")
            preference= Preference(name, record, temp)
            preference_list.append(preference)
        input ("Press ENTER to return to the main menu")
        main_menu()
    
    elif selection == 6:
        for preference in preference_list:
            print(preference)  
                   
    else:
        save_drinks("drink_output.csv")
        save_people("person_output.csv")
        save_order("order_output.csv")
        save_preferences ("preferences_output.csv")
        exit()