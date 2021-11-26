import RPi.GPIO as GPIO
import os
import time

while True:
    try:
        GPIO.setmode(GPIO.BOARD)

        PIN_TRIGGER = 18
        PIN_ECHO = 16

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        time.sleep(2)

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)

        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print(distance)

        if distance <= 40:
            #os.system("vcgencmd display_power 0")
            print("menor que 40")
        elif distance > 40:
            print("maior que 40")
            #os.system("vcgencmd display_power 1")

    finally:
        GPIO.cleanup()
