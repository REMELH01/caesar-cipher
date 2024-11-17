def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            char = char.lower()
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text

user_input = input("Please enter a sentence: ")
encrypted_output = caesar_cipher(user_input, 5)

print("The encrypted sentence is:", encrypted_output)