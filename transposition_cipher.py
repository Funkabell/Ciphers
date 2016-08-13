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

    key = float(key)
    columns = int(math.ceil(len(text) / key))
    rows = int(key)
    blanks = (columns*rows) - len(text)
    decrypted = ['']*columns

    col = 0
    row = 0

    for letter in text:
        decrypted[col] += letter
        col += 1

        if (col == columns) or ((col == columns - 1) and (row >= rows - blanks)):
            col = 0
            row += 1
    return ''.join(decrypted)

if __name__ == "__main__":
    main()