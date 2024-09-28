stocks = {'AAPL': 150, 'GOOGL': 2750, 'MSFT': 300}


def FindPrice(symbol):
    symbol = symbol.upper()
    for i in stocks:
        price = 0
        if symbol == i:
            i = stocks.get(symbol)
            return i
        else:
            str = "Stock not Found"
    return str


input = str(input('Enter Stock name: '))
print(FindPrice(input))