import random

words = [
    # 3-letter words
    "cat",
    "dog",
    "sun",
    "bat",
    # 4-letter words
    "moon",
    "star",
    "tree",
    "wolf",
    "fish",
    # 5-letter words
    "apple",
    "grape",
    "river",
    "stone",
    "flame",
    "grass",
    # 6-letter words
    "forest",
    "banana",
    "rabbit",
    "silver",
    "planet",
    "mirror",
    "pirate",
    "crystal",
    "danger",
    "sunset",
]
# random.shuffle(words)
# isWin = False

# try:
#     word_char = int(input("Enter the length of characters for the word max 3-6: "))
#     if not word_char in [3, 4, 5, 6]:
#         raise ValueError("Invalid word length. Please try again.")
# except ValueError as e:
#     print(e)
# else:
#     result = next((word for word in words if len(word) == word_char), None)
#     # result = "mirror"
#     print(result)
#     life = len(result) 
#     user_guess = ["_"] * len(result) 
#     while life > 0:
#         try:
#             char = input("guess the  character with one input at a time : ").lower()
#         except ValueError as e:
#             print(e)
#         if len(char) == 1:
#             if char in list(result):
#                 indices = [
#                     index for index, character in enumerate(result) if character == char
#                 ]
#                 print(f"INDICES {indices}")
#                 for idx,index in enumerate(indices):
#                     if user_guess[index] == "_":
#                         user_guess[index] = char
#                         break
#                     elif idx == len(indices) - 1:  
#                         life -= 1
#                         print("Character already guessed.")
#                         print(f"Wrong guess, you have {life} attempts left.")

                        
#                 print(f"Guess {" ".join(user_guess)}")
#                 if "".join(user_guess) == result:
#                     isWin = True
#                     break
#             else:
#                 life-= 1
#                 print("".join(user_guess))
#                 print(f"Wrong guess, you have {life} attempts left.")
#         else:
#             print("Please enter only one character.")
#     if isWin:
#         print(f"The Word is {result} You win!!!")
#     else:
#         print(f"The correct word is {result} You LOSE!!")



# # //* ANGELA VERSION
# 


words_list = ['air','dog','moon']
choosen_word = random.choice(words_list)
print(f"choosen_word: {choosen_word}")
placeholder = "_" * len(choosen_word)
print(f"placeholder: {placeholder}")
correct_letters = []
game_over =False

while not game_over :
    guess = input("Enter 1 character of the word : ").lower()
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display+= letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if "_" not in display:
        game_over = True
        print("Congratulations, you won!")
    print(display)


print(f"Curreny guess: {display}")