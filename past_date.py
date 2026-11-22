# Question:
# Import the datetime module.
# Get the current date.
# Calculate the date 30 days ago using timedelta().
# Display today's date and the calculated past date.
import datetime
today = datetime.date.today()
past_date = today - datetime.timedelta(days=30)
print("todays date",today)
print("past date",past_date)