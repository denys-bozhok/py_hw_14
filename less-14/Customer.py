from utils.get_product_to_cart import get_product_to_cart


class Customer:
    def __init__(self, id, balance, cart, promo):
        self.id = id
        self.balance = balance
        self.cart = cart
        self.promo = promo

    # Захар помог решить проблему:

    def add_product_to_cart(self, products_arr: list, product_title: str):

        len_of_cart = len(self.cart)

        try:
            if len_of_cart == 0:
                needed_product = list(filter(lambda product: product["title"] == product_title, products_arr))

                get_product_to_cart(needed_product, self.cart)

            elif len_of_cart != 0:
                product_in_cart = list(filter(lambda product: product["title"] == product_title, self.cart))

                if not product_in_cart:
                    needed_product = list(filter(lambda product: product["title"] == product_title, products_arr))

                    get_product_to_cart(needed_product, self.cart)

                else:
                    product_in_cart = list(filter(lambda product: product["title"] == product_title, self.cart))
                    needed_product = list(filter(lambda product: product["title"] == product_title, products_arr))

                    if needed_product[0]["count"] > 0:

                        needed_product[0]["count"] -= 1
                        product_in_cart[0]["count"] += 1

                    else:
                        print("We can delivery this product for U per 3-5 days")
        except:
            print("Error")

        # Без помощи Захара

        # for prod in self.cart:
        #     if prod["title"] == product_title and prod["count"] > 0:
        #         prod["count"] += 1
        #         return
        #
        # for product in products_arr:
        #     if product["title"] == product_title and product["count"] == 0:
        #         print("We can delivery this product per 3-5 days")
        #
        #     if product["title"] == product_title and product["count"] != 0:
        #         new_product = product.copy()
        #         new_product["count"] = 1
        #         self.cart.append(new_product)
        #
        #         product["count"] -= 1

    def bye_product(self, promo):
        sum_cart = 0

        for product in self.cart:

            if self.promo and product["withPromo"]:
                product["price"] *= promo

            sum_cart += product["price"] * product["count"]

            if sum_cart > self.balance:
                print("Get uot!!!")

            else:
                self.balance -= sum_cart

