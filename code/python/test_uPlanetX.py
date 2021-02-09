import uPlanetX

v = '0.5'

def testLedPot():
    print('Pot in J1 - Led in J3')
    while True:
        valorPot = uPlanetX.get_analog(1) # Entre 0 y 1023
        uPlanetX.set_led(3,valorPot)

