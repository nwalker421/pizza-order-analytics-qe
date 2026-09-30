from src.pizza_analyzer import normalize_toppings, get_top_combinations, filter_valid_orders, format_combination_result, format_ranked_results

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

def test_get_top_combinations_ranks_by_descending_frequency():
    pizza_orders = [
        {"toppings": ["cheese"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["cheese"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("cheese",), 3),
        (("pepperoni",), 2),
        (("mushrooms",), 1)

    ]

def test_get_top_combinations_ranks_ties_alphabetically():
    pizza_orders = [
        {"toppings": ["pepperoni"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["cheese"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["cheese"]} 

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("cheese",), 2),
        (("mushrooms",), 2),
        (("pepperoni",), 2)

    ]

def test_get_top_combinations_ranks_multi_topping_ties_alphabetically():
    pizza_orders = [
        {"toppings": ["pepperoni", "mushrooms"]},
        {"toppings": ["sausage", "onions"]},
        {"toppings": ["cheese", "mushrooms"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["onions", "sausage"]},
        {"toppings": ["mushrooms", "cheese"]} 

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("cheese", "mushrooms"), 2),
        (("mushrooms", "pepperoni"), 2),
        (("onions", "sausage"), 2)

    ]

def test_get_top_combinations_priorities_frequency_over_alphabetical_order():
    pizza_orders = [
        {"toppings": ["apple"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["cheese"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("pepperoni",), 3),
        (("cheese",), 2),
        (("apple",), 1)

    ]

def test_get_combinations_ranks_mixed_frequencies_and_ties():
    pizza_orders = [
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["sausage"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("pepperoni",), 3),
        (("cheese",), 2),
        (("mushrooms",), 2),
        (("sausage",), 1)

    ]

def test_get_combinations_ranks_after_normalization():
    pizza_orders = [
        {"toppings": ["Pepperoni", "Mushrooms"]},
        {"toppings": ["mushrooms", "pepperoni"]},
        {"toppings": ["PEPPERONI", "MUSHROOMS"]},
        {"toppings": ["cheese"]},
        {"toppings": ["Cheese"]},
        {"toppings": ["sausage"]}

    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("mushrooms", "pepperoni",), 3),
        (("cheese",), 2),
        (("sausage",), 1)

    ]

def test_get_combinations_returns_all_when_fewer_than_20():
    pizza_orders = [
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["cheese"]},
        {"toppings": ["mushrooms"]},
        {"toppings": ["pepperoni"]},
        {"toppings": ["sausage"]}
    ]

    result = get_top_combinations(pizza_orders)

    assert result == [
        (("pepperoni",), 3),
        (("cheese",), 2),
        (("mushrooms",), 2),
        (("sausage",), 1),
    ]

def test_get_combination_returns_top_20_from_21_unique():
    pizza_orders = [
        {"toppings": [f"topping{i:02d}"]}
        for i in range(1, 22)

    ]

    result = get_top_combinations(pizza_orders)

    assert len(result) == 20
    assert (("topping20",), 1) in result
    assert (("toppings21",), 1) not in result

def test_get_combination_returnss_all_19_unique():
    pizza_orders = [
        {"toppings": [f"topping{i:02d}"]}
        for i in range(1, 20)

    ]

    result = get_top_combinations(pizza_orders)

    assert len(result) == 19
    assert (("topping01",), 1) in result
    assert (("toppings19",), 1) not in result
    assert (("toppings20",), 1) not in result

#TC-029 Apply default result time of 20
def test_get_combinations_applies_default_limit_of_20():
    pizza_orders = [
        {"toppings":[f"topping{i:02d}"]}
        for i in range(1, 26)

    ]

#Call function without supplying a limit
    result = get_top_combinations(pizza_orders)

#Verify the default maximum is 20
    assert len(result) == 20


#TC-030 Select correct Top 20 from larger dataset
def test_get_combinations_select_correct_top_20_from_50():
    pizza_orders = []

    #Create 50 unique combinations with known frequencies
    #topping01 appears once, topping02 twice,...topping 50 fifty times
    for i in range(1, 51):
        for _ in range(i):
            pizza_orders.append({"toppings": [f"topping{i:02d}"]})

    #Reverse the source order so results cannot depend on encounter order
    pizza_orders.reverse()

    result = get_top_combinations(pizza_orders)

    #Verify only 20 combinations are returned
    assert len(result) == 20

    #The 20 highest frequency combinations must be topping50 through topping31
    expected = [
        ((f"topping{i:02d}",), i)
        for i in range(50, 30, -1)

]

    assert result == expected


#TC-031 Preserve ranking within Top-20 results
def test_get_combinations_preserve_ranking_within_top_20():
    pizza_orders =[]

    #Create 25 unique combinations with known frequencies
    #topping01 appears once, topping02 twice,...topping25 twenty-five times
    for i in range(1, 26):
        for _ in range(i):
            pizza_orders.append({"toppings": [f"topping{i:02d}"]})

    result = get_top_combinations(pizza_orders)

    #Expected ranking before limiting
    #topping25, topping24,...topping06
    expected_top_20 = [
        ((f"topping{i:02d}",), i)
        for i in range(25, 5, -1)

    ]

    #Verify the top-20 limit preserves the established ranking
    assert result == expected_top_20

#TC-032 Return one combination when only one exits
def test_get_combinations_returns_one_when_only_one_exits():
    pizza_orders = [
        {"toppings": ["pepperoni"]}
        for _ in range(10)

    ]

    result = get_top_combinations(pizza_orders)

    #Verify exactly one combination is returned
    assert len(result) == 1

    #Verify the single combination and the frequency is correct
    assert result == [
        (("pepperoni",), 10)

    ]


#TC-033 Return empty result when no valid combinations exist
def test_get_combinations_return_empty_results_when_no_valid_combinations_exist():
    pizza_orders = []

    result = get_top_combinations(pizza_orders)

    #Verify no combinations are returned
    assert result == []

    #Verify the result contains zero items
    assert len(result) == 0

#TC-034 Verify custom limit less than 20
def test_get_combinations_respects_custom_limit_less_than_20():
    pizza_orders = []
   
    #Create 10 unique combinations with known frequencies
    for i in range(1, 11):
        for _ in range(i):
            pizza_orders.append({"toppings": [f"topping{i:02d}"]})

    result = get_top_combinations(pizza_orders, limit=5)

    #Verify the custom limit returns exactly 5 combinations.
    assert len(result) == 5

    #Verify the five highest-frequency combinations are returned in rank order.
    assert result == [
        (("topping10",), 10),
        (("topping09",), 9),
        (("topping08",), 8),
        (("topping07",), 7),
        (("topping06",), 6),

    ]

#TC-035 Display complete topping combination
def test_format_combination_result_displays_complete_topping_combination():
    combination = ("mushrooms", "pepperoni")
    count = 3

    result = format_combination_result(combination, count)

    assert result == "mushrooms, pepperoni - 3"

#TC-036 Display calculated order frequency
def test_format_combination_result_displays_calculated_order_frequency():
    combination = ("mushrooms", "pepperoni")
    count = 27

    result = format_combination_result(combination, count)

    assert result == "mushrooms, pepperoni - 27"

#TC-037 Display sequential rankings beginning at 1
def test_format_combination_result_displays_sequential_rankings():
    combinations = [
        (("pepperoni",), 27),
        (("cheese",), 24),
        (("mushrooms",), 19),

    ]

    results = [
        format_combination_result(combination, count, rank)
        for rank, (combination, count) in enumerate(combinations, start=1)

    ]

    assert results == [
        "1. pepperoni - 27",
        "2. cheese - 24",
        "3. mushrooms - 19",

    ]

#TC-038 Display maximum 20 results when 20 or more qualify
def test_format_ranked_results_display_maximum_20_results():
    results = [
        ((f"topping{i:02d}",), i)    
        for i in range(25, 0, -1)

    ]

    formatted_results = format_ranked_results(results)

    assert len(formatted_results) == 20

#TC-039 Display fewer than 20 results when fewer are available
def test_format_ranked_results_display_all_when_fewer_than_20():
    results = [
        ((f"topping{i:02d}",), i)
        for i in range(7, 0, -1)

    ]

    formatted_results = format_ranked_results(results)

    assert len(formatted_results) == 7
    assert formatted_results[0] == "1. topping07 - 7"
    assert formatted_results[-1] == "7. topping01 - 1"

#TC-040 Preserve deterministic order in displayed results
def test_format_ranked_results_preserves_deterministic_order():
    results = [
        (("cheese",), 5),
        (("mushrooms",), 5),
        (("pepperoni",), 5,

    ]

    formatted_results = format_ranked_results(results)

    assert formatted_results == [
        "1. cheese - 5",
        "2. mushrooms - 5",
        "3. pepperoni - 5",

    ]
    
    
