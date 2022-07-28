annual_fee = int(input())

price_for_sneakers = annual_fee - annual_fee * 40 / 100
price_of_basketball_clothing = price_for_sneakers - price_for_sneakers * 20 / 100
price_of_basketball_ball = price_of_basketball_clothing * 25 / 100
price_of_basketball_accessories = price_of_basketball_ball * 20 / 100

total_annual_fee = annual_fee + price_of_basketball_accessories + price_of_basketball_ball \
                   + price_of_basketball_clothing + price_for_sneakers

print(total_annual_fee)
