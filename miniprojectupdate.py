from functions.menu import main_menu, start_up, clear_screen
from persistence.db_read import see_people, see_drinks, see_all_preferences
from persistence.db_write import add_people, add_drinks

while True: 
    start_up()
    main_menu()
    selection = int(input("\n Please enter your selection here:  "))
    
    if selection == 1:
        see_people()
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
        see_drinks()
        choice_2 = input ("Would you like to add to this list? Y or N \n")
        if choice_2 == "Y" or choice == "y":
            add_drinks()
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
        else:
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
        
    elif selection ==6:
        see_all_preferences()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        main_menu()
        
    # elif selection == 3:
    #     for person in person_list:
    #         name= person.name
    #         print("\n" + name + ":")
    #         select = input (f"\n \t Does {name} want to order a drink? Y or N:   ")
    #         if select == "Y" or select == "7":
    #             print ("\t Please choose from the following list of drinks:  ")
    #             for drink in list(enumerate(drink_list, start=1)):
    #                 print(drink)
    #                 # drink_name= drink.kind
    #                 # print(drink_name)
    #             choice = input("Enter your choice here:   ")
    #             order= Order(name, choice)
    #             order_list.append(order)
    #         else:
    #             continue
    #     input ("Press ENTER to return to the main menu")
    #     main_menu()