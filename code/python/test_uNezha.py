# uNezha & uPlanetX test
# @javacasm
# https://github.com/javacasm/Elecfreaks-Nezha-PlanetX-Review/tree/master/code/python
# bassed in https://github.com/lionyhw/PlanetX_MicroPython & https://github.com/elecfreaks/pxt-nezha/blob/master/main.ts

import uNezha
import utime

v = '0.5'

def testMotores():
    print('Motor in M1 - Servo in S1')
    uNezha.set_motor(1,50)
    utime.sleep(1)
    uNezha.set_motor(1,100)
    utime.sleep(1)
    uNezha.set_motor(1,0)
    uNezha.set_servo(1,90)
    utime.sleep(1)
    uNezha.set_servo(1,0)
    utime.sleep(1)
    uNezha.set_servo(1,180)
    
