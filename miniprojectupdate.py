from functions.menu import main_menu, start_up, clear_screen
from persistence.db_read import see_people, see_drinks, see_all_preferences
from persistence.db_write import add_people, add_drinks, create_order

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
            
    elif selection ==3:
        create_order()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        main_menu()
        
    elif selection ==5:
        see_all_preferences()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        main_menu()
    
    else:
        exit()