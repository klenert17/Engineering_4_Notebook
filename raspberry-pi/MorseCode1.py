import time
## I used large portions of Rivers's work in this assignment. Here is a link to their notebook. https://github.com/rivques/Engr4Code
#These are all the letters and numbers translated
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
while True:
    user_input = input("Enter the string to translate, or type '-q' to quit. ") #prints out a space for you to type words in moniter
    user_input = user_input.upper()
   
    if user_input == "-Q":
        break #everything stops if you type -q in
    morse_translation = ""
    translation_good = True
   
    for letter in user_input:
        if letter == " ":
            morse_translation += "/" #if you put a space, it makes a break
        else:
            try:
                morse_translation += MORSE_CODE[letter] + " "
            except KeyError:
                print(f"Unsupported character \"{letter}\" used. Please try again.") #if you put in a letter that isn't in the above definitions, it tells you
                translation_good = False
                break
 
    if translation_good:
        print(morse_translation) 
            