import random

def encoded_message(text):
    encoded_message = ''
    for char in text:
        encoded_char = chr(random.randint(33, 126))
        encoded_message += encoded_char
    return encoded_message

def main():
    user_input = input("Enter text to encode into a box: ")
    encoded_text = encoded_message(user_input)
    print("Encoded message:")
    print(encoded_text)

if __name__ == "__main__":
    main()
