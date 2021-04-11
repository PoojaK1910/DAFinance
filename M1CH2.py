# Create and print list names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']
print(names)

# Create and print list prices
prices = [159.54, 37.13, 71.17]
print(prices)

# Print the first item in names
print(names[0])

# Print the second item in names
print(names[1])

# Print the last element in prices
print(prices[-1])

# names
names = ['Apple Inc', 'Coca-Cola', 'Walmart']

# Use slicing on list names
names_subset = names[1:3]
print(names_subset)

# prices
prices = [159.54, 37.13, 71.17]

# Use extended slicing on the list prices
prices_subset = prices[:2]
print(prices_subset)

# Create and print the nested list stocks
stocks = [names, prices]
print(stocks)

# Use list indexing to obtain the list of prices
print(stocks[1])

# Use indexing to obtain company name Coca-Cola
print(stocks[0][1])

# Use indexing to obtain 71.17
print(stocks[1][2])

