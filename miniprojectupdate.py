from functions.menu import main_menu, clear_screen
from persistence.db_edit import edit_preferences
from persistence.db_read import see_people, see_drinks, see_all_preferences
from persistence.db_write import add_people, add_drinks, create_order
from persistence.db_create import create_receipt, create_round, round_receipt

while True: 
    main_menu()
    selection = int(input("\n Please enter your selection here:  "))
    
    if selection == 1:
        clear_screen()
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
            
        
    elif selection == 2:
        clear_screen()
        see_drinks()
        choice_2 = input ("Would you like to add to this list? Y or N \n")
        if choice_2 == "Y" or choice_2 == "y":
            add_drinks()
            input ("Press ENTER to return to the main menu")
            clear_screen()  
        else:
            input ("Press ENTER to return to the main menu")
            clear_screen()
          
            
    elif selection ==3:
        clear_screen()
        choice_3 = int(input("Are you ordering for yourself (1) or for the group (2)? Enter:   "))
        if choice_3 == 1:
            create_order()
            input ("Press ENTER to return to the main menu")
            clear_screen()
        elif choice_3 == 2:
            create_round()
            input ("Press ENTER to return to the main menu")
            clear_screen()
        else:
            print("Invalid choice entered. Returning to Main Menu")
            clear_screen()
    
    elif selection == 4:
        clear_screen()
        create_receipt()
        input ("Press ENTER to return to the main menu")
        clear_screen()
    
    elif selection ==5:
        clear_screen()
        round_receipt()
        input ("Press ENTER to return to the main menu")
        clear_screen()
        
    elif selection == 6:
        clear_screen()
        see_all_preferences()
        edit= input("Would you like to edit any of these preferences? Y or N:   ")
        if edit == "Y" or edit == "y":
            edit_preferences ()
            input ("Press ENTER to return to the main menu")
            clear_screen()
        else:
            input ("Press ENTER to return to the main menu")
            clear_screen()
    
    else:
        print( "Bye")
        exit()