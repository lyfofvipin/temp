import datetime
import calendar

def weekday_count(start, end, week_day):
  start_date  = datetime.datetime.strptime(start, '%d/%m/%Y')
  end_date    = datetime.datetime.strptime(end, '%d/%m/%Y')
  week        = {}
  for i in range((end_date - start_date).days):
    day       = calendar.day_name[(start_date + datetime.timedelta(days=i+1)).weekday()].capitalize()
    week[day] = week[day] + 1 if day in week else 1
  return week[week_day]

print(weekday_count(str(raw_input("Enter start date: ")), str(raw_input("Enter end date: ")), str(raw_input("Enter weekday :")).capitalize()))