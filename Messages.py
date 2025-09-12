# messages.py

def instructions_message():
    print("\nInstructions: Choose pizzas from the menu below. You can finish ordering anytime by typing 'done'.")

def invalid_choice_message():
    print("Invalid choice, pick a number from the menu.")

def quantity_min_message():
    print("Quantity must be at least 1.")

def max_pizza_message(max_pizzas):
    print(f"You can only order {max_pizzas} pizzas in total.")

def invalid_number_message():
    print("Enter a valid number (1,2,3).")

def extras_added_message(extra_name):
    print(f"{extra_name} added.")

def max_reached_message(max_pizzas):
    print(f"You have reached the maximum of {max_pizzas} pizzas.")
