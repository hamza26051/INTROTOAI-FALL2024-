class Restaurant:
    def __init__(self):
        
        self.menu_items = {}  
        self.booked_tables = []  
        self.customer_orders = []  
    def add_item_to_menu(self, item_name, price):
        """Add an item to the menu."""
        self.menu_items[item_name] = price
        print(f"Added '{item_name}' to the menu at ${price:.2f}.")

    def book_table(self, table_number):
        """Book a table."""
        if table_number not in self.booked_tables:
            self.booked_tables.append(table_number)
            print(f"Table {table_number} has been booked.")
        else:
            print(f"Table {table_number} is already booked.")

    def customer_order(self, table_number, items):
        """Take an order from a customer."""
        if table_number not in self.booked_tables:
            print(f"Table {table_number} is not booked.")
            return
        
        # Check if all items are on the menu
        invalid_items = [item for item in items if item not in self.menu_items]
        if invalid_items:
            print(f"Items not on the menu: {', '.join(invalid_items)}")
            return
        
        order = (table_number, items)
        self.customer_orders.append(order)
        print(f"Order for table {table_number} has been taken.")

    def print_menu(self):
        """Print the menu."""
        print("Menu:")
        if not self.menu_items:
            print("The menu is currently empty.")
        else:
            for item_name, price in self.menu_items.items():
                print(f"{item_name}: ${price:.2f}")

    def print_table_reservations(self):
        """Print the table reservations."""
        print("Table Reservations:")
        if not self.booked_tables:
            print("No tables are currently booked.")
        else:
            for table_number in self.booked_tables:
                print(f"Table {table_number}")

    def print_customer_orders(self):
        """Print the customer orders."""
        print("Customer Orders:")
        if not self.customer_orders:
            print("No customer orders have been placed.")
        else:
            for table_number, items in self.customer_orders:
                print(f"Table {table_number}: {', '.join(items)}")



restaurant = Restaurant()
restaurant.add_item_to_menu("Burger", 8.99)
restaurant.add_item_to_menu("Fries", 3.49)
restaurant.add_item_to_menu("Soda", 1.99)
restaurant.book_table(1)
restaurant.book_table(2)
restaurant.customer_order(1, ["Burger", "Fries"])
restaurant.customer_order(2, ["Soda"])
restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()