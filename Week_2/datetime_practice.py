from datetime import datetime, date, time

today = date.today()
print(today)

tomorrow = date(2025, 9, 11)
print(tomorrow)

next_week = date.fromisoformat("2025-09-18")
print(next_week)

right_now = datetime.now()
print(right_now)

seconds_timestamp = right_now.timestamp()
print(seconds_timestamp)

my_date =  datetime.fromtimestamp(1750000000)
print(my_date)