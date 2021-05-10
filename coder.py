def string_encoding(string):
    """

    Arguments:

    string: the string which do encode

    This function returns the chars coded list.

    """

    chars_code_list = []
    for i in range(len(string)):
        if len(chars_code_list) == 0:
            chars_code_list.append(ord(string[i]))
        else:
            chars_code_list.append(ord(string[i]) - ord(string[i - 1]))
    return chars_code_list


def string_decoding(chars_code_list):

    """

    Arguments:

    string: the string which do decode
    shift: the shifting value

    This function returns the string.

    """

    string = ""
    for i in range(len(chars_code_list)):
        if len(string) == 0:
            string += chr(chars_code_list[i])
        else:
            string += chr(chars_code_list[i] + ord(string[i - 1]))
    return string


if __name__ == "__main__":
    # Inputs
    string = input("\nAdjon meg egy szót a kódoláshoz: ")

    # Encoding
    encoded_string = string_encoding(string)

    # Decoding
    decoded_string = string_decoding(encoded_string)

    print(f"A megadott szöveg: {string}")
    print(f"A kódolt szöveg: {encoded_string}")
    print(f"A dekódolt szöveg: {decoded_string}")
