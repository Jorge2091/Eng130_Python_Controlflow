# pseudo coding

# if it's cold:
# - take jacket
#
# if it's raining:
# - rain rack
#
# if it's sunny: boolean value true - next line
# - let's go the beach
#
# else or elif
# weather = "sunny"
# if weather == "cold": #True or False
#     print("wear a jacket")
# elif weather == "sunny":
#     print("let's go to the beach")
# else:
#     print("no match found")

# age restriction for movie tickets
# create a condition for 18 & above
# 16 & above
# universal 3 +
# pg 8+
# 12a
# 15 & above
# if nothing matched, inform the user to enter their age again
# user must not be allowed to enter age over 117 years
promt = True
while promt:
    age = input("How old are you now? ")
    if age.isdigit():
        promt = False
    else:
        print("please input only digits")

user_age = int(age)

def movie_rating(age):
    if age > 117:
        print("please retry again and input correct value for age")
    elif age >17:
        print("You can view any movie you like, no restriction on you")
    elif age > 15:
        print("You can only view movies which are 16 and under")
    elif age > 14:
        print("you can only view movies of 15 and under")
    elif age > 11:
        print("you can view 12a movies and under")
    elif age > 7:
        print("you can view pg movies and under")
    elif age > 3:
        print("you can only watch U rated movies")
    else:
        print("Too young")
    return (f"Your age is {age}")

print(movie_rating(user_age))
