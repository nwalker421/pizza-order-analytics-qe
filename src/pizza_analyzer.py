"""Core pizza order analysis function."""

from collections import Counter

def normalize_toppings(toppings):
    normalized = [topping.strip().lower() for topping in toppings]
    return tuple(sorted(normalized))

def get_top_combinations(pizza_orders, limit=20):
    valid_orders = filter_valid_orders(pizza_orders)
    combinations = [normalize_toppings(pizza["toppings"]) for pizza in valid_orders]
    frequency = Counter(combinations)
    return frequency.most_common(limit)


def filter_valid_orders(pizza_orders):
    valid_orders = []

    for pizza in pizza_orders:
        if "toppings" not in pizza:
          continue

        toppings = pizza["toppings"]

        if not isinstance(toppings, list):
          continue
  
        if len(toppings) ==0:
          continue

        valid_orders.append(pizza)


    return valid_orders

def test_get_top_combinations_counts_single_occurence():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [(("mushrooms", "pepperoni"), 1)]


    
