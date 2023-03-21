def create_order():
    print("What would you like to order?")
    order = int(input("Press 1 for tea, 2 for coffee, 3 for cake"))
    return order

def print_order(order):

    file = open("order.txt", "w")
    if order == 1:
        file.write("You have ordered a tea.\n")
        file.write("Your total order cost is: £2 \n")
        print("Order created!!!")
        file.close()
    elif order == 2:
        file.write("You have ordered a coffee.\n")
        file.write("the total cost of the order is: £3\n")
        print("Order created!!!")
        file.close()
    elif order == 3:
        file.write("You have ordered a cake.\n")
        file.write("the total for the order is: £5\n")
        print("Order created!!!")
        file.close()
    else:
        print("you have entered an invalid order, please try again")
        file.close()


if __name__ == '__main__':
    new_order = create_order()
    print_order(new_order)
