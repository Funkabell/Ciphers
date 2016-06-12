import string


def main():
    print encrypt_caesar('BASS', 'B')
    print decrypt_caesar('CBTT', 'B')
    print encrypt_vingenere("ATTACKATDAWN", "LEMON")
    print decrypt_vingenere('LXFOPVEFRNHR', 'LEMON')


def decrypt_vingenere(text, key):

    # changing key to fit length of word e.g. LEMONLEMONLE
    text_length = len(text)
    key *= (text_length % len(key))
    key += key[:(text_length - len(key))]

    decrypted_string = ''

    for number, letter in enumerate(text):
        decrypted_string += decrypt_caesar(letter, key[number])

    return decrypted_string


def encrypt_vingenere(text, key):

    # changing key to fit length of word e.g. LEMONLEMONLE
    text_length = len(text)
    key *= (text_length % len(key))
    key += key[:(text_length - len(key))]

    encrypted_string = ''

    for number, letter in enumerate(text):
        encrypted_string += encrypt_caesar(letter, key[number])

    return encrypted_string


def encrypt_caesar(text, key):

    encrypted_string = ""
    new_order = string.uppercase[string.uppercase.find(key):]
    new_order += string.uppercase[:string.uppercase.find(key)]

    for letter in text:
        encrypted_string += new_order[string.uppercase.find(letter)]
    return encrypted_string


def decrypt_caesar(text, key):

    decrypted_string = ""
    new_order = string.uppercase[string.uppercase.find(key):]
    new_order += string.uppercase[:string.uppercase.find(key)]

    for letter in text:
        for i in xrange(26):
            if new_order[i] == letter:
                decrypted_string += string.uppercase[i]

    return decrypted_string




if __name__ == "__main__":
    main()