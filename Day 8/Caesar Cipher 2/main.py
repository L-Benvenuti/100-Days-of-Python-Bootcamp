alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, type):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter)
        if type == "encode":
            shifted_position += shift_amount
        else:
            shifted_position -= shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

if direction == "encode" or direction == "decode":
    caesar(original_text=text, shift_amount=shift, type=direction)
else:
    print("Bruh, try again...")