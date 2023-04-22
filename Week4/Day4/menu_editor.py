from xp1_week4 import MenuItem
class MenuEditor:
    def __init__(self):
        self.menu = []

    def add_item_to_menu(self):
        name = input("Enter the name of the item: ")
        price = input("And the price of the item: ")
        item = MenuItem(name, price)
        self.menu.append(item)
        print("Item added successfully.")

    def remove_item_from_menu(self):
        name = input("Enter the name of the item to remove: ")
        for item in self.menu:
            if item.name == name:
                self.menu.remove(item)
                print("Item removed successfully.")
                return
        print("Error: Item not found.")

    def show_user_menu(self):
        choice = input("Enter your choice: ")
        while choice not in ['1','2','3','4','5']:
            print("\nMenu Editor:")
            print("1. Load Manager")
            print("2. Add Item to Menu")
            print("3. Remove Item from Menu")
            print("4. Show Restaurant Menu")
            print("5. Exit")
        if choice == '1':
            self.load_manager()
        elif choice == '2':
                self.add_item_to_menu()
        elif choice == '3':
                self.remove_item_from_menu()
        elif choice == '4':
                self.show_restaurant_menu()
        elif choice == '5':
                self.show_restaurant_menu()
                exit()
        else:
                print("Invalid choice.")
                self.show_user_menu()

    def show_restaurant_menu(self):
        print("\nRestaurant Menu:")
        for item in self.menu:
            item.display()



MenuEditor.show_user_menu(2)



