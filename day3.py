import string


def cipher_generator():
    lowercase_alphabet = list(string.ascii_lowercase)
    newMessage = []
    while True:
        print("Hello Welcome to the cipher generator")
        generate_type = input("type 'encrypt' to encrypt or 'decrypt' to decrypt : ")
        message = input(f"Please type the message that u want to {generate_type} : ")
        shift_number = int(input(" of cipher you want to generate : "))
        if generate_type == "encrypt":
            for msg in message:
                if (lowercase_alphabet.index(msg) + shift_number) > len(
                    lowercase_alphabet
                ):
                    newMessage.append(
                        lowercase_alphabet[
                            lowercase_alphabet.index(msg)
                            + shift_number
                            - len(lowercase_alphabet)
                        ]
                    )
                else:
                    newMessage.append(
                        lowercase_alphabet[lowercase_alphabet.index(msg) + shift_number]
                    )
            print(f"heres the {generate_type} message {"".join(newMessage)}")
            newMessage = []
        elif generate_type == "decrypt":
            for msg in message:
                if (lowercase_alphabet.index(msg) - shift_number) < 0:
                    newMessage.append(
                        lowercase_alphabet[
                            lowercase_alphabet.index(msg)
                            - shift_number
                            + len(lowercase_alphabet)
                        ]
                    )
                else:
                    newMessage.append(
                        lowercase_alphabet[lowercase_alphabet.index(msg) - shift_number]
                    )
            print(f"heres the {generate_type} message {"".join(newMessage)}")
            newMessage = []

        else:
            print("Invalid input, please enter 'encrypt' or 'decrypt'")
            return None
        retry = input("Typer 'yes' to continue otherwise type 'no' ")
        if retry.lower() in ["yes", "no"]:
            if retry.lower() == "no":
                print("Good bye!")
                return None
        else:
            print("You type Invalid input ill asume u said yes")
            newMessage = []

            continue


print(cipher_generator())
