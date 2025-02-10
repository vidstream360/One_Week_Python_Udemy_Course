#example of a nested dict

prices = {
    "arugala" : 1.15,
    "basil" : 2.54,
    "blackberries" : 4.93,
    "blueberries" : 2.88,
    "coconut" : 7.15,
    "fennel" : 3.36,
}

produce = {
    "arugala": {
        "price": 1.15,
        "qty": 61,
        "organic": True,
        "producer": "Blue Kitty Farms"
    },
    "coconut": {
        "price": 7.15,
        "qty": 12,
        "organic": False,
        "producer": "Tropical Dream Farm"
    }
}
