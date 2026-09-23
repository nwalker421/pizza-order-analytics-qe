from src.pizza_analyzer import normalize_toppings, get_top_combinations, filter_valid_orders

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

def test_filter_valid_orders_accepts_valid_orders():
    pizza_orders = [
        {"toppings": ["pepperoni",]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["cheese"]},
    ]

    result = filter_valid_orders(pizza_orders)

    assert result == pizza_orders

def test_filter_valid_orders_accepts_single_order():
    pizza_orders = [
        {"toppings": ["pepperoni"]}

    ]

    result = filter_valid_orders(pizza_orders)

    assert result == pizza_orders

def test_filter_valid_orders_excludes_empty_toppings():
    pizza_orders = [
        {"toppings": []}

    ]

    result = filter_valid_orders(pizza_orders)

    assert result == []

def test_filter_valid_orders_excludes_missing_toppings():
    pizza_orders = [
        {"orderId": 1001}

    ]

    result = filter_valid_orders(pizza_orders)

    assert result == []

def test_filter_valid_orders_excludes_invalid_toppings_type():
    pizza_orders = [
        {"toppings": "pepperoni"}

    ]

    result = filter_valid_orders(pizza_orders)

    assert result == []


def test_filter_valid_orders_processes_mixed_dataset():
    pizza_orders = [
        {"toppings": ["pepperoni"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"orderId": 1001},
        {"toppings": ["cheese"]},
        {"toppings": "sausage"},
        {"toppings": ["onions"]},

    ]

    result = filter_valid_orders(pizza_orders)

    assert result == [
        {"toppings": ["pepperoni"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["onions"]},

    ]

def test_normalize_toppings_handles_different_order():
    first = ["pepperoni", "mushrooms"]
    second = ["mushrooms", "pepperoni"]

    result_one = normalize_toppings(first)
    result_two = normalize_toppings(second)

    assert result_one == result_two

def test_normalize_toppings_preserves_single_topping():
    toppings = ["cheese"]

    result = normalize_toppings(toppings)
    assert result == ("cheese",)

def test_normalize_toppings_preserves_all_toppings():
    toppings = ["pepperoni", "mushrooms", "onions"]

    result = normalize_toppings(toppings)

    assert result == ("mushrooms", "onions", "pepperoni")

def test_normalize_toppings_handles_multiple_sequences():
    first = ["pepperoni", "mushrooms", "onions"]
    second = ["onions", "pepperoni", "mushrooms"]
    third = ["mushrooms", "onions", "pepperoni"]

    result_one = normalize_toppings(first)
    result_two = normalize_toppings(second)
    result_three = normalize_toppings(third)

    assert result_one == result_two == result_three

def test_normalize_toppings_preserves_duplicate_toppings():
    toppings = ["pepperoni", "pepperoni", "mushrooms"]

    result = normalize_toppings(toppings)

    assert result == ("mushrooms", "pepperoni", "pepperoni")

def test_normalize_toppings_handles_case_and_whitespace():
    first = ["Pepperoni", "MUSHROOMS"]
    second = ["pepperoni", "mushrooms"]

    result_one = normalize_toppings(first)
    result_two = normalize_toppings(second)

    assert result_one == result_two
    assert result_one == ("mushrooms", "pepperoni")

def test_get_top_combinations_counts_single_occurence():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [(("mushrooms", "pepperoni"), 1)]


def test_get_top_combinations_counts_multiple_occurenes():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["pepperoni", "mushrooms"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [(("mushrooms", "pepperoni"), 3)]

def test_get_top_combinations_counts_distinct_combinations():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]},
        {"toppings": ["cheese"]},
        {"toppings": ["pepperoni", "pepperoni"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["cheese", "cheese"]},
        {"toppings": ["onions"]},
        {"toppings": ["cheese"]},
        {"toppings": ["pepperoni", "mushrooms"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert dict(result) == {
        ("mushrooms", "pepperoni"): 3,
        ("cheese",): 2,
        ("pepperoni", "pepperoni"): 1,
        ("cheese", "cheese"): 1,
        ("onions",): 1
        
    }
            
def test_get_top_combinations_counts_normalized_variations():
    pizza_orders = [
        {"toppings": ["Pepperoni", "Mushrooms"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["PEPPERONI", "MUSHROOMS"]}

    ]

    result = get_top_combinations(pizza_orders)
    assert result == [(("mushrooms", "pepperoni"), 3)]


def test_get_top_combinations_preserves_duplicate_toppings():
    pizza_orders = [
        {"toppings": ["pepperoni", "pepperoni"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["pepperoni", "pepperoni"]}

    ]

    result = get_top_combinations(pizza_orders)
    assert result == [
        (("pepperoni", "pepperoni"), 2),
        (("pepperoni", ), 1)
        
    ]

def test_get_top_combinations_with_one_valid_order():
    pizza_orders = [
        {"toppings": ["sausage", "onions"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [(("onions", "sausage"), 1)]

def test_get_top_combinations_excludes_invalid_orders():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {},
        {"toppings": "cheese"},
        {"toppings": []}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [(("mushrooms", "pepperoni"), 2)]

def test_get_top_combinations_returns_all_when_fewer_than_20():
    pizza_orders = [
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["sausage"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("pepperoni",), 2),
        (("cheese",), 2),
        (("mushrooms",), 1),
        (("sausage",), 1)

    ]
    
            
            
