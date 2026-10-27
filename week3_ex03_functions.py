#Question1
def greet(hello, world):
    print("the greeting is: " + hello + ", " + world)

greet("Hello", "World")


#Question2
def personalized_greeting(name):
    print("Hello " + name + "!")

personalized_greeting("Liyabona")


#Question3
def square(number):
    return number * number

result = square(5)
print(result)


#Question4
def rectangle_area(length, width):
    return length * width


result = rectangle_area(4, 5)
print(result)

#Question5
def apply_operation(operation, number):
    return operation(number)

def double(x):
    return x * 2

test_result = apply_operation(double, 5)
print(f"The double of 5 is: {test_result}")
