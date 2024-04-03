#this is app.py
#app.py is the core to access aiModule.py and rdpModule.py, this part of the program should be responsible for opening the main screen of the app.
#on the main screen there should be 3 buttons only 1: button to access Random Data Producer module, 2: button to access: STQB Helper module and one more button (Q) to stop and close the program
#the ui could be created with customtkinter

import rdpModule, aiModule, time, os



def main():
    while True:
        print("Hello User, which module would you like to access?")
        print("1: Random Data Producer")
        print("2: ISTQB Helper")
        print("Q: To exit program")
        choice = input("Press a button to open the desired menu: ")
        
        if choice == '1':
            print("Executing Random Data Producer module...")
            time.sleep(1)  # Call the function from aiModule
            os.system('cls')
            rdpModule.run_data_generation()
            
        elif choice == '2':
            print("Executing ISTQB Helper module...")
            time.sleep(1)  # Call the function from aiModule
            os.system('cls')
            aiModule.run_istqb_helper()  # Call the function from aiModule

        elif choice == 'Q' or 'q':
            print("Stopping...")
            time.sleep(1)  # Call the function from aiModule
            os.system('cls')
            break    
        else:
            print("Invalid input. Please enter 1, 2 or Q.")

if __name__ == "__main__":
    main()