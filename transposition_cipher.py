import math


def main():

    key = 8
    text = "Common sense is not so common."
    # should be Cenoonommstmme oo snnio. s s c
    print encrypt(text,key)
    text = "Cenoonommstmme oo snnio. s s c"
    print decrypt(text,key)


def encrypt(text, key):

    encrypted_str = ""
    for i in xrange(key):
        for j in range(i,len(text),key):
            encrypted_str += text[j]
    return encrypted_str


def decrypt(text,key):

    decrypted_str = ""
    key_opp = (len(text) / key) + 1
    rows = (len(text) / key)
    if (rows % key) != 0: rows = rows + 1
    #decrypted = [""] * rows

    blanks = (rows*key) - len(text)
    text_length = len(text) + 1

    for i in range(key_opp):
        blank_range = 0
        for number,j in enumerate(range(i,text_length,rows)):
            if len(decrypted_str) == len(text):
                return decrypted_str
            if blanks is not 0 and number > key - blanks:
                j -= 1
            decrypted_str += text[j]

    return decrypted_str


if __name__ == "__main__":
    main()