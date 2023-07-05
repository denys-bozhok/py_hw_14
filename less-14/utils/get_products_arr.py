def get_products_arr(store):

    products_arr = []
    for el in store.categories:
        for product in el["category"]:
            products_arr.append(product.__dict__)

    return products_arr
