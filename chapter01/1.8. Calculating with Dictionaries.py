
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))

prices_sorted = sorted(zip(prices.values(), prices.keys()))

#zip() creates an iterator that can only be consumed once.

prices_and_names = list(zip(prices.values(), prices.keys()))

min(prices, key=lambda k: prices[k])
max(prices, key=lambda k: prices[k])

min_value = prices[min(prices, key=lambda k: prices[k])]

print (min_value)