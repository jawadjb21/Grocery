import sys, csv, re

class Grocery:
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        if not self.list:
            return "Your grocery list is empty."
        result = "Grocery List:\n"
        for item in sorted(self.list, key= lambda item: item["name"]):
            result += f"- {item['quantity']} kg of {item['name']}\n"
        return result.strip()

    def add_item(self, name, quantity:int):
        if not re.search(r"^[a-zA-Z\s'-]+$", name):
            raise ValueError
            
        if quantity == 0:
            return "Insufficient amount!"

        for item in self.list:
            if item["name"] == name:
                item["quantity"] += quantity
                return f"{name} already exists. Updated quantity to {item['quantity']} kg."

        self.list.append({"name": name, "quantity": quantity})
        return f"{quantity} kg of {name} has been added to your list."

    def remove_item(self, name, quantity:int):
        if not self.list:
            return "List is currently empty!"
        
        if not re.search(r"^[a-zA-Z\s'-]+$", name):
            raise ValueError
        
        for item in self.list:
            if item["name"] == name:
                if item["quantity"] <= 0:
                    return f"You're already out of {name}."
                item["quantity"] -= quantity
                if item["quantity"] <= 0:
                    self.list.remove(item)
                    return f"{name} has been removed from the list."
                else:
                    return f"Updated {name} to {item['quantity']} kg."
        return f"{name} does not exist in your list!"

    def view_list(self):
            return str(self)

    def save_list(self):
        if not self.list:
            return "Your list is empty."
        try:
            with open("Grocery.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "quantity"])
                writer.writeheader()
                for item in sorted(self.list, key= lambda item: item["name"]):
                    writer.writerow({"name":item["name"], "quantity":item["quantity"]})
            return "Your list has been saved!"
        except Exception as e:
            return f"{e} has occured!"

user = Grocery()

def add(name, quantity):
    return user.add_item(name, quantity)

def remove(name, quantity):
    return user.remove_item(name, quantity)

def view():
    return user.view_list()

def save():
    return user.save_list()

def main():
    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Save List")
        print("5. Exit")

        action = input("Please choose an option (1-5): ").strip()

        if action == "1":
            try:
                name = input("Enter the name of the product: ").strip().title()
                quantity = int(input("Enter the quantity (kg): "))
                if re.search(r"^[a-zA-Z\s'-]+$", name):
                    print(add(name, quantity))
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input!")
        elif action == "2":
            try:
                name = input("Enter the name of the product to remove: ").strip().title()
                quantity = int(input("Enter the quantity to remove (kg): "))
                if re.search(r"^[a-zA-Z\s'-]+$", name):
                    print(remove(name, quantity))
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input!")

        elif action == "3":
            print(view())

        elif action == "4":
            print(save())

        elif action == "5":
            sys.exit("Happy Shopping!")

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()