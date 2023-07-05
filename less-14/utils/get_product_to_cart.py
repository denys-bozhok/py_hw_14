def get_product_to_cart(needed_product: list, cart):
    if needed_product[0]["count"] > 0:
        needed_product[0]["count"] -= 1

        new_product = needed_product[0].copy()
        new_product["count"] = 1

        cart.append(new_product)

    else:
        print("We can delivery this product for I per 3-5 days")
