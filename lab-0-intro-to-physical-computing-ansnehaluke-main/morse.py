'''
morse.py
A program that generates Morse Code beeps
using a buzzer to communicate a phrase.
The phrase is: <YOUR PHRASE>
Author: <YOUR NAME>
Date: <DATE>
'''

# from picozero import Buzzer 
# pico_buzz = Buzzer(5)
# pico_buzz.off()

# from time import sleep

#for "cat"

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.7)

# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.3)
# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.5)



#for "dog"

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.3)

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.3)

# pico_buzz.off()
# sleep(0.3)
# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)

#For "owl"

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.3)

# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.3)

# pico_buzz.off()
# sleep(0.3)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)

# pico_buzz.on()
# sleep(0.3)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)
# pico_buzz.on()
# sleep(0.1)
# pico_buzz.off()
# sleep(0.1)

# Using Pico to do the morse code and play three words with three letters (cat, dog, owl)
# first import buzzer and pico 
from picozero import Buzzer
from time import sleep

# use 5 as the wire is places at 5 in Pico hardware
buzzer = Buzzer(5)

# Define durations
DOT_DURATION = 0.1       # "." is 0.1 seconds
DASH_DURATION = 0.3      # "-" is 0.3 seconds
PAUSE_DURATION = 0.3     # pause between parts of a letter
SPACE_DURATION = 0.7     # space between letters

# defining the function to use the duaration code
def play_morse_word(word):
    for symbol in word:
        if symbol == ".":
            buzzer.on()
            sleep(DOT_DURATION)
            buzzer.off()
            sleep(0.1)
        elif symbol == "-":
            buzzer.on()
            sleep(DASH_DURATION)
            buzzer.off()
            sleep(0.1)
        elif symbol == " ":
            sleep(PAUSE_DURATION)
        elif symbol == " / ":
            sleep(SPACE_DURATION)

# Play Morse code for the line
morse_line = "-.-. .- - / -.. --- --. / --- .-- .-.."   # the line is: cat dog owl

# calling the function 
play_morse_word(morse_line)
