import winreg as wrg
import sys

def reg_add():
    try:
        # storing location of HKEY_CURRENT_USER
        location = wrg.HKEY_CURRENT_USER

        # store the path
        path = wrg.OpenKeyEx(location, r"Software\\")
        key = wrg.CreateKey(path,"mypath")
        print(" how may values do you want to add in your key  ")
        choice = int(input("enter the number: "))
        i=0
        while i < choice:
            # enter the value and the data for your value
            value = input("Enter the value you want to add : ")
            field = input("Enter the data in your value : ")

            # make changes in the registery
            wrg.SetValueEx(key, value, 0, wrg.REG_SZ, field)
            i = i + 1
            # close the key
            wrg.CloseKey(key)
            print(" The value is added successfully")
    except WindowsError as e:
        print(f"Error:{e.strerror}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def reg_read():
    try:
        # storing location of HKEY_CURRENT_USER
        location = wrg.HKEY_CURRENT_USER

        # store the path
        path = wrg.OpenKeyEx(location, r"Software\\")
        key = wrg.CreateKey(path,"mypath")

        # Get the number of values in the key
        num_values = wrg.QueryInfoKey(key)[1]
        for i in range(num_values):
            value_name, value_data, value_type = wrg.EnumValue(key, i)
            print(f"Value Name: {value_name}")


        print(" which values do you want to read in your key ")
        choice = input("enter the value name:  ")

        # enter the value and the data for your value
        value_1 = wrg.QueryValueEx(key, choice)
        print(value_1[0])
        wrg.CloseKey(key)
        print("The value read successfully")
    except WindowsError as e:
        print(f"Error:{e.strerror}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    print(" * Program to add and read values in the registry *")

    continue_program = True
    while continue_program:
        print(" 1.Add values in the registry \n 2.Read values in the registry \n 3. Exit")
        try:
            u_choice = int(input("Enter your choice: (1/2/3) "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            continue

        if u_choice == 1:
            try:
                reg_add()
            except Exception as e:
                print(f"Error occurred while adding values: {e}")
        elif u_choice == 2:
            try:
                reg_read()
            except Exception as e:
                print(f"Error occurred while reading values: {e}")
        elif u_choice == 3:
            continue_program = False
        else:
            print("Wrong choice")

        if continue_program:
            user_input = input("Do you want to continue? (y/n) ").lower()
            continue_program = (user_input == 'y')

    print("Exiting the program...")

if __name__ == "__main__":
    main()


