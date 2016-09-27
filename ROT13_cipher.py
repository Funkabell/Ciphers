import string


def main():
    text = 'hello'
    print ROT13(text)
    text = 'uryyb'
    print ROT13(text)


def ROT13(text):        # encrypts and decrypts
    letter_order = string.lowercase
    rot13_order = letter_order[13:] + letter_order[:13]

    letter_dict = dict(zip(letter_order, rot13_order))

    encrypted_str = ''.join(letter_dict[letter] for letter in text)
    return encrypted_str


if __name__ == "__main__":
    main()