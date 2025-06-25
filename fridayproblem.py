import datetime

def has_friday_13th(month, year):
    try:
        date = datetime.date(year, month, 13)
        return date.weekday() == 4  
    except ValueError:
        return False  

print(has_friday_13th(9, 2025)) 
print(has_friday_13th(6, 2025))  
print(has_friday_13th(2, 2026))  
print(has_friday_13th(13, 2025)) 