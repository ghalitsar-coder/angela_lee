import string

lowercase_alphabet = list(string.ascii_lowercase)

# def cipher_generator(lowercase_alphabet):
#     newMessage = []
#     while True:
#         print("Hello Welcome to the cipher generator")
#         generate_type = input("type 'encrypt' to encrypt or 'decrypt' to decrypt : ")
#         message = input(f"Please type the message that u want to {generate_type} : ")
#         shift_number = int(input(" of cipher you want to generate : "))
#         if generate_type == "encrypt":
#             for msg in message:
#                 if (lowercase_alphabet.index(msg) + shift_number) > len(
#                     lowercase_alphabet
#                 ):
#                     newMessage.append(
#                         lowercase_alphabet[
#                             lowercase_alphabet.index(msg)
#                             + shift_number
#                             - len(lowercase_alphabet)
#                         ]
#                     )
#                 else:
#                     newMessage.append(
#                         lowercase_alphabet[lowercase_alphabet.index(msg) + shift_number]
#                     )
#             print(f"heres the {generate_type} message {"".join(newMessage)}")
#             newMessage = []
#         elif generate_type == "decrypt":
#             for msg in message:
#                 if (lowercase_alphabet.index(msg) - shift_number) < 0:
#                     newMessage.append(
#                         lowercase_alphabet[
#                             lowercase_alphabet.index(msg)
#                             - shift_number
#                             + len(lowercase_alphabet)
#                         ]
#                     )
#                 else:
#                     newMessage.append(
#                         lowercase_alphabet[lowercase_alphabet.index(msg) - shift_number]
#                     )
#             print(f"heres the {generate_type} message {"".join(newMessage)}")
#             newMessage = []

#         else:
#             print("Invalid input, please enter 'encrypt' or 'decrypt'")
#             return None
#         retry = input("Typer 'yes' to continue otherwise type 'no' ")
#         if retry.lower() in ["yes", "no"]:
#             if retry.lower() == "no":
#                 print("Good bye!")
#                 return None
#         else:
#             print("You type Invalid input ill asume u said yes")
#             newMessage = []

#             continue


# print(cipher_generator(lowercase_alphabet))


# * angela version


def cipher_it(message,encode_or_decode,shift_number):
    result = ""
    
    for letter in message:
            print(letter)
            if letter not in lowercase_alphabet :
                result += letter
            else:
                if encode_or_decode == 2:
                    shift_number = -abs(shift_number)
                print(f"aftery shift number -> {shift_number}")
                shifted_position = lowercase_alphabet.index(letter) + shift_number
                shifted_position %= len(lowercase_alphabet)
                result += lowercase_alphabet[shifted_position]

    print(
        f"The {"encode" if encode_or_decode == 1 else "decode"}d message is: {result}"
    )


def cipher_generator2():
    while True:
        encode_or_decode = int(
            input(
                "Enter a message to encrypt or decrypt: 1 for encrypt and 2 for decrypt: "
            )
        )
        message = input(
            f"Enter the message that u want to {"encode" if encode_or_decode == 1 else "decode"} : "
        ).lower()
        shift_number = int(input("Enter the shift number: "))
        cipher_it(message,encode_or_decode,shift_number)
        retry = input("Typer 'yes' to continue otherwise type 'no' ")
        if retry.lower() in ["yes", "no"]:
            if retry.lower() == "no":
                print("Good bye!")
                return None
        else:
            print("You type Invalid input ill asume u said yes")
            continue


cipher_generator2()
