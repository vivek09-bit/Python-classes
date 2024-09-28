# 1. Portfolio Allocation Analysis
# Problem:
# Given two dictionaries—one representing the number of shares owned for each stock and another representing the current price of each stock—write a Python function to calculate the total value of the portfolio.

portfolio = {'AAPL': 50, 'GOOGL': 10, 'MSFT': 30}
prices = {'AAPL': 150, 'GOOGL': 2750, 'MSFT': 300}

def TotalValue(portfolio, prices):
    TotalPrice = dict()
    for i in portfolio:
        TotalPrice.update({i :portfolio.get(i)* prices.get(i)})
    # print()
    return TotalPrice

Total = TotalValue(portfolio,prices)
print(Total)