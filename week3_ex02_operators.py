#question1

#x = 0
#x += 3
#y = 5
#y *= 2
#result = x / y
#print(result)

#question2




a = 10
b = 5
c = 8
if a > b:
    print("a is greater than b")
if b == a:
    print("b is equal to a")
else:
    print("b is not equal to a")
if c <= a:
    print("c is less than or equal to a")
else:
    print("c is greater than a")
if b % 2 == 0:
    print("b is even")
else:
    print("b is odd")


final_condition = (a > b) or (b % 2 == 0 and c <= a)
print(final_condition)

#Question3
score = int(input("Enter the score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"The grade for the score is: {grade}")

#Question4
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
