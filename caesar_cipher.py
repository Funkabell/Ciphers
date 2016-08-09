import string


def main():
    encrypted = encrypt("bass", 2)
    print encrypted

    decrypted = decrypt("cbtt", 2)
    print decrypted

    decrypt_brute("ifmmp")


def encrypt(str, key):
    encrypted_str = ""
    new_order = string.lowercase[key-1:]
    new_order += string.lowercase[:key-1]

    for letter in str:
        placement = string.lowercase.find(letter)
        encrypted_str += new_order[placement]
    return encrypted_str


def decrypt(str, key):
    decrypted_str = ""
    key = 27 - key
    old_order = string.lowercase[key:]
    old_order += string.lowercase[:key]

    for letter in str:
        placement = string.lowercase.find(letter)
        decrypted_str += old_order[placement]
    return decrypted_str


def decrypt_brute(str):
    for i in range(1,26):
        print decrypt(str,i)


if __name__ == "__main__":
    main()