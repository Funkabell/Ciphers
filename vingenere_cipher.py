import string

def main():
    #print encrypt_caesar('BASS', 1)
    #print decrypt_caesar('CBTT', 1)
    #print encrypt_vingenere("ATTACKATDAWN", "LEMON")
    print decrypt_vingenere('LXFOPVEFRNHR', 'LEMON')


def decrypt_vingenere(text, key):

    #changing key to fit length of word e.g. LEMONLEMONLE
    text_length = len(text)
    key *= (text_length % len(key))
    key += key[:(text_length - len(key))]

    decrypted_list = []
    slice_point = 0
    decrypted_string = ''

    #finds the new encrypted order
    for text_number, text_letter in enumerate(text):
        for i in xrange(26):
            if text_letter == string.uppercase[i]:
                slice_point = i
        decrypted_list.append(decrypt_caesar(text_letter, slice_point))

    #finds the key letter number
    for key_number, key_letter in enumerate(key):
        for i in xrange(26):
            if key_letter == string.uppercase[i]:
                decrypted_list[key_number] = (decrypted_list[key_number], i)


    vertical_placement = 0  # first letter
    horizontal_placement = 0
    for order, number in decrypted_list:
        #print number, order
        for i in xrange(26):
            if order[0] == string.uppercase[i]:
                vertical_placement = i
                print vertical_placement

            if number >= vertical_placement:
                horizontal_placement = number - vertical_placement
            elif number < vertical_placement:
                horizontal_placement = vertical_placement - number

        decrypted_string += string.uppercase[horizontal_placement]

    return decrypted_string


def encrypt_vingenere(text, key):

    #changing key to fit length of word e.g. LEMONLEMONLE
    text_length = len(text)
    key *= (text_length % len(key))
    key += key[:(text_length - len(key))]

    encrypted_list = []
    slice_point = 0
    ecrypted_string = ''

    #finds the placement of the letter
    for key_number, key_letter in enumerate(key):
        for i in xrange(26):
            if key_letter == string.uppercase[i]:
                encrypted_list.append(i)

    #finds the new encrypted order
    for text_number, text_letter in enumerate(text):
        for i in xrange(26):
            if text_letter == string.uppercase[i]:
                slice_point = i
        #rewrites the list to a list of tuples
        encrypted_list[text_number] = (encrypted_list[text_number],(encrypt_caesar(text_letter, slice_point)))

    for i, order in encrypted_list:
        ecrypted_string += order[i]

    return ecrypted_string


def encrypt_caesar(text, slice_point):
    
    encrypted_string = ""
    new_order = str(string.uppercase[slice_point:])
    new_order += str(string.uppercase[:slice_point])

    for letter in text:
        for number, i in enumerate(string.uppercase):
            if letter == i:
                encrypted_string += new_order[number]
    #return encrypted_string
    return new_order


def decrypt_caesar(text, key):

    decrypted_string = ""
    new_order = str(string.uppercase[key:])
    new_order += str(string.uppercase[:key])

    for letter in text:
        for number, i in enumerate(new_order):
            if letter == i:
                decrypted_string += string.uppercase[number]
    #return decrypted_string
    return new_order



if __name__ == "__main__":
    main()