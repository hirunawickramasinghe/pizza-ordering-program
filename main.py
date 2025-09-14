# main.py
from order import get_customer_details, take_order, calculate_total
from receipt import print_receipt
from menu import DELIVERY_FEE


def main():
    while True:
        # Get customer details including payment method
        customer_info = get_customer_details()

        # Take the order
        order = take_order()

        if not order:
            print("No pizzas ordered. Exiting.")
            return

        # Calculate total with delivery fee if needed
        total = calculate_total(order, customer_info["type"], DELIVERY_FEE)

        # Show receipt
        print("\nPlease review your order:")
        print_receipt(customer_info, order, total)

        # Confirm or cancel
        confirm = input("Do you want to confirm this order? (yes/no) ").strip().lower()
        if confirm == "yes":
            print("Order confirmed!")
        else:
            print("Order cancelled.")

        # Ask for another order
        new_order = input("\nWould you like to place another order? (yes/no) ").strip().lower()
        if new_order != "yes":
            print("Thanks for ordering! See you next time! 🍕")
            break


# Run the program
main()

