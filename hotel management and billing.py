HotelMenu = {
    'Chicken Biryani': 150,
    'Mutton Biryani': 250,
    'Pizza': 50,
    'Dosa': 40,
    'Burger': 60,
    'Pasta': 70,
    'Idli': 30,
    'Puri': 30,
    'Coffee': 25,
    'chai':20
}

print("Welcome to Python Hotel")
print("HotelMenu:")
for item, price in HotelMenu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# Function to add an item to the order
def add_item_to_order():
    global order_total
    item = input("Enter the name of the item you want to order: ")
    if item in HotelMenu:
        order_total += HotelMenu[item]
        print(f"Item {item} has been added to your order.")
    else:
        print(f"Sorry, {item} is not available on the menu.")

# Initial order
add_item_to_order()

# Asking if user wants to add more items
while True:
    another_order = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_order == "yes":
        add_item_to_order()
    elif another_order == "no":
        break
    else:
        print("Invalid input. Please enter Yes or No.")

# Printing the total order amount
print(f"The total amount of the order is Rs{order_total}")
