class Manager:
    def __init__(self, isManager=True):
        self.isManager = isManager

    def read_products(self, products_arr: list):

        if self.isManager:

            for product in products_arr:
                for key, value in product.items():
                    print(key, "-", value)

                print("--------------")

    def delete_products(self, deleting_product_name: str, products_arr: list):
        new_arr = []

        for prod in products_arr:
            if prod["title"] != deleting_product_name:
                new_arr.append(prod)

        return new_arr
        # return new_arr

    def add_product(self, products_arr: list, product_string: str):
        new_arr = product_string.split(', ')

        new_product = {
            "title": new_arr[0],
            "price": int(new_arr[1]),
            "count": int(new_arr[2]),
            "withPromo": bool(new_arr[3])
        }

        return products_arr.append(new_product)

    def redaction_product(self, products_arr: list, product_info: str):

        product_info_arr = product_info.split(", ")

        for product in products_arr:
            if product[product_info_arr[0]] == product_info_arr[1]:
                product[product_info_arr[0]] = product_info_arr[2]

        return products_arr