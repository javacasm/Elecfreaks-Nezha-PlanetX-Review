# Simply C - PlanetX / Nezha python API
# bassed in https://github.com/lionyhw/PlanetX_MicroPython
from microbit import pin1, pin2, pin13, pin15,

v = '0.6'

# internal connection 
j_pins = [pin1,pin2, pin13, pin15]


def set_led(jPin, brightness):
    """
    jPin digital port 1 - 4 
    brightness  0 - 1023
    """
    j_pins[jPin-1].write_analog(brightness)

def get_analog(jPin):
    """
    jPin analog Port 1 - 2
    return 0 - 1023 value
    """
    return j_pins[jPin-1].read_analog()
