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
# apple_price = 500
# pizza_price = 1200
# ramen_price = 1300

# price = 0

# item = input("What item would you like to buy?: ")

# if item == "apple":
#     price += apple_price
# elif item == "pizza":
#     price += pizza_price
# elif item == "ramen":
#     price += ramen_price
# else:
#     print(f"{item} is not on the menu")
#     exit()

# quantity = int(input("How many do you want to buy?: "))
# total_price = price * quantity

# print(f"Your total amount will be {total_price} yen")


price1 = 3132.43118
price2 = -23.232
price3 = 12.8987

print(f"{price2: .3f}")     # {price:.2f} = {price: .2f} even when there's space between // formatting decimal places
print(f"{price3:010}")      # 10 is how many spaces and 010 is replaceing the spaces with 0. and nope, other numbers or char won't work
print(f"{price3:+}")        # + sign in front of the number 
print(f"{price2:+}")        # the minus ones will show minus instead
print(f"{price1:,}")        # each thousand will seperate by ,
print(f"{price1:+,.2f}")    # can also combine