from utils.get_category_arr import get_category_arr
from utils.get_product_in_category import get_product_in_category
from utils.get_product_for_sale_arr import get_product_for_sale_arr


class Store:

    def __init__(self, categories):
        self.categories = categories

    def shaw_categories(self):
        i = 0
        for category in self.categories:
            for key, value in category.items():
                if key == "name":
                    print(i + 1, value.upper())
                    i += 1

    def shaw_product_in_category(self, index):
        category_arr = get_category_arr(self.categories)
        product_list = get_product_in_category(category_arr, index)

        i = 0

        for product in product_list:
            if product["count"] != 0:

                print(f"{i+1}) "
                      f"{product['title']} - "
                      f"{product['price']}$")

                if product['withPromo']:
                    print("-15% for sale rith PROMO")

            else:
                print(f"{i + 1}) {product['title']} per 3-5 days "
                      f"for {product['price']}$")

            i += 1
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def shaw_sales_products(self, promo):
        category_arr = get_category_arr(self.categories)
        product_for_sale_list = get_product_for_sale_arr(category_arr)

        i = 0

        for product in product_for_sale_list:

            if product["count"] != 0:
                print(f"{i + 1}) "
                      f"{product['title']} - "
                      f"{product['price'] * promo}$")
            i += 1

    def shaw_all_product(self, products_arr: list):
        get_category_arr(self.categories)
        i = 0

        for product in products_arr:

            if product["count"] != 0:
                print(f"{i + 1}) "
                      f"{product['title']} - "
                      f"{product['price']}$")
            i += 1