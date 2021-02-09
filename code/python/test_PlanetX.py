import uPlanetX

def testLedPot():
    while True:
        valorPot = uPlanetX.get_analog(1) # Entre 0 y 1023
        uPlanetX.set_led(3,valorPot)

