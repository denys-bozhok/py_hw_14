from utils.get_instance import get_instance
from utils.get_products_arr import get_products_arr


def main(customer, store, promo, manager):

    admin = manager

    user = get_instance(customer)

    products_arr = get_products_arr(store)

    is_running = True

    print("\nHello in our Kex-shop\n")

    while is_running:
        print("1) Admin\n2) Customer\n3) quit")

        try:
            is_admin = int(input("Are you admin or customer?\n"))
        except:
            print("Error number")

        match(is_admin):

            case 1:
                manager.isManager = True

                admin_choose = ""

                while admin.isManager:

                    print("1) read products\n2) delete products\n3) add_product\n4) redaction_product\n5) BACK")

                    try:
                        admin_choose = int(input("What you wonna do?\n"))
                    except:
                        print("Enter correct number")

                        manager.isManager = False

                    match(admin_choose):
                        case 1:
                            manager.read_products(products_arr)

                        case 2:
                            delete_title = input("Enter title of product for delete\n")

                            try:
                                products_arr = manager.delete_products(delete_title, products_arr)
                            except:
                                print("INCORRECT TITTLE")

                        case 3:
                            product_string = input("Please enter product info by coma: "
                                                   "Title, Price, Count, True/False for sale\n")

                            try:
                                manager.add_product(products_arr, product_string)
                                print("Okey!")

                            except:
                                print("ERROR!")

                        case 4:
                            product_info = input("Please enter product info by coma: "
                                                 "key, Value, New value\n")

                            try:
                                products_arr = manager.redaction_product(products_arr, product_info)
                                print("Okey!")

                            except:
                                print("Something wrong!")

                        case 5:
                            manager.isManager = False

                        case _:
                            print("Incorrect data, try again")

            case 2:
                is_customer = True

                while is_customer:

                    print("1) See categories\n2) See all products\n3) Product in sale\n"
                          "4) See your cart\n5) Bye product\n6) Back")

                    try:
                        customer_choose = int(input("What you want?\n"))
                    except:
                        print("Error Number")

                    match(customer_choose):
                        case 1:
                            store.shaw_categories()

                            try:
                                choose_category = int(input("Choose category :\n")) + - 1
                                store.shaw_product_in_category(choose_category)

                                chosen_product = input("Enter title of product to add a cart")

                                customer.add_product_to_cart(products_arr, chosen_product)

                            except:
                                print("Error number")

                        case 2:
                            store.shaw_all_product(products_arr)

                            chosen_product = input("Enter title of product to add a cart\n")

                            customer.add_product_to_cart(products_arr, chosen_product)

                        case 3:
                            store.shaw_sales_products(promo)

                            chosen_product = input("Enter title of product to add a cart\n")

                            customer.add_product_to_cart(products_arr, chosen_product)

                        case 4:
                            print("------------------\nYour cart :")

                            store.shaw_all_product(user["cart"])

                            print("------------------\n")

                        case 5:
                            customer.bye_product(promo)

                            print("U bye :")

                            store.shaw_all_product(user["cart"])

                            print(f"You have {user['balance']}$")

                        case 6:
                            is_customer = False

                        case _:
                            print("Incorrect data, try again")

            case 3:
                print("Goodbye!")
                is_running = False

            case _:
                print("Error data, try again")

