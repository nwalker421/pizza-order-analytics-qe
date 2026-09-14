"""Core pizza order analysis function."""

from collections import Counter

def normalize_toppings(toppings): return tuple(sorted(toppings))

def get_top_combinations(pizza_orders, limit=20):
  combinations = [normalize_toppings(pizza["toppings"]) for pizza in pizza_orders]
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

        valid_orders.apped(pizza)

    return valid_orders
