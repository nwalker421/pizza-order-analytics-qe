from src.pizza_analyzer import normalize_toppings, get_top_combinations

def test_normalize_toppings_sorts_toppings():
    toppings = ["pepperoni", "mushrooms"]

    result = normalize_toppings(toppings)

    assert result == ("mushrooms", "pepperoni")

def test_get_top_combinations_counts_identical_combinations():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["cheese"]},

]

    result = get_top_combinations(pizza_orders)

    assert result [0] == (("mushrooms", "pepperoni"), 2)
    assert result [1] == (("cheese",), 1)
