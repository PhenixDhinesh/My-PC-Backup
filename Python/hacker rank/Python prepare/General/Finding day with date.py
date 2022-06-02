import calendar

m,d,y=list(map(int,input().split()))
day=calendar.weekday(y,m,d)
print(calendar.day_name[day].upper())