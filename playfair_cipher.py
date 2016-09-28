import string


def main():
    key = 'five'
    password = adjust_password(key)

    text = 'go to new york'
    print encrypt_playfair(text, password)

    text = 'hnztsgxzmtmu'
    print decrypt_playfair(text, password)


def encrypt_playfair(text_string, password):
    print text_string
    encrypted_str = ''
    # deletes spaces and adjusts string length
    text = adjust_text(text_string)
    print text
    text = list(text)
    print text

    for i in xrange(0, len(text), 2):
        first_letter = text[i]
        second_letter = text[i + 1]

        first_result = ''
        second_result = ''

        first_position = password.find(first_letter)
        second_position = password.find(second_letter)
        if is_same_row(first_position, second_position):
            first_result, second_result = change_samerow_position(first_position, second_position)
        elif is_same_column(first_position, second_position):
            first_result, second_result = change_samecolumn_position(first_position, second_position)
        else:
            first_result, second_result = new_position(first_position, second_position)
        encrypted_str = encrypted_str + password[first_result] + password[second_result]

    return encrypted_str


def decrypt_playfair(text_string, password):
    text = list(text_string)
    decrypted_str = ''

    for i in xrange(0, len(text), 2):  # runs 6 times
        first_letter = text[i]
        second_letter = text[i + 1]

        first_result = ''
        second_result = ''

        first_position = password.find(first_letter)
        second_position = password.find(second_letter)

        if is_same_row(first_position, second_position):
            first_result, second_result = re_samerow_position(first_position, second_position)
        elif is_same_column(first_position, second_position):
            first_result, second_result = re_samecolumn_position(first_position, second_position)
        else:
            first_result, second_result = new_position(first_position, second_position)

        decrypted_str = decrypted_str + password[first_result] + password[second_result]

    return decrypted_str


#whether the letters are in the same row
def is_same_row(first, second):
    first_row = first / 5
    second_row = second / 5
    if first_row == second_row:
        return True
    else:
        return False


#whether the letters are in the same column
def is_same_column(first, second):
    first_column = first % 5
    second_column = second % 5
    if first_column == second_column:
        return True
    else:
        return False


#get new position if letters are in the same row
def change_samerow_position(first, second):
    return return_placement(first + 1, second + 1)


#get new position if letters are in the same column
def change_samecolumn_position(first, second):
    return return_placement(first + 5, second + 5)


#get new position if letters are not in the same row or column
def new_position(first, second):
    first_row = first / 5
    first_column = first % 5
    second_row = second / 5
    second_column = second % 5

    first_result_row = first_row
    first_result_column = second_column
    first_result = (first_result_row * 5) + first_result_column

    second_result_row = second_row
    second_result_column = first_column
    second_result = (second_result_row * 5) + second_result_column

    return first_result, second_result


#get original position if letters are in the same column
def re_samerow_position(first, second):
    return return_placement(first - 1, second - 1)


#get original position if letters are not in the same column or row
def re_samecolumn_position(first, second):
    return return_placement(first - 5,second - 5)


def return_placement(desired_first, desired_second):
    first = desired_first % 25
    second = desired_second % 25

    if first < 0:
        first += 25
    if second < 0:
        second += 25
    return first, second


#adjusts length
def adjust_text(text):
    text = text.replace(' ', '')

    for i in xrange(len(text) - 1):
        if (text[i] == text[i + 1]) and (text[i] != 'x'):
            text[i + 1].replace('x')

    if len(text) % 2 != 0:
        text += 'x'

    return text


def adjust_password(password):
    add_pass = string.lowercase
    for letter in password:
        if add_pass.find(letter)>0:
            position = add_pass.find(letter)
            add_pass = add_pass[:position] + add_pass[position+1:]

        if 'j' in add_pass and 'i' not in add_pass:
            add_pass = ''.join(add_pass.split('j'))
        elif 'j' not in add_pass and 'i' in add_pass:
            add_pass = ''.join(add_pass.split('i'))

    if 'i' and 'j' in add_pass:
        add_pass = ''.join(add_pass.split('j'))
    return password + add_pass



if __name__ == "__main__":
    main()