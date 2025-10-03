from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox)
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

class GroceryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.grocery = Grocery()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Grocery List Manager")
        self.setGeometry(100, 100, 400, 400)

        # Layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Input Fields
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        self.quantity_label = QLabel("Quantity (kg):")
        self.quantity_input = QLineEdit()

        input_layout.addWidget(self.name_label)
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.quantity_label)
        input_layout.addWidget(self.quantity_input)

        # Buttons
        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.add_item)

        self.remove_button = QPushButton("Remove Item")
        self.remove_button.clicked.connect(self.remove_item)

        self.view_button = QPushButton("View List")
        self.view_button.clicked.connect(self.view_list)

        self.save_button = QPushButton("Save List")
        self.save_button.clicked.connect(self.save_list)

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.remove_button)
        button_layout.addWidget(self.view_button)
        button_layout.addWidget(self.save_button)

        # Output Area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Add layouts to main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.output_text)

        self.setLayout(main_layout)

    def add_item(self):
        name = self.name_input.text().strip().title()
        try:
            quantity = int(self.quantity_input.text())
            message = self.grocery.add_item(name, quantity)
            QMessageBox.information(self, "Info", message)
            self.clear_inputs()
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input! Please enter a valid name and quantity.")

    def remove_item(self):
        name = self.name_input.text().strip().title()
        try:
            quantity = int(self.quantity_input.text())
            message = self.grocery.remove_item(name, quantity)
            QMessageBox.information(self, "Info", message)
            self.clear_inputs()
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid input! Please enter a valid name and quantity.")

    def view_list(self):
        self.output_text.setText(self.grocery.view_list())

    def save_list(self):
        message = self.grocery.save_list()
        QMessageBox.information(self, "Info", message)

    def clear_inputs(self):
        self.name_input.clear()
        self.quantity_input.clear()

if __name__ == "__main__":
    app = QApplication([])
    window = GroceryApp()
    window.show()
    app.exec_()
