# customer.py
def get_customer_details():
    print("\nWelcome to Python Pizza! Please enter your details to start your order.")
    name = input("Enter your name: ").strip().title()
    while name == "":
        print("Name cannot be blank.")
        name = input("Enter your name: ").strip().title()

    phone = input("Enter your phone number: ").strip()
    while phone == "" or not all(c.isdigit() or c in " -+" for c in phone):
        print("Phone number can only have numbers, spaces, dashes or + sign.")
        phone = input("Enter your phone number: ").strip()

    order_type = input("Pickup or Delivery? ").strip().lower()
    while order_type not in ["pickup", "delivery"]:
        print("Please type 'pickup' or 'delivery'")
        order_type = input("Pickup or Delivery? ").strip().lower()

    address = ""
    if order_type == "delivery":
        address = input("Enter your delivery address: ").strip()
        while address == "":
            print("Address cannot be blank.")
            address = input("Enter your delivery address: ").strip()

    return {"name": name, "phone": phone, "type": order_type, "address": address}

