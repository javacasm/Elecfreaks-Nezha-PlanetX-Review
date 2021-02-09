# uNezha & uPlanetX test
# @javacasm
# https://github.com/javacasm/Elecfreaks-Nezha-PlanetX-Review/tree/master/code/python
# bassed in https://github.com/lionyhw/PlanetX_MicroPython & https://github.com/elecfreaks/pxt-nezha/blob/master/main.ts

import utime
import uNezha
import uPlanetX

v = '0.5'

def testPotServor():
    print('Pot in J1 - Servo in S1')
    lastValue = 0
    while True:
        val = uPlanetX.get_analog(1)
        if val != lastValue:
            angle = int(180*val/1023)
            print('pot:{} angle:{}'.format(val, angle))
            uNezha.set_servo(1,angle)
            lastValue = val
        utime.sleep(0.1)
