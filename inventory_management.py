from abc import ABC, abstractmethod

# Base class representing a generic inventory item
class InventoryItem(ABC):
    def __init__(self, item_id, name, quantity, price):
        self.__item_id = item_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    # Encapsulation: Using getters and setters to manage access to attributes
    def get_item_id(self):
        return self.__item_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    # Abstract method to be implemented by subclasses
    @abstractmethod
    def calculate_total_value(self):
        pass

    def __str__(self):
        return f"ID: {self.__item_id}, Name: {self.__name}, Quantity: {self.__quantity}, Price: {self.__price}"

# Subclass for a specific type of inventory item (e.g., electronics)
class ElectronicsItem(InventoryItem):
    def __init__(self, item_id, name, quantity, price, warranty_period):
        super().__init__(item_id, name, quantity, price)
        self.__warranty_period = warranty_period

    def get_warranty_period(self):
        return self.__warranty_period

    def set_warranty_period(self, warranty_period):
        self.__warranty_period = warranty_period

    def calculate_total_value(self):
        return self.get_quantity() * self.get_price()

    def __str__(self):
        return super().__str__() + f", Warranty Period: {self.__warranty_period} years"

# Subclass for another type of inventory item (e.g., consumables)
class ConsumableItem(InventoryItem):
    def __init__(self, item_id, name, quantity, price, expiration_date):
        super().__init__(item_id, name, quantity, price)
        self.__expiration_date = expiration_date

    def get_expiration_date(self):
        return self.__expiration_date

    def set_expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    def calculate_total_value(self):
        return self.get_quantity() * self.get_price()

    def __str__(self):
        return super().__str__() + f", Expiration Date: {self.__expiration_date}"
    
    
# class sales:
#     def __init__(self):
#         self.items = {}

# Class representing the inventory, holding a collection of items
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        item_id = item.get_item_id()
        if item_id in self.items:
            print(f"Item with ID {item_id} already exists.")    
        else:
            self.items[item_id] = item
            print(f"Item {item.get_name()} added to inventory.")

    def update_item(self, item_id, **kwargs):
        if item_id in self.items:
            item = self.items[item_id]
            for key, value in kwargs.items():
                if key == 'name':
                    item.set_name(value)
                elif key == 'quantity':
                    item.set_quantity(value)
                elif key == 'price':
                    item.set_price(value)
                elif isinstance(item, ElectronicsItem) and key == 'warranty_period':
                    item.set_warranty_period(value)
                elif isinstance(item, ConsumableItem) and key == 'expiration_date':
                    item.set_expiration_date(value)
            print(f"Item {item_id} updated.")
        else:
            print(f"Item with ID {item_id} not found.")

    def view_item(self, item_id):
        if item_id in self.items:
            print(self.items[item_id])
        else:
            print(f"Item with ID {item_id} not found.")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item {item_id} deleted.")
        else:
            print(f"Item with ID {item_id} not found.")

    def view_inventory(self):
        if self.items:
            print("Current Inventory:")
            for item in self.items.values():
                print(item)
        else:
            print("Inventory is empty.")

def main():
    inventory = Inventory()

    while True:
        print('\nWELCOME TO VASANTH & C0')
        print("\nInventory Management System")
        print("1. Add Electronics Item")
        print("2. Add Consumable Item")
        print("3. Update Item")
        print("4. View Item")
        print("5. Delete Item")
        print("6. View Inventory")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            warranty_period = int(input("Enter warranty period (in years): "))
            item = ElectronicsItem(item_id, name, quantity, price, warranty_period)
            inventory.add_item(item)

        elif choice == '2':
            item_id = input("Enter item ID: ")
            name = input("Enter item name: ")
            quantity = int(input("Enter item quantity: "))
            price = float(input("Enter item price: "))
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            item = ConsumableItem(item_id, name, quantity, price, expiration_date)
            inventory.add_item(item)

        elif choice == '3':
            item_id = input("Enter item ID to update: ")
            updates = {}
            updates['name'] = input("Enter new name (leave blank to keep current): ") or None
            updates['quantity'] = input("Enter new quantity (leave blank to keep current): ") or None
            updates['price'] = input("Enter new price (leave blank to keep current): ") or None

            if isinstance(inventory.items.get(item_id), ElectronicsItem):
                updates['warranty_period'] = input("Enter new warranty period (leave blank to keep current): ") or None
            elif isinstance(inventory.items.get(item_id), ConsumableItem):
                updates['expiration_date'] = input("Enter new expiration date (leave blank to keep current): ") or None

            # Filter out None values from updates
            updates = {k: v for k, v in updates.items() if v is not None}
            inventory.update_item(item_id, **updates)

        elif choice == '4':
            item_id = input("Enter item ID to view: ")
            inventory.view_item(item_id)

        elif choice == '5':
            item_id = input("Enter item ID to delete: ")
            inventory.delete_item(item_id)

        elif choice == '6':
            inventory.view_inventory()

        elif choice == '7':
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
