
"""
Python file containing functions to encrypt and decipher ASCII latin alphabet characters in a string using caesar's shift cipher.
"""

def caesar_shift_cipher(string, shift=0):
    """
    :param string: The string to encrypt
    :param shift: The integer used to shift letters in the string to encrypt
    :return encrypted_string: The encrypted string
    """
    encrypted_string = str()
    shift %= 26
    for char in string:
        ASCII_pos = ord(char)
        ASCII_ord = ASCII_pos + shift
        if (65 <= ASCII_pos <= 90 and ASCII_ord > 90) or (97 <= ASCII_pos <= 122 and ASCII_ord > 122):
            # The character is either : an uppercase letter and is after Z, or a lower  case letter, and is after Z.
            ASCII_ord -= 26
        if 65 <= ASCII_pos <= 90 or 97 <= ASCII_pos <= 122:  # The character is an upper case or a lower case letter
            encrypted_string += chr(ASCII_ord)
        else:  # The character is not a letter
            encrypted_string += char
    return encrypted_string


def caesar_shift_decipher(encrypted_string):
    """
    This function deciphers a string using caesar's shift cipher
    :param encrypted_string: The string to decipher.
    :return deciphered_strings_list: A list with tuples of 2 elements : the deciphered string and the shift used to get the encrypted string from the deciphered string.
    """
    deciphered_strings_list = list()
    for shift in range(1, 26):  # The message is encrypted for each possible shift
        deciphered_string = str()
        for char in encrypted_string:
            ASCII_pos = ord(char)
            ASCII_ord = ASCII_pos + shift
            if (65 <= ASCII_pos <= 90 and ASCII_ord > 90) or (97 <= ASCII_pos <= 122 and ASCII_ord > 122):
                ASCII_ord -= 26
            if 65 <= ASCII_pos <= 90 or 97 <= ASCII_pos <= 122:
                deciphered_string += chr(ASCII_ord)
            else:
                deciphered_string += char
        deciphered_strings_list.append((deciphered_string, 26-shift))
    return deciphered_strings_list


# Tests :
results = caesar_shift_cipher("Veni, Vidi, Vici.", 5)
print("Caesar Shift Cipher : 'Veni, Vidi, Vici.' --> '{}'".format(results))

results = caesar_shift_decipher("Ajsn, Anin, Anhn.")
print("Caesar Shift Decipher :")
for result in results:
    print("'Ajsn, Anin, Anhn.' --> '{}'".format(result))


