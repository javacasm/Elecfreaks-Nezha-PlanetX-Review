# Simply C - PlanetX / Nezha python API
# bassed in https://github.com/lionyhw/PlanetX_MicroPython & https://github.com/elecfreaks/pxt-nezha/blob/master/main.ts
from microbit import i2c

v = '0.5'

NEZHA_ADDR = 0x10

bInitNezha = False

def initNezha():
    global bInitNezha
    i2c.init()
    print('Init i2c')
    bInitNezha = True

def set_motor( motor, speed):
    """
        motor: 1 - 4
        speed: -100 - 100
    """
    global bInitNezha
    if bInitNezha == False:
        initNezha()

    if speed < 0:
        i2c.write(NEZHA_ADDR, bytearray([motor, 0x02, speed * -1, 0]))
    else:
        i2c.write(NEZHA_ADDR, bytearray([motor, 0x01, speed, 0]))


def set_servo(servo, angle):
    """
        servo 1 - 4
        angle 0 - 180
    """
    if bInitNezha == False:
        initNezha()
    i2c.write(NEZHA_ADDR, bytearray([0x09+servo , angle, 0, 0]))


