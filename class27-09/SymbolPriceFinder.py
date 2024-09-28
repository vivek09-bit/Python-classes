# Q.2

# stock_prices = {'AAPL': 150, 'GOOGL': 2750, 'MSFT': 300}
# symbol = input(str("Enter your symbol: "))
# price = stock_prices.get(symbol, "Not Found")
# print(price)
stocks = {'AAPL': 150, 'GOOGL': 2750, 'MSFT': 300}


def FindPrice(symbol):
    symbol = symbol.upper()
    for i in stocks:
        if symbol == i:
            i = stocks.get(symbol)
            return i
        else:
            str = "Stock not Found"
    return str


input = str(input('Enter Stock name: '))
print(FindPrice(input))