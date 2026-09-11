"""Core pizza order analysis function."""

from collections import Counter

def normalize_toppings(toppings): return tuple(sorted(toppings))

def get_top_combinations(pizza_orders, limit=20):
  combinations = (normalize_toppings(pizza["toppings"]) for pizza in pizza_orders]
  frequency = Counter(combinations)
  return frequency.most_common(limit)
