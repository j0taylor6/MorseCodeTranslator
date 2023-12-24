# Morse Code Translator

# Dictionaries

import winsound
import time

MorseToEnglish = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'
}

EnglishToMorse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
}

# Translation Functions
def translate_morse_to_english(input_text):
    input_text = input_text.upper()
    morse_code_words = input_text.split(' ')
    english_text = ""
    for ch in morse_code_words:
        if ch in MorseToEnglish:
            english_text = english_text +  MorseToEnglish[ch] + ' '
        else:
            english_text = english_text + "?"
    return english_text

def translate_english_to_morse(input_text):
    input_text = input_text.upper()
    morse_text = ""
    for ch in input_text:
        if ch == ' ':
            morse_text += ' / '
        elif ch in EnglishToMorse:
            morse_text += EnglishToMorse[ch] + ' '
        else:
            morse_text += '? '
    return morse_text

# play morse code sound

def play_morse_code(morse_code):
    dot_length = 200  # milliseconds
    dash_length = 600
    space_length = 200
    word_space_length = 1400
    frequency = 1000  # Hz

    for char in morse_code:
        if char == '.':
            winsound.Beep(frequency, dot_length)
        elif char == '-':
            winsound.Beep(frequency, dash_length)
        elif char == ' ':
            time.sleep(space_length / 1000.0)
        elif char == '/':
            time.sleep(word_space_length / 1000.0)
        else:
            continue
        time.sleep(space_length / 1000.0)

# user Input
GetTranslationChoice = input("Do you want to translate:\n1. Morse-code To English\n2. English To Morse-code\n")
GetTranslationInput = input("Provide the text for conversion: ")

# print Translation
if GetTranslationChoice == "1":
    englishText = translate_morse_to_english(GetTranslationInput)
    print(englishText)
elif GetTranslationChoice == "2":
    morseCode = translate_english_to_morse(GetTranslationInput)
    print(morseCode)
    play_morse_code(morseCode)
else:
    print("Translation choice is neither 1 nor 2")



