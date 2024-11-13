import json
from user_management import authenticate_user, get_user_role
from inventory import Inventory

def main():
    print("Welcome to Inventory Management System")

    username = input("Enter username: ")
    password = input("Enter password: ")
    user = authenticate_user(username, password)

    if user:
        role = get_user_role(user)
        inventory = Inventory()

        if role == "Admin":
            print("\n--- Admin Dashboard ---")
            while True:
                print("\nOptions: [1] View All [2] Add [3] Edit [4] Delete [5] Adjust Stock [0] Exit")
                choice = input("Choose an action: ")

                if choice == '1':
                    inventory.show_all_products()
                elif choice == '2':
                    inventory.add_product()
                elif choice == '3':
                    inventory.modify_product()
                elif choice == '4':
                    inventory.remove_product()
                elif choice == '5':
                    inventory.adjust_stock()
                elif choice == '0':
                    print("Exiting Admin dashboard.")
                    break
                else:
                    print("Invalid option.")
        elif role == "User":
            print("\n--- User Dashboard ---")
            while True:
                print("\nOptions: [1] View All Products [2] Search by Name [3] Filter by Stock Level [0] Exit")
                choice = input("Choose an action: ")

                if choice == '1':
                    inventory.show_all_products()
                elif choice == '2':
                    name = input("Enter product name to search: ")
                    inventory.search_by_name(name)
                elif choice == '3':
                    inventory.filter_stock()
                elif choice == '0':
                    print("Exiting User dashboard.")
                    break
                else:
                    print("Invalid option.")
    else:
        print("Authentication failed. Invalid credentials.")

if __name__ == "__main__":
    main()
