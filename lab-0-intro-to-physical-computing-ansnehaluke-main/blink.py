'''
blink.py
A simple program that blinks an LED on the
Pico board three times.
Author: <YOUR NAME>
Date: <DATE>
'''

# to make it blink three times 
from picozero import PicoLED
pico_led = PicoLED()
pico_led.toggle()
from time import sleep

pico_led.on()
sleep(3)
pico_led.off()
sleep(3)
pico_led.on()
sleep(3)
pico_led.off()
sleep(3)
pico_led.on()
sleep(3)
pico_led.off()
sleep(3)
