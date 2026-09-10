# Pizza Order Analytics Requirements

##Business Requirement

The application shall analyze pizza order data and identify the 20 most frequently ordered unique topping combinations.

##Functional Requirements
1. The application shall load pizza order data from a JSON data source.
2. The application shall read the toppings associated with each pizza order.
3. The application shall normalize topping combinations so that topping order does not affect grouping.
4. The application shall group identical topping combinations.
5. The application shall calculate the number of orders for each unique topping conbination.
6. The application shall sort topping combinations from highest to lowest frequency.
7. The application shall return the top 20 most frequently ordered topping combinations.
8. The output shall include:
- Rank
- Topping combination
- Order frequency
