import utime
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
