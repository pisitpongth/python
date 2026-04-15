from inventory import Inventory


def show_info(product):
    print(
        "Product name: ",
        product.name,
        "\nCurrent stock: ",
        product.stock,
        "\n------------------------------",
    )


def main():
    product1 = Inventory("Pen", 100)

    is_loop = True

    show_info(product1)

    while is_loop:
        print("Press 1 to add item in stock", "\nPress 2 to remove item from stock")

        menu = int(input("Enter a menu: ").strip())

        if menu == 1:
            amount = int(input("How many item to add in stock: ").strip())
            product1.add_stock(amount)

            print()

            show_info(product1)
        elif menu == 2:
            amount = int(input("How many item to remove from stock: ").strip())
            product1.remove_stock(amount)

            print()

            show_info(product1)
        else:
            is_loop = False
            print("END PROGRAM")


if __name__ == "__main__":
    main()
