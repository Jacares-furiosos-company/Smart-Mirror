import RPi.GPIO as GPIO
import time
import os

while True:
    try:
        GPIO.setmode(GPIO.BOARD)
        pinTrigger = 18
        pinEcho = 16

        GPIO.setup(pinTrigger, GPIO.OUT)
        GPIO.setup(pinEcho, GPIO.IN)

        GPIO.output(pinTrigger, GPIO.LOW)
        GPIO.output(pinTrigger, GPIO.HIGH)

        time.sleep(0.00001)
        GPIO.output(pinTrigger, GPIO.LOW)

        while GPIO.input(pinEcho)==0:
            pulseStartTime = time.time()
        while GPIO.input(pinEcho)==1:
            pulseEndTime = time.time()

        pulseDuration = pulseEndTime - pulseStartTime
        distance = round(pulseDuration * 17150, 2)

        print("Distance: %.2f cm" % (distance))

        if distance <= 50:
            os.system("vcgencmd display_power 1")
            print("menor que 50")
        elif distance > 50:
            print("maior que 50")
            os.system("vcgencmd display_power 0")
    except:
        pass
    finally:
        GPIO.cleanup()
        time.sleep(3)