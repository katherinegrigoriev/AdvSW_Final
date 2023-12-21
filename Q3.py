f = open("sample_AAPL.txt", "r")
listItems = f.read().splitlines()
appleprices=listItems
for i in range(0, len(listItems)):
 appleprices[i] = float(listItems[i])

def buy_and_sell(stock_price):
    stock_price = appleprices
    max_profit_val, current_max_val = 0, 0
    for price in reversed(stock_price):
        current_max_val = max(current_max_val, price)
        potential_profit = current_max_val - price
        max_profit_val = max(potential_profit, max_profit_val)
        
    return max_profit_val


print(f"The largest possible profit from buying and selling one share is: $ " + str(buy_and_sell(range(0, len(appleprices)+1))))