alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(text, shift, direction):
    text_value = ""
    if shift > len(alphabet):
        shift = shift % 26
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            text_value += alphabet[new_position]
        else:
            text_value += char
    print(f"The {direction}d text is: {text_value}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caeser(text=text, shift=shift, direction=direction)

    repeat = input("Do you want to run the program again? Type Y or N\n").lower()
    if repeat == "n":
        should_continue = False
        print("Goodbye!")