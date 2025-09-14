from menu import MENU, DELIVERY_FEE


def print_receipt(customer_info, order, total):
    print("\n----- RECEIPT -----")
    print("Customer:", customer_info['name'])
    print("Phone:", customer_info['phone'])
    if customer_info["type"] == "delivery":
        print("Address:", customer_info['address'])
        print(f"Delivery Fee: ${DELIVERY_FEE:.2f}")
    else:
        print("Pickup Order")

    # SHOW PAYMENT METHOD
    print("Payment method:", customer_info["payment"].title())

    print("\nItems Ordered:")
    for (flavour, extras), qty in order.items():
        extras_names = ", ".join([extra for extra, _ in extras])
        extras_display = f" (+{extras_names})" if extras_names else ""
        price = MENU[[k for k, v in MENU.items() if v[0] == flavour][0]][1]
        for _, price_extra in extras:
            price += price_extra
        print(f"{qty} x {flavour}{extras_display} - ${price * qty:.2f}")

    print(f"\nTOTAL: ${total:.2f}")
    print("-------------------")
    print("Thank you for ordering from Python Pizza!")
