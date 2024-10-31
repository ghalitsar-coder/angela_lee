import random
# import day1
# # print(f"Random Integer 0-10 {random.randint(0,10)}")
# print(f"Random from another module / file {day1.random_number_0_to_10}")

# //* PART 2
# number = random.randint(0,1)
# number_rand = round(random.random() * 1)
# print(f"Number random {number_rand}")
# if number == 0:
#     print("Head")
# else :
#     print("Tail")


# //* PART 3 
# friends = ["Alice", "Bob", "Zach","Robert", "Adam", "Angela"]
# index = random.randint(0,len(friends)-1)
# print(f"panjang dari penggunaan method len: {len(friends)}")

# print(f"The person should pay the bill is : {friends[index]}")


# //* PART 4

# while True:
#     options= ["rock","paper","scissor"]
#     option_index = random.randint(0,len(options)-1)
#     user_choice = int(input("What do you choose ?  Type 0 for Rock , Type 1 for Paper , Type 2 for Scissor  : "))
#     comp_choice = options[option_index]
#     result = ""
#     if user_choice in [0,1,2]:
#         if comp_choice == options[user_choice] :
#             result = "Draw"
#         else :
#             if user_choice == 0:
#                 result = "Win" if comp_choice == "scissor" else "Lose"
#             elif user_choice== 1:
#                 result = "Win" if comp_choice == "rock" else "Lose"
#             else :
#                 result = "Win" if comp_choice == "paper" else "Lose"
#     else:
#         print("Invalid input")
    
#     print(f"Computer choose {comp_choice} and you choose {options[user_choice]} You {result} !!")
#     retry = input("Again ? y/n :")
#     if retry == "n":
#         print("================ Good BYE !!! ====================")
#         break
#     else :
#         print("================ Here we go agaaaain !!!! =================\n\n")

# //* PART 5
# data = [41, 39, 101, 28, 170, 151, 190, 200, 158, 54]
# temp = 0

# for i in data:
#     print(i)
#     if i> temp:
#         temp = i
# print(f"The maximum number on the list is {temp}")

# //* PART 6
# total = 0
# for i in range(1,101):
#     total+=i
# print(f"The total of add the numbers from 1 to 100 is  {total}")


# //* PART 7 

# for i in range(1,101):
#     if i %3 == 0 and i %5 == 0 :
#         print(f"FizzBuzz")
        
#     elif i % 5 == 0 and not i % 3 ==0:
#         print(f"Fizz")
#     elif i % 3 == 0 and not i % 5 == 0:
#         print(f"Buzz")
#     else :
#         print(i)

# //* PART 8  

    # letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # numbers =  ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

    # letter_length = int(input("How many letters do you want inside your password ? "))
    # number_length = int(input("How many number do you want ? "))
    # symbol_length = int(input("How many symbol do you want ? "))

    # temp_pass = []
    # password = ""

    # for a in range(0,letter_length):
    #     random_index = random.randint(0, len(letters)-1)
    #     temp_pass.append(letters[random_index])
        
    # for b in range(0,number_length):
    #     random_index = random.randint(0, len(numbers)-1)
    #     temp_pass.append(numbers[random_index])
        
    # for c in range(0,symbol_length):
    #     random_index = random.randint(0, len(symbols)-1)
    #     temp_pass.append(symbols[random_index])

    # arr =[1,2,3]
    # print(f"lenght dari arr {len(arr)}")
    # password= "".join(random.sample(temp_pass,len(temp_pass)))
    # print(f"ini password anda {password}")
    
    
    
    # //* PART 9
        # def turn_right():
        #     turn_left()
        #     turn_left()
        #     turn_left()

        #     turn_left()
        #     move()
        #     turn_right()
        #     move()
        #     turn_right()
        #     move()
        #     turn_right()
        #     move()
        
    # //* PART 10
    #    def turn_right():
    #     turn_left()
    #     turn_left()
    #     turn_left()

    # def jump ():
    #     move()
    #     turn_left()
    #     move()
    #     turn_right()
    #     move()
    #     turn_right()
    #     move()
    #     turn_left()

    # for j in range(0,6):
    #     jump()
# //* PART 11
#     def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump ():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    

# while not at_goal()  :
#     if not wall_in_front():
#         if front_is_clear():
#             move()
#     else :
#         jump()
            
            
# //* PART 12
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump ():
#     turn_left()
#     while front_is_clear()and wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
   
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else :
#         move()
        
# num = 0
# for i in  range(0, 10):
#    num += i
# print(num)

    # //* PART 13
    # def turn_right():
    # turn_left()
    # turn_left()
    # turn_left()

# def jump ():
#     turn_left()
#     while front_is_clear()and wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()
   
# while not at_goal():
#     if wall_in_front():
#         jump()
#     else :
#         move()

# //* PART 14
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
        
     
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif front_is_clear() and not wall_on_right():
#         turn_right()
#         move()
#     elif not front_is_clear() and wall_on_right():
#         turn_left()
#     else :
#         turn_right()
#         if front_is_clear():
#             move()


# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()
     
# while not at_goal() :
#     if right_is_clear() :
#         turn_right()
#         move()
#     elif front_is_clear() :
#         move()
#     else :
#         turn_left()
    


# guess = [""]* 5

# print(guess)


word = "chair"
guess = "i"

# Find all indices where the guessed character appears in the word
indices = [index for index, char in enumerate(word) if char == guess]

print(indices[0])  # Output: [3]