# name = "sai han"
# age = 27
# email = "saihan@example.com"
# is_student = True

# age = str(age)

# print("hello world")
# print(f"your name {name} and you're {age}. contact info = {email}. are you a student: {is_student}")
# print(age)
# print(type(age))

# name = input("Enter your name: ")
# print(f"Hello {name}")

# shopping cart
apple_price = 500
pizza_price = 1200
ramen_price = 1300

price = 0

item = input("What item would you like to buy?: ")

if item == "apple":
    price += apple_price
elif item == "pizza":
    price += pizza_price
elif item == "ramen":
    price += ramen_price
else:
    print(f"{item} is not on the menu")
    exit()

quantity = int(input("How many do you want to buy?: "))
total_price = price * quantity

print(f"Your total amount will be {total_price} yen")
