# //* PART 1

print("Hello World!")


# //* PART 2

# name = input("Name pls! ")
# age = input("age pls! ")
# classOf = input("class pls! ")
# print(f"Hi my name is {name} , and my age is {age}, im from {classOf}")


# //* PART 3

# name = input("Name pls! ")
# length = len(name)
# print(f"The name '{name}'  has {length} characters!")


# //* PART 4

# print("Welcome to the Band Name Generator!")
# city = input("What`s the name of the city you grew up in ? ")
# pet = input ("What`s your pet name ? ")
# print(f"Your band name could be {city} {pet}  ")


# //* PART 5
# print("hello"[-1])
# print(type("hello"))
# print(type(12345))
# print(type(123.356))
# print(type(False))


# print("Your name length is " + str(len(input("Your name "))))


# //* PART 6

# print(3*(3+((3//3)-3)))

# //* TIP CALCULATOR

# bill = float(input("What was the total bill ? "))
# tipGiven = int(input("How much the tip would u like to give ? 10, 12 or 15 ? "))
# peopleSplit = int(input("How many people to split the bill ? "))
# tip_as_percent = tipGiven / 100
# total_tip_amount = bill * tip_as_percent
# totalBill = bill + total_tip_amount
# totalSplit = totalBill / peopleSplit
# result =  round(totalSplit,2)
# # result = round(((totalBill + (totalBill * (tipGiven / 100))) / peopleSplit), 2)
# print(f"Each person should pay {result:.2f}")


# //* PART 7

print("Welcome to Modulo!")

number = int(input("Enter the number "))
if number % 2 == 0:
    print("Even number")
else : 
    print("Odd number")