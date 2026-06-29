num = int(input("Enter a number:"))
if num > 0:
    print("Number is +ve")
elif num<0:
    print("Number is -ve")
else:
    print("Number is zero")

#task Grade Calculator
marks = int(input("Enter your marks(0-100):"))
if marks >= 90:
    grade ="A"
elif marks >= 75:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks < 50 :
    grade = "Average"
else:
    print("Fail")

print("Your Grade:", grade)

#task
age = int(input("Enter your age:"))
if age < 60:
    age = "You are an adult"
elif age < 18:
    age ="You are young"
else:
    age= "You are senior citizen"

print("Your Age:", age)