chicken_meals = int(input())
fish_meals = int(input())
vegetarian_meals = int(input())


price_for_all_the_meals = chicken_meals * 10.35 + fish_meals * 12.40 + vegetarian_meals * 8.15
price_for_desert = price_for_all_the_meals * 20 / 100
delivery = 2.50
total_sum = price_for_all_the_meals + price_for_desert + delivery

print("Цена на поръчката: " + str(total_sum))
