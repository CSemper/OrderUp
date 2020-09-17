from functions.menu import main_menu, clear_screen
from persistence.db_edit import edit_preferences
from persistence.db_read import see_people, see_drinks, see_all_preferences
from persistence.db_write import add_people, add_drinks, create_order
from persistence.db_create import create_receipt

while True: 
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
        if choice_2 == "Y" or choice_2 == "y":
            add_drinks()
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
        else:
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
            
    elif selection ==3:
        choice_3 = int(input("Are you ordering for yourself (1) or for the group (2)? Enter:   "))
        if choice_3 == 1:
            create_order()
            input ("Press ENTER to return to the main menu")
            clear_screen()
            main_menu()
        elif choice_3 == 2:
            print("Group Order Functionality Pending")
        else:
            print("Invalid choice entered. Returning to Main Menu")
    
    elif selection == 4:
        create_receipt()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        main_menu()
        
    elif selection ==5:
        see_all_preferences()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        main_menu()
    
    elif selection == 6:
        edit_preferences ()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        main_menu()
        
    else:
        exit()