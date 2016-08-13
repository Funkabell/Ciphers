import string
import itertools


def main():
    action = raw_input("Would you like to encrypt or decrypt? (e/d) ")
    if action == "d":
        text = raw_input("Please enter the string to decrypt : ").upper()
        key = raw_input("Please enter the key : ").upper()
        print decrypt_vingenere(text, key)
    if action == "e":
        text = raw_input("Please enter the string to encrypt : ").upper()
        key = raw_input("Please enter the key : ").upper()
        print encrypt_vingenere(text, key)

    #print encrypt_caesar('BASS', 'B')
    #print decrypt_caesar('CBTT', 'B')
    #print encrypt_vingenere("ATTACKATDAWN", "LEMON")
    #print decrypt_vingenere('LXFOPVEFRNHR', 'LEMON')


def decrypt_vingenere(text, key):

    return ''.join(decrypt_caesar(text_letter, key_letter) for key_letter, text_letter in zip(itertools.cycle(key), text))


def encrypt_vingenere(text, key):

    return ''.join(encrypt_caesar(text_letter, key_letter) for key_letter, text_letter in zip(itertools.cycle(key), text))


def encrypt_caesar(text, key):

    new_order = string.uppercase[string.uppercase.find(key):]
    new_order += string.uppercase[:string.uppercase.find(key)]
    letter_dict = dict(zip(string.uppercase, new_order))

    encrypted_string = ''.join(letter_dict[letter] for letter in text)

    return encrypted_string


def decrypt_caesar(text, key):

    new_order = string.uppercase[string.uppercase.find(key):]
    new_order += string.uppercase[:string.uppercase.find(key)]
    letter_dict = dict(zip(new_order, string.uppercase))

    decrypted_string = ''.join(letter_dict[letter] for letter in text)

    return decrypted_string




if __name__ == "__main__":
    main()