alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    output_text = ""
    for letter in text:
        if direction == "encode":
            shifted_index = alphabet.index(letter) + shift
            if shifted_index > 25:
                shifted_index -= 26
        else:
            shifted_index = alphabet.index(letter) - shift
            if shifted_index < 0:
                shifted_index += 26
        output_text += alphabet[shifted_index]
    print(f"The {direction}d text is {output_text}")

caesar(text, shift, direction)