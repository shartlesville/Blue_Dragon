# topping list:
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives','anchovies','mushrooms']
prices = [2.00, 6.00, 1.00, 3.00, 2.00, 7.00, 2.00]

# $2 pizzas
num_two_dollar_slices = prices.count(2.00)
print(num_two_dollar_slices)

# number of pizza types
num_pizzas = len(toppings)

print('We sell', num_pizzas, 'different kinds of pizza!')
# pizza and prices
pizza_and_prices = list(zip(prices, toppings))

# sort pizza_and_prices
pizza_and_prices.sort()
print(pizza_and_prices)

# least expensive
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)

# most expensive
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)

#out of anchovies
pizza_and_prices.pop()
print(pizza_and_prices)

# new topping
pizza_and_prices.insert(4, (2.50, 'peppers'))
print(pizza_and_prices)

# 3 least expensive
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
