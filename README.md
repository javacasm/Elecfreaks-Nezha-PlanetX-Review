## Nezha Inventor's Kit para micro:bit

Nuestros amigos de [micro-log](https://micro-log.com) y [Elecfreaks](https://elecfreaks.com) han tenido el detalle de enviarnos un [Nezha Inventor's Kit para micro:bit](https://www.micro-log.com/microbit/3563-nezha-inventor-s-kit-for-microbit.html) para que lo probemos. Os adelanto el resultado: me encanta.

Es una mezcla estupenda de kit electrónico: complentos y sensores para micro:bit y piezas de construcción, que nos va a permitir crear nuestros propios proyectos. Eso sí desde el principio nos proporcionan muchos ejemplos para aprender a usarlo.

Seguiremos probándolo, con lo que esta documentación irá creciendo.


### Revisión


[![Vídeo: Revisión del Nezha Inventos's Kit para micro:bit de Elecfreaks](https://img.youtube.com/vi/PyKDS6uPcSU/0.jpg)](https://youtu.be/PyKDS6uPcSU)



Se trata de un [Producto](https://www.elecfreaks.com/nezha-inventor-s-kit-for-micro-bit-without-micro-bit-board.html) de Elecfreaks pensado para desarrollar todo tipo de proyectos con micro:bit (no incluída en el kit), los sensores y actuadores incluidos y la gran cantidad de bloques de construcción (compatibles con Lego)

![](https://images.elecfreaks.com/wysiwyg/products/2020/EF08232/EF08232-008.jpg)

Es una placa de expansión para micro:bit creada por elecfreaks que nos permite conectar fácilmente a nuestra placa micro:bit sensores de diferentes tipos usando conectores de tipo RJ11 y también servos y motores.

En un lateral podemos conectar los típicos sensores y actuadores digitales (pulsadores, leds, ultrasonidos) en las clavijas rojas y analógicos (potenciómetros, sensor de humedad,...).

En el otro lateral podremos conectar sensores de tipo I2C, como por ejemplo acelerómetros o sensores atomósféricos (como el BME280).

![](https://www.elecfreaks.com/learn-en/_images/03444_01.png)

### Conexiones

* 4 x Conexiones RJ11 para módulos digitales (1,2,3,4) Marcados con etiqueta roja
* 2 x Conexiones RJ11 para módulos analógicos (1 y 2) Marcados con etiqueta amarilla
* 4 x Conexiones RJ11 para módulos I2C (IIC)
* 4 x Motores con conexión de 2 cables (con polaridad)
* 4 x Motores con conexión FisherTechnics
* 4 x Servos con conexión estándar de 3 hilos (Vcc, GND y Signal)
* 1 Altavoz conectado a P0
* Batería de 80mAh

La estructura de Nezha dispone de agujeros para fijarla a bloques de construcción compatibles con Lego


## Sensores PlanetX

Son muchos y muy variados los sensores disponibles en el formato llamado PlanetX. Podemos verlos en detalle en su [Documentación: PlanetX sensors](https://www.elecfreaks.com/learn-en/microbitplanetX/index.html)


### Sensores incluídos:

El Inventor's Kit incluye los siguientes sensores, hemos enlazado un ejemplo y los detalles técnicos de la página de documentación PlanetX de Elecfreaks.

* [Sensor de suelo](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05005.html)

![](https://www.elecfreaks.com/learn-en/_images/05005_01.png)


* [Sensor de distancia por ultrasonidos](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05007.html)

![](https://www.elecfreaks.com/learn-en/_images/05007_01.png)

* 3 x [Led](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05009.html) (rojo, amarillo y verde)

![](https://www.elecfreaks.com/learn-en/_images/05009_01.png)

* [Sensor de choque (final de carrera)](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05008.html)

![](https://www.elecfreaks.com/learn-en/_images/05008_01.png)

* [Potenciómetro](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05018.html)

![](https://www.elecfreaks.com/learn-en/_images/05018_01.png)

* [Siguelíneas](https://www.elecfreaks.com/learn-en/microbitplanetX/Plant_X_EF05019.html)

![](https://www.elecfreaks.com/learn-en/_images/05019_01.png)

### Programación

Como hemos dicho, podemos programar los sensores con bloques usando la extensión PlanetX de makecode o con python usando el [módulo PlanetX](https://github.com/lionyhw/PlanetX_MicroPython/archive/master.zip). Tenemos disponibles muchos ejemplos en [este enlace del github de elecfreaks](https://github.com/elecfreaks/learn-en/tree/master/microbitplanetX)

[![Vídeo: Proyecto sencillo con Nezha Inventor's Kit para micro:bit de Electrofreaks con bloques de MakeCode](https://img.youtube.com/vi/PtqHgtValnE/0.jpg)](https://youtu.be/PtqHgtValnE)


[Test Nezha](https://makecode.microbit.org/_YHgP9t55kUzm)


### Programación con bloques de Makecode

Para controlar los motores y servos usaremos la extensión Nezha de Makecode y para controlar los distintos sensores usaremos la extensión PlanetX de Makecode

Además de [la documentación](https://www.elecfreaks.com/learn-en/microbitExtensionModule/nezha.html) Elecfreaks nos proporciona un gran número de [ejemplos de programación con bloques](https://www.elecfreaks.com/learn-en/microbitKit/Nezha_Inventor_s_kit_for_microbit/index.html)

### Programación con micropython

También podemos programarla con micropython usando el [módulo PlanetX](https://github.com/lionyhw/PlanetX_MicroPython/archive/master.zip)

[Nezha documentation](https://www.elecfreaks.com/learn-en/microbitExtensionModule/nezha.html)

Este es un ejemplo sencillo de uso del módulo de Elecfreaks. Lamentablemente da problemas de memoria al usarlo en la micro:bit V1.5, pero funciona bien en la V2

```python
import enum # Definiciones de los puertos J1-J4
import trimpot # potenciometro
import nezha # control de servos y motores
import led

def testMotores():
    nezha = nezha.NEZHA()
    nezha.set_motor(1,100)
    nezha.set_servo(1,90)

def testLedPot():
    pot = trimpot.TRIMPOT(enum.J1)
    ledRojo = led.LED(enum.J3)
    ledRojo.set_led(1,50) # Activa el led al 50%

while True:
    valorPot = pot.get_analog() # Entre 0 y 1023
    ledRojo.set_led(1,100*valorPot/1023)
```

#### Adaptación a micro:bit v1.5

Reduciendo el código al mínimo, eliminando imports que no se necesitan he conseguido una miniversión capaz de controlar leds, motores y servos desde un potenciómetro en una micro:bit v1.5

La base son estos 2 módulos que he llamado uNezha y uPlanetX (la u inicial se refieren a micro)

```python
# Simply funtional Nezha python API
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

```

y 

```python
# Simply funtional PlanetX  python API
# bassed in https://github.com/lionyhw/PlanetX_MicroPython

from microbit import pin1, pin2, pin13, pin15

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

```

Lo que nos permite controlar fácilmente la posición de un servo con un potenciómetro

```python
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
```

### Programación con bloques

Podemos programar nuestra micro:bit con la placa Nezha conectada con bloques usando la extensión PlanetX

[Ejemplos](https://www.elecfreaks.com/learn-en/microbitplanetX/ai/Plant_X_EF05035.html#samples)

A destacar el [ejemplo de seguimiento de cara](https://www.elecfreaks.com/learn-en/microbitplanetX/ai/Plant_X_EF05035%20_04.html)

### Programación con python

Para programarla en python usaremos el [siguiente paquete](https://github.com/lionyhw/EF_Produce_MicroPython/archive/master.zip). Tenemos disponible la documentación del [API en python](https://www.elecfreaks.com/learn-en/microbitplanetX/ai/Plant_X_EF05035.html#add-python-file)

Para ello tenemos que [instalarle el firmware adecuado](https://www.elecfreaks.com/learn-en/microbitplanetX/ai/Plant_X_EF05035.html#add-python-file)

[Documentación](https://github.com/elecfreaks/learn-en/tree/master/microbitplanetX/ai)

Todas las imágenes son cortesía de Elecfreaks


## AI Lens

Dentro de los sensores PlanetX (no incluído en el Inventor's Kit) existe uno que me ha parecido especialmente interesante. Es un [sensor inteligente con cámara y que se puede conectar con RJ11 a una entrada IIC](https://www.elecfreaks.com/learn-en/microbitplanetX/ai/index.html)

Este módulo es capaz de aprender y reconocer imágenes, caras, seguimiento de bolas, ...

![](https://www.elecfreaks.com/learn-en/_images/05035_01.png)

Esquema de conexión

![](https://www.elecfreaks.com/learn-en/_images/05035_03.png)

