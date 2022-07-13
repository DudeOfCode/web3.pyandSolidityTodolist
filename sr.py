Day = int(input("Enter the day in numbers: "))
while Day > 31 or Day == 0:
    if Day == 0:
        Day = int(input("The day cannot be zero: "))
    if Day > 31:
        Day = int(input("Days cannot be greater than 31 in a month: "))
