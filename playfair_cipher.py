def main():
    text = list('go to new york')
    password = 'fiveabcdghklmnopqrstuwxyz'
    print encrypt_playfair(text, password)

    text = list('hnztsgxzmtmu')
    print decrypt_playfair(text, password)


def encrypt_playfair(text, password):
    encrypted_str = ''
    check_validity(text)  # deletes spaces and adjusts string length

    for i in xrange(0, len(text), 2):
        first_letter = text[i]
        second_letter = text[i + 1]

        first_result = ''
        second_result = ''

        first_position = password.find(first_letter)
        second_position = password.find(second_letter)
        if same_row(first_position, second_position):
            first_result, second_result = samerow_position(first_position, second_position)
        elif same_column(first_position, second_position):
            first_result, second_result = samecolumn_position(first_position, second_position)
        else:
            first_result, second_result = new_position(first_position, second_position)
        encrypted_str = encrypted_str + password[first_result] + password[second_result]

    return encrypted_str


def decrypt_playfair(text, password):
    decrypted_str = ''

    for i in xrange(0, len(text), 2):  # runs 6 times
        first_letter = text[i]
        second_letter = text[i + 1]

        first_result = ''
        second_result = ''

        first_position = password.find(first_letter)
        second_position = password.find(second_letter)
        if same_row(first_position, second_position):
            first_result, second_result = re_samerow_position(first_position, second_position)
        elif same_column(first_position, second_position):
            first_result, second_result = re_samecolumn_position(first_position, second_position)
        else:
            first_result, second_result = new_position(first_position, second_position)
        decrypted_str = decrypted_str + password[first_result] + password[second_result]

    return decrypted_str


def same_row(first, second):            #whether the letters are in the same row
    first_row = first / 5
    second_row = second / 5
    if first_row == second_row:
        return True
    else:
        return False


def same_column(first, second):         #whether the letters are in the same column
    first_column = first % 5
    second_column = second % 5
    if first_column == second_column:
        return True
    else:
        return False


def samerow_position(first, second):    #get new position if letters are in the same row
    first = (first + 1) % 25
    second = (second + 1) % 25

    return first, second


def samecolumn_position(first, second): #get new position if letters are in the same column
    first = (first + 5) % 25
    second = (second + 5) % 25

    return first, second


def new_position(first, second):        #get new position if letters are not in the same row or column
    first_row = first / 5
    first_column = first % 5
    # print first_column
    second_row = second / 5
    second_column = second % 5

    first_result_row = first_row
    first_result_column = second_column
    first_result = (first_result_row * 5) + first_result_column

    second_result_row = second_row
    second_result_column = first_column
    second_result = (second_result_row * 5) + second_result_column

    return first_result, second_result


def re_samerow_position(first, second): #get original position if letters are in the same column
    first = (first - 1) % 25
    second = (second - 1) % 25

    if first < 0:
        first = 24
    if second < 0:
        second = 24
    return first, second


def re_samecolumn_position(first, second):  #get original position if letters are not in the same column or row
    first = (first - 5) % 25
    second = (second - 5) % 25

    if first < 0:
        first = 25 + first
    if second < 0:
        second = 25 + second
    return first, second


def check_validity(text):       #adjusts length
    i = -1
    while (len(text) != i):
        i = i + 1
        if i == len(text):
            break
        if text[i] == ' ':
            del text[i]
    for j in xrange(len(text) - 1):
        if (text[j] == text[j + 1]) and (text[j] != 'x'):
            text[j + 1] = 'x'

    if len(text) % 2 != 0:
        text = text.append('x')

    return (text)


if __name__ == "__main__":
    main()