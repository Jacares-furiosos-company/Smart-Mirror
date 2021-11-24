import screen_brightness_control as sbc
#import distance as dis
import time

while True:
    distanciaEncontrada = 40 #dis.verificaDistancia()

    if (distanciaEncontrada <= 40):
        sbc.set_brightness(100)
    elif (distanciaEncontrada > 40):
        sbc.set_brightness(1)
    time.sleep(3)


