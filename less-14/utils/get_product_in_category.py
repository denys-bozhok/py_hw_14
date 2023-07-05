def get_product_in_category(arr: list, index: int):
    product_in_category_arr = []

    for product in arr[index]:
        product_in_category_arr.append(product.__dict__)

    return product_in_category_arr
