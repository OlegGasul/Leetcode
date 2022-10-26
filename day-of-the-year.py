def dayOfYear(date: str) -> int:
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    year, month, day = [int(x) for x in date.split('-')]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days[1] = 29
        
    return sum(days[0 : month - 1]) + day

print(dayOfYear("2019-01-09"))
print(dayOfYear("2019-02-10"))