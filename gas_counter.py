dist = 3136
fuel = 8.7
price = 1.32

price_for_hund = fuel*price
price_for_one = price_for_hund/100

print('Results: ')

price_total = 0.0
for i in range(0,dist):
    price_total +=price_for_one
    if i == 1000:
        print(f'Fuel price for {i}km is {round(price_total,2)} leva!')
    if i == 2500:
        print(f'Fuel price for {i}km is {round(price_total,2)} leva!')
    if i == 5000:
        print(f'Fuel price for {i}km is {round(price_total,2)} leva!')

print(f'Fuel price for {dist}km is {round(price_total,2)} leva!')