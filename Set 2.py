def shift_letter(letter, shift):

    clean_letter = letter.upper()[0]

    if clean_letter == " ":
        result = " "

    else:
        result = chr((ord(clean_letter) + shift - 65) % 26 + 65)

    return result
    

def caesar_cipher(message, shift):

    clean_message = message.upper()
    expanded_message = [ord(element) for element in clean_message]
    shifted_numbers = [32 if expanded_message[i] == 32 else (expanded_message[i] + shift - 65) % 26 + 65 for i in range(len(expanded_message))]
    shifted_letters = [chr(shifted_numbers[i]) for i in range(len(shifted_numbers))]
    result = ''.join(shifted_letters)
    
    return result
    

def shift_by_letter(letter, letter_shift):

    letter = letter.upper()[0]
    letter_shift = ord(letter_shift.upper()[0]) - 65

    if letter == " ":
        result = " "

    else:
        result = chr((ord(letter) + letter_shift - 65) % 26 + 65)

    return result


def vigenere_cipher(message, key):

    clean_message = message.upper()
    clean_key = key.upper()
    
    adjusted_key = clean_key * ((len(clean_message)//len(clean_key)) + 1)
    final_key = adjusted_key[0:len(clean_message)]

    expanded_message = [ord(element) for element in clean_message]
    expanded_key = [ord(element) for element in final_key]
    shifted_numbers = [32 if expanded_message[i] == 32 else ((expanded_message[i] + expanded_key[i] - 65 - 65) % 26) + 65 for i in range(len(expanded_message))]
    shifted_message = [chr(shifted_numbers[i]) for i in range(len(shifted_numbers))]
    result = ''.join(shifted_message)

    return result

def scytale_cipher(message, shift):

    if len(message) % shift == 0:
        clean_message = message
    else:
        clean_message = message + "_" * (shift - len(message) % shift)

    result = ""

    for i in range(len(clean_message)):
        ciphered = clean_message[(i // shift) + (len(clean_message) // shift) * (i % shift)]
        result += ciphered

    return result

def scytale_decipher(message, shift):

    message_list_form = list(message)
    sublist_quantity = len(message) / shift
    listnumber = 0
    result = []
    fstr=""
    x=0
    while listnumber < sublist_quantity:
        sublist = message_list_form[shift * listnumber : shift * (listnumber + 1)]
        listnumber += 1
        result.append(sublist) 

    
    concatenated_list =''.join([item for sublist in zip(*result) for item in sublist])

    return concatenated_list
