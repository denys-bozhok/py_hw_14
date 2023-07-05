def get_product_for_sale_arr(arr: list) -> list:
    new_arr = []

    for category in arr:
        for product in category:
            if product.__dict__['withPromo']:
                new_arr.append(product.__dict__)

    return new_arr
