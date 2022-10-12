

#
# data = 0
#
# while data < 10:
#     print(f"it's working - > {data}")
#     if data == 5:
#         break
#     data += 1


user_prompt = True
while user_prompt:
    age = input("Please enter your age? ")

    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits only")
print(f"Your age is {age}")


# calculate their age - year of birth etc.
year = 2022 - int(age)
year = str(year)
print("and you were born in {}".format(year))