class Product:
    def __init__(self, title, price, count):
        self.title = title
        self.price = price
        self.count = count


class Dildo(Product):
    def __init__(self, title, price, count=0, withPromo=False):
        super().__init__(title, price, count)
        self.withPromo = withPromo


class Dols(Product):
    def __init__(self, title, price, count=0, withPromo=False):
        super().__init__(title, price, count)
        self.withPromo = withPromo


class BDSM(Product):
    def __init__(self, title, price, count=0, withPromo=False):
        super().__init__(title, price, count)
        self.withPromo = withPromo


class Closer(Product):
    def __init__(self, title, price, count=0, withPromo=False):
        super().__init__(title, price, count)
        self.withPromo = withPromo
