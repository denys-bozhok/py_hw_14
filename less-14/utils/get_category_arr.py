def get_category_arr(arr: list) -> list:
    new_arr = []

    for category in arr:
        for key, value in category.items():
            if key == "category":
                new_arr.append(value)
    return new_arr
