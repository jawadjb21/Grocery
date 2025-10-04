# 🛒 Grocery List Manager

A simple Python command-line application to manage your grocery list.
This project demonstrates object-oriented programming, input validation using regular expressions, file handling with CSV, and automated testing with `pytest`.

---

## 🚀 Features

* Add items to your grocery list with quantities
* Remove items or update quantities
* View your list in alphabetical order
* Save your list to a CSV file (`Grocery.csv`)
* Input validation using regex (only allows valid names)
* Tested with `pytest`

---

## 📂 Project Structure

```
grocery-list/
├── grocery/
│   └── grocery.py         # Main program logic
├── tests/
│   └── test_grocery.py    # Unit tests
├── Grocery.csv            # Saved grocery list (generated after saving)
├── README.md              # Project documentation
└── requirements.txt       # Dependencies (pytest)
```

---

## 🛠️ Installation & Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/grocery-list.git
   cd grocery-list
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate    # On macOS/Linux
   venv\Scripts\activate       # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python grocery/grocery.py
   ```

---

## 🧪 Running Tests

This project uses `pytest` for testing.

```bash
pytest
```

---

## 📊 Example

```
Options:
1. Add Item
2. Remove Item
3. View List
4. Save List
5. Exit

Please choose an option (1-5): 1
Enter the name of the product: Apple
Enter the quantity (kg): 2
2 kg of Apple has been added to your list.
```

---

## ✅ Future Improvements

* Support fractional quantities (e.g., 1.5 kg)
* Persist grocery list by **loading from CSV** on startup
* Add colored CLI output for better UX

---

## 📄 License

This project is licensed under the MIT License – feel free to use and modify.
