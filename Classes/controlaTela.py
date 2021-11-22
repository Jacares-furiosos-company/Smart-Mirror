import screen_brightness_control as sbc
import time

while True:
    distanciaEncontrada = dis.verificaDistancia()

    if (distanciaEncontrada <= 40):
        sbc.set_brightness(100)
    elif (distanciaEncontrada > 40):
        sbc.set_brightness(1)
    time.sleep(3)


