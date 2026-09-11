"""Core pizza order analysis function."""

from collections import Counter

def normalize_toppings(toppings):
  """Return toppings in a consistent order."""
  return tuple(sorted(toppings))

def get_top_combinations(pizza_orders, limit=20):
  """Return the most frequently ordered pizza topping combinations."""

  combinations = [
    normalize_toppings(pizza["toppings"])
    for pizza in pizza_orders

]

    frequently = Counter(combinations)

    return frequency.most_common(limits)
