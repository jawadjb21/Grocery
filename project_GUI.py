import tkinter as tk
from tkinter import messagebox
import csv
import re

class Grocery:
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        if not self.list:
            return "Your grocery list is empty."
        result = "Grocery List:\n"
        for item in sorted(self.list, key=lambda item: item["name"]):
            result += f"- {item['quantity']} kg of {item['name']}\n"
        return result.strip()

    def add_item(self, name, quantity: int):
        if not re.search(r"^[a-zA-Z\s'-]+$", name):
            raise ValueError("Invalid name format")

        if quantity <= 0:
            return "Quantity must be greater than 0!"

        for item in self.list:
            if item["name"] == name:
                item["quantity"] += quantity
                return f"{name} already exists. Updated quantity to {item['quantity']} kg."

        self.list.append({"name": name, "quantity": quantity})
        return f"{quantity} kg of {name} has been added to your list."

    def remove_item(self, name, quantity: int):
        if not self.list:
            return "List is currently empty!"

        if not re.search(r"^[a-zA-Z\s'-]+$", name):
            raise ValueError("Invalid name format")

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
                for item in sorted(self.list, key=lambda item: item["name"]):
                    writer.writerow({"name": item["name"], "quantity": item["quantity"]})
            return "Your list has been saved!"
        except Exception as e:
            return f"Error: {e}" 

# Tkinter GUI Application
class GroceryApp:
    def __init__(self, root):
        self.grocery = Grocery()
        self.root = root
        self.root.title("Grocery List Manager")

        # Input Frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.input_frame, text="Quantity (kg):").grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(self.input_frame)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Item", command=self.add_item)
        self.add_button.grid(row=0, column=0, padx=10)

        self.remove_button = tk.Button(self.button_frame, text="Remove Item", command=self.remove_item)
        self.remove_button.grid(row=0, column=1, padx=10)

        self.view_button = tk.Button(self.button_frame, text="View List", command=self.view_list)
        self.view_button.grid(row=0, column=2, padx=10)

        self.save_button = tk.Button(self.button_frame, text="Save List", command=self.save_list)
        self.save_button.grid(row=0, column=3, padx=10)

        # Output Frame
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(pady=10)

        self.output_text = tk.Text(self.output_frame, height=15, width=50, state=tk.DISABLED)
        self.output_text.pack()

    def add_item(self):
        name = self.name_entry.get().strip().title()
        try:
            quantity = int(self.quantity_entry.get())
            message = self.grocery.add_item(name, quantity)
            messagebox.showinfo("Info", message)
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid name and quantity.")

    def remove_item(self):
        name = self.name_entry.get().strip().title()
        try:
            quantity = int(self.quantity_entry.get())
            message = self.grocery.remove_item(name, quantity)
            messagebox.showinfo("Info", message)
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid name and quantity.")

    def view_list(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, self.grocery.view_list())
        self.output_text.config(state=tk.DISABLED)

    def save_list(self):
        message = self.grocery.save_list()
        messagebox.showinfo("Info", message)

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()