import screen_brightness_control as sbc

distanciaEncontrada = 40 #dis.verificaDistancia()

if (distanciaEncontrada <= 40):
    sbc.set_brightness(100)
elif (distanciaEncontrada > 40):
    sbc.set_brightness(1)

print(sbc.get_brightness())
