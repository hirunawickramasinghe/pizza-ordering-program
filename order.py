from menu import MENU, EXTRAS, MAX_PIZZAS
from messages import (
    instructions_message,
    invalid_choice_message,
    quantity_min_message,
    max_pizza_message,
    invalid_number_message,
    extras_added_message,
    max_reached_message
)

def take_order():
    order = {}
    total_pizzas = 0

    instructions_message()  # show instructions

    while total_pizzas < MAX_PIZZAS:
        print("\n---- MENU ----")
        for num, (flavour, price) in MENU.items():
            print(f"{num}. {flavour} - ${price:.2f}")

        choice = input("Enter pizza number (or 'done' to finish): ").strip()
        if choice.lower() == "done":
            break
        if choice not in MENU:
            invalid_choice_message()
            continue

        flavour, price = MENU[choice]

        while True:
            qty_str = input(f"How many {flavour}? ")
            try:
                qty = int(qty_str)
                if qty <= 0:
                    quantity_min_message()
                elif total_pizzas + qty > MAX_PIZZAS:
                    max_pizza_message(MAX_PIZZAS)
                else:
                    break
            except ValueError:
                invalid_number_message()

        extras_chosen = []
        print("Optional extras:")
        for num, (extra, price_extra) in EXTRAS.items():
            print(f"{num}. {extra} - ${price_extra:.2f}")
        add_extra = input("Do you want extras for this pizza? (yes/no) ").strip().lower()
        if add_extra == "yes":
            while True:
                extra_choice = input("Enter extra number (or 'done' to finish): ").strip()
                if extra_choice.lower() == "done":
                    break
                if extra_choice in EXTRAS:
                    extras_chosen.append(EXTRAS[extra_choice])
                    extras_added_message(EXTRAS[extra_choice][0])
                else:
                    invalid_choice_message()

        order[(flavour, tuple(extras_chosen))] = order.get((flavour, tuple(extras_chosen)), 0) + qty
        total_pizzas += qty

        if total_pizzas >= MAX_PIZZAS:
            max_reached_message(MAX_PIZZAS)
            break

        more = input("Do you want to add another pizza? (yes/no) ").strip().lower()
        if more == "no":
            break

    return order

def calculate_total(order, order_type, DELIVERY_FEE):
    total = 0
    for (flavour, extras), qty in order.items():
        price = MENU[[k for k,v in MENU.items() if v[0]==flavour][0]][1]
        for extra, price_extra in extras:
            price += price_extra
        total += price * qty

    if order_type == "delivery":
        total += DELIVERY_FEE

    return total
