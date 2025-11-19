#Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime
from datetime import date
now = datetime.now()
print(now)                      
day = now.day                   
month = now.month               
year = now.year                 
hour = now.hour                 
minute = now.minute             
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}') 

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

#Today is 5 December, 2019. Change this time string to time.
today_string="5 december, 2019"
print("date string=",today_string)
today_date=datetime.strptime(today_string,"%d %B, %Y")
print("today date is ",today_date)

#Calculate the time difference between now and new year.
today=date(2025,11,19)
new_year=date(2026,1,1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1=datetime.now()
t2=datetime(2026,1,1)
diff=t2-t1
print('Time left for new year:', diff)

#Calculate the time difference between 1 January 1970 and now.
t3=datetime(1970,1,1)
diff=t1-t3
print('Time left for new year:', diff)
