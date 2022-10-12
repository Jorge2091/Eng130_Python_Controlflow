# Python Control Flow

## if elif else

### Loops - for loop - while loop

#### python keywords break - continue etc

if it's cold:
- take jacket

if it's raining:
- rain mack

if it's sunny: boolean value true - next line
- let's go the beach

else or elif

### Age restriction for movie tickets

with the if statement, you can make sure that all user can view or only select a potion of categories such as age restriction in movies<br/>
We can use the `while` loop to keep asking for user input if the data doesn't match. This is to make sure the user inputs digits only
```python
promt = True
while promt:
    age = input("How old are you now? ")
    if age.isdigit():
        promt = False
    else:
        print("please input only digits")
```
We then need to make sure that the input is transformed from string to an integer value with the `int()` method.
```python
age = int(age)
```
