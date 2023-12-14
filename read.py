import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        print('Place card on Reader')
        id, text = reader.read()
        print('ID: {}'.format(id))
        print('Text: {}'.format(text))

except: # use Ctr+C to terminate the programm
    GPIO.cleanup()
    print('GPIO Good to Go')