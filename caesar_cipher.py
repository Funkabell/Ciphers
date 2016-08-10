import string


def main():
    brute = 0
    action = raw_input("Would you like to encrypt or decrypt? (e/d) ")
    if action == "d":
        brute = raw_input("Do you have the key or would you like to brute force? (k/b) ")

    if action == "e":
        str = raw_input("Please enter the string to encrypt : ")
        key = int(raw_input("Please enter the key : "))
        print encrypt(str,key)

    elif action == "d" and brute == "k":
        str = raw_input("Please enter the string to decrypt : ")
        key = int(raw_input("Please enter the key : "))
        print decrypt(str,key)
    elif action == "d" and brute == "b":
        str = raw_input("Please enter the string to decrypt : ")
        list_brute = decrypt_brute(str)
        for option in list_brute:
            print option
    ##Should return cbtt
    #encrypted = encrypt("bass", 2)
    #print encrypted
    ##Should return bass
    #decrypted = decrypt("cbtt", 2)
    #print decrypted
    ##Should return Hello
    #decrypt_brute("ifmmp")


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
    list_brute = []
    for i in range(1,26):
        list_brute.append("Key#%s: %s" % (i, decrypt(str,i)))
    return list_brute

if __name__ == "__main__":
    main()