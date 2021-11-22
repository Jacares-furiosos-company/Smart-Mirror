import RPi.GPIO as GPIO
import time


def verificaDistancia():
    try:
        GPIO.setmode(GPIO.BOARD)
        pinTrigger = 18
        pinEcho = 16

        GPIO.setup(pinTrigger, GPIO.OUT)
        GPIO.setup(pinEcho, GPIO.IN)

        GPIO.output(pinTrigger, GPIO.LOW)
        GPIO.output(pinTrigger, GPIO.HIGH)

        GPIO.output(pinTrigger, GPIO.LOW)

        while GPIO.input(pinEcho) == 0:
            pulseStartTime = time.time()
        while GPIO.input(pinEcho) == 1:
            pulseEndTime = time.time()

        pulseDuration = pulseEndTime - pulseStartTime
        distance = round(pulseDuration * 17150, 2)

        print("Distance: %.2f cm" % (distance))

    finally:
        GPIO.cleanup()
        return distance
