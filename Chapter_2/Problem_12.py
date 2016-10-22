# Introduction
print("We are all very interested in Joe's financial transactions, so let's see how much profit he made!")
print("Or lost...")
# Define how much each stock costs and how many he bought
quantity = 2000
value = 40
# Create formulas to calculate how much the stocks cost and how much the broker will receive
cost_of_stocks = quantity * value
broker = cost_of_stocks * .03
# total amount paid for stocks plus cost of broker
total_paid = cost_of_stocks + broker
print("Joe paid $" + str(format(cost_of_stocks, ',.0f') + " for his initial stocks."))
print("For the first transaction, he owed his stockbroker $" + str(format(broker, ',.0f')) + " for his commission.")
print("At this point, Joe had -$" + str(format(total_paid, ',.0f')) + "in his bank account.")
# Next, create formulas to calculate how much money he made off of his sold stocks and how much he owes his stockbroker
# define how much the stocks were sold for
new_value = 42.75
# amount made off of his stocks sold
sold_stocks = quantity * new_value
# new amount owed to broker
broker_2 = sold_stocks * .03
# amount left after stocks were sold and before broker was paid
profit = sold_stocks - total_paid
# amount left after stocks were sold and broker was paid
total_made = profit - broker_2
print("He sold his stocks for $" + str(format(sold_stocks, ',.0f')) + " two weeks later.")
print("After he had done this, he had $" + str(format(profit, ',.0f')) + " left.")
print("He paid his stockbroker another $" + str(format(broker_2, ',.0f')) + " for commission.")
print("His total money left after he paid his stockbroker was $" + str(format(total_made, ',.0f')))
print("So in the end, Joe ended up making a profit!")


