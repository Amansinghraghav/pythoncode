def is_leap(year):
    if year % 4 != 0 :
        leap = False
    else :
        leap = True
    return leap
year = int(input("enter the n number"))
print(is_leap(year))