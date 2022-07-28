number_of_pages = int(input())
pages_to_read_in_an_hour = int(input())
number_days_for_reading = int(input())
time_to_read_the_book = number_of_pages / pages_to_read_in_an_hour
needed_time_reading_per_day = int(time_to_read_the_book / number_days_for_reading)

print(needed_time_reading_per_day)