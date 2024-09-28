stocks = {'AAPL': 150, 'GOOGL': 2750, 'MSFT': 300}


def FindPrice(symbol):
    symbol = symbol.upper()
    return stocks.get(symbol, 'Stock not found')
   

input = str(input('Enter Stock name: '))
print(FindPrice(input))