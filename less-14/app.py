from Product import *
from Customer import *
from Store import *
from Manager import *

from main import main
from utils.get_instance import get_instance
from utils.get_value import get_value


def app():

    customer = Customer(100001, 3000, [], True)

    dildos_instances = [Dildo("vibrator", 75, 2, True),
                        Dildo("black dildo", 85, 3, False),
                        Dildo("double-strike", 120, 4, False)]

    dols_instances = [Dols("Blood-Rain", 250, 0, False),
                      Dols("Lara Croft", 250, 1, True),
                      Dols("Virginia 'Pepper' Potts", 350, 3, False)]

    BDSM_instances = [BDSM("handcuffs", 50, 2, True),
                      BDSM("whip", 45, 2, False),
                      BDSM("gag", 10, 5, True),
                      BDSM("blindfold", 15, 2, False),
                      BDSM("swing", 500, 3, True)]

    closers_instance = [Closer("Batman", 180, 1, True),
                        Closer("Harley Quinn", 220, 0, False)]

    categories_arr = [{"name": "dildos", "category": dildos_instances},
                      {"name": "dols", "category": dols_instances},
                      {"name": "BDSM", "category": BDSM_instances},
                      {"name": "closer", "category": closers_instance}]

    store = Store(categories_arr)

    manager = Manager(False)

    promo = 0.85

    main(customer, store, promo, manager)


if __name__ == "__main__":
    app()
