hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
#avg price of a haircut
for price in prices:
  total_price = total_price + price
print(total_price)
avg_price = total_price / len(prices)
print('Average Haircut Price: ', avg_price)
#new price
new_prices = [price -5 for price in prices]
print(new_prices)

total_revenue = 0
#total revenue
for i in range(len(hairstyles)):
  total_revenue = prices[i] * last_week[i] + total_revenue
print('Total Revenue: ', total_revenue)
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)
#haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)

