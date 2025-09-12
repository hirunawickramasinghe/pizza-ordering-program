# main.py
from customer import get_customer_details
from order import take_order, calculate_total
from receipt import print_receipt
from menu import DELIVERY_FEE

def main():
    while True:
        customer_info = get_customer_details()
        order = take_order()

        if not order:
            print("No pizzas ordered. Exiting.")
            return

        total = calculate_total(order, customer_info["type"], DELIVERY_FEE)

        print("\nPlease review your order:")
        print_receipt(customer_info, order, total)

        confirm = input("Do you want to confirm this order? (yes/no) ").strip().lower()
        if confirm == "yes":
            print("Order confirmed!")
        else:
            print("Order cancelled.")

        new_order = input("\nWould you like to place another order? (yes/no) ").strip().lower()
        if new_order != "yes":
            print("Thanks for ordering! See you next time! 🍕")
            break

main()
