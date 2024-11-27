import string

# * my version

# def cipher_generator():
#     lowercase_alphabet = list(string.ascii_lowercase)
#     alphabet_length = len(lowercase_alphabet)
#     newMessage = []
#     while True:
#         print("Hello Welcome to the cipher generator")
#         generate_type = input("type 'encrypt' to encrypt or 'decrypt' to decrypt : ")
#         message = input(f"Please type the message that u want to {generate_type} : ")
#         shift_number = int(input(" of cipher you want to generate : "))
#         shift_number %= alphabet_length
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


# * GPT  - version


def cipher_generator():
    lowercase_alphabet = list(string.ascii_lowercase)
    alphabet_length = len(lowercase_alphabet)
    new_message = []

    while True:
        print("Hello! Welcome to the cipher generator.")
        generate_type = input(
            "Type 'encrypt' to encrypt or 'decrypt' to decrypt: "
        ).lower()
        if generate_type not in ["encrypt", "decrypt"]:
            print("Invalid input, please enter 'encrypt' or 'decrypt'.")
            continue

        message = input(
            f"Please type the message you want to {generate_type}: "
        ).lower()
        shift_number = int(input("Enter the shift number for the cipher: "))
        shift_number %= (
            alphabet_length  # Keep the shift within the range of the alphabet
        )

        for char in message:
            if char in lowercase_alphabet:
                char_index = lowercase_alphabet.index(char)

                if generate_type == "encrypt":
                    new_index = (char_index + shift_number) % alphabet_length
                elif generate_type == "decrypt":
                    new_index = (char_index - shift_number) % alphabet_length

                new_message.append(lowercase_alphabet[new_index])
            else:
                # For characters not in the alphabet (e.g., spaces, punctuation), keep them as is
                new_message.append(char)

        print(f"Here is the {generate_type}ed message: {''.join(new_message)}")
        new_message = []

        retry = input("Type 'yes' to continue or 'no' to quit: ").lower()
        if retry == "no":
            print("Goodbye!")
            return
        elif retry != "yes":
            print("Invalid input; I'll assume you want to continue.")


print(cipher_generator())



# * angela lee version
