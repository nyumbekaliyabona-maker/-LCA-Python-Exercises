#question 1
from turtle import color


fruits = ["apple", "banana", "cherry", "pear", "elderberry"]    
fruits.append("kiwi")
fruits.insert(0, "strawberry")
fruits.remove("banana")
print(fruits)

#question 2
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
total_sum = sum(squared_numbers)
len=len(squared_numbers)
print(f"The sum of the squared numbers is: {total_sum}")
print(f"The number of squared numbers is: {len}")

#question 3
countries_capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "UK": "London",
    "France": "Paris",
    "Japan": "Tokyo"
}
countries_capitals["Germany"] = "Berlin"
update_capital = input("japan= Yiroshima")
countries_capitals["Japan"] = update_capital
del countries_capitals["France"]
print(countries_capitals)

#Question 4
fruit_colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

print(fruit_colors.keys())


print(fruit_colors.values())

for fruit, color in fruit_colors.items():
    print(f"{fruit}: {color}")


    target_fruit = "banana"

if target_fruit in fruit_colors:
    print(f"The color of {target_fruit} is {fruit_colors[target_fruit]}")