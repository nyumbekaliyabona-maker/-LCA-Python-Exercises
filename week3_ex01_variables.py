name = input("What is your name?: ")
age = input("How old are you?: ")
print("Hello " + name + ", you are " + age + " years old!")

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")

# Ask the user for a temperature in Celsius and store it as a float
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
