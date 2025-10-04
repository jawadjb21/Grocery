import pytest, csv
from project import add, remove, view, save, user

user.list = []

def test_add():
    assert add("Apple", 2) == "2 kg of Apple has been added to your list."
    assert add("Apple", 1) == "Apple already exists. Updated quantity to 3 kg."
    for item in user.list:
        assert item["name"] == "Apple"
        assert item["quantity"] == 3
    add("Chicken", 2)
    assert len(user.list) == 2
    with pytest.raises(ValueError):
        assert add("m1", 1)

def test_remove():
    assert remove("Chicken", 1) == "Updated Chicken to 1 kg."
    assert remove("Apple", 3) == "Apple has been removed from the list."
    assert remove("Orange", 2) == "Orange does not exist in your list!"

def test_view():
    assert view() == "Grocery List:\n- 1 kg of Chicken" #dont need \n as we're returning result.strip(). So, trailing backspaces removed.

def test_save():
    assert save() == "Your list has been saved!"
    with open("Grocery.csv") as file:
        reader = csv.DictReader(file)
        for line in reader:
            assert line["name"] == "Chicken"
            assert line["quantity"] == "1"