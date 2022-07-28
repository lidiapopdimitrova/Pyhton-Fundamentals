foil_price_per_squre_meter = 1.50
price_for_a_liter_of_paint = 14.50
price_for_a_liter_thinner_for_paint = 5
needed_foil = int(input())
needed_paint = int(input())
needed_thinner = int(input())
hours_to_complete_the_job = int(input())

sum_foil = needed_foil + 2
total_sum_foil = sum_foil * foil_price_per_squre_meter

sum_paint = needed_paint + needed_paint * 10 / 100
total_sum_paint = sum_paint * price_for_a_liter_of_paint

sum_thinner = needed_thinner * price_for_a_liter_thinner_for_paint
sum_bags = 0.40

total_sum = total_sum_paint + total_sum_foil + sum_bags + sum_thinner

sum_for_the_workers_per_hour = total_sum * 30 / 100
total_sum_for_the_workers = sum_for_the_workers_per_hour * hours_to_complete_the_job

total_sum_for_the_repainting = total_sum_for_the_workers + total_sum
str = 'Сумата на всички разходи: ' + str(total_sum_for_the_repainting)
print(str)