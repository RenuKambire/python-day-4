import datetime

today = datetime.date.today()
future_date = today + datetime.timedelta(days=15)

print("today", today)
print("future date", future_date)