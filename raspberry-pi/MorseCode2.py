#type: ignore
## I used large portions of Rivers's work in this assignment. Here is a link to their notebook. https://github.com/rivques/Engr4Code


import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP1) #where the LED is connected
led.direction = digitalio.Direction.OUTPUT


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
CHAR_DELAYS = {
    modifier = 0.25
    dot_time = 1*modifier
    dash_time = 3*modifier
    between_taps = 1*modifier
    between_letters = 3*modifier
    between_words = 7*modifier}

while True:

    character_input = input("Enter the string to translate, or type '-q' to quit. ") #prints out a space for you to type words in moniter

    character_input = character_input.upper()
    if character_input == "-Q":
        break #everything stops if you type -q in
    morse_translation = ""
    valid_translation = True #approves the characters put in
   
   
    for letter in character_input:
        if letter == " ":
            morse_translation += "/" #if you put a space, it makes a break
        else:
            try:
                morse_translation += MORSE_CODE[letter] + " "
            except KeyError:
                print(f"Unsupported character \"{letter}\" used. Please try again.") #if you put in a letter that isn't in the above definitions, it tells you
                translation_good = False
                break #everything stop
    
    
    if valid_translation:
        print(morse_translation)
        for pulse in morse_translation:
            on_delay, off_delay = CHAR_DELAYS[pulse]
            if on_delay == 0: # bypass ever turning the LED on
                time.sleep(off_delay)
            else:
                led.value = True
                time.sleep(on_delay)
                led.value = False
                time.sleep(off_delay)
            