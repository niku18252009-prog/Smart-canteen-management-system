# Smart College Canteen Management and Billing System
# Simple Python project using lists, loops, if-else and functions

food_items = ["Samosa", "Sandwich", "Burger", "Pizza", "Cold Drink", "Tea"]
prices = [15, 40, 60, 100, 40, 15]


def show_menu():
    print("\n----------- CANTEEN MENU -----------")
    for i in range(len(food_items)):
        print(i + 1, ".", food_items[i], "- Rs.", prices[i])
    print("------------------------------------")


def take_order():
    order_items = []
    order_qty = []

    while True:
        show_menu()
        choice = int(input("Enter item number (0 to finish): "))

        if choice == 0:
            break

        if choice >= 1 and choice <= len(food_items):
            qty = int(input("Enter quantity: "))

            if qty > 0:
                order_items.append(choice - 1)
                order_qty.append(qty)
                print("Item added to order.")
            else:
                print("Quantity should be greater than 0.")
        else:
            print("Please enter a valid item number.")

    return order_items, order_qty


def make_bill(order_items, order_qty):
    total = 0

    print("\n-------------- BILL --------------")
    print("Item\t\tQty\tAmount")
    print("----------------------------------")

    for i in range(len(order_items)):
        item_no = order_items[i]
        qty = order_qty[i]
        amount = prices[item_no] * qty
        total = total + amount

        print(food_items[item_no], "\t", qty, "\tRs.", amount)

    discount = 0

    if total >= 500:
        discount = total * 0.10
    elif total >= 300:
        discount = total * 0.05

    final_amount = total - discount

    print("----------------------------------")
    print("Total: Rs.", total)
    print("Discount: Rs.", round(discount, 2))
    print("Final Amount: Rs.", round(final_amount, 2))
    print("----------------------------------")


def main():
    print("==========================================")
    print(" SMART COLLEGE CANTEEN")
    print(" MANAGEMENT AND BILLING SYSTEM")
    print("==========================================")

    name = input("Enter customer name: ")

    order_items, order_qty = take_order()

    if len(order_items) == 0:
        print("\nNo items were ordered.")
    else:
        print("\nCustomer:", name)
        make_bill(order_items, order_qty)

    print("\nThank you for visiting the canteen!")


main()
