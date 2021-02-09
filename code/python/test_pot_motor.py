# uNezha & uPlanetX test
# @javacasm
# https://github.com/javacasm/Elecfreaks-Nezha-PlanetX-Review/tree/master/code/python
# bassed in https://github.com/lionyhw/PlanetX_MicroPython & https://github.com/elecfreaks/pxt-nezha/blob/master/main.ts

import utime-
import uNezha
import uPlanetX

v = '0.5'

def testPotMotor():
    lastValue = 0
    print('Pot in J1 - Led in J3')
    while True:
        val = uPlanetX.get_analog(1)
        if val != lastValue:
            speed = int(100*val/1023)
            print('pot:{} speed:{}'.format(val, speed))
            uNezha.set_motor(1,speed)
            lastValue = val
        utime.sleep(0.1)
