from datetime import date

def Calculate(BirthDate):
    today = date.today()
    age = today.year - BirthDate.year - ((today.month ,today.day) < (BirthDate.month ,BirthDate.day))
    return age
print("Welcome to Age calculator, Lets calculate your age...")
year = int(input("Enter a birth year:"))
month = int(input("Enter a birthday month:"))
day = int(input("Enter birthday date:"))
Calculated_age = Calculate(date(year,month,day))
print("Your age is "+ str(Calculated_age) +" now")
print("Thanks for using age calculator")