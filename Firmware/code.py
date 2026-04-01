import board
import digitalio
import time
import random

led_pins = [board.D3, board.D4, board.D5]
leds = []
for pin in led_pins:
    led = digitalio.DigitalInOut(pin)
    led.direction = digitalio.Direction.OUTPUT
    leds.append(led)

sw_pins = [board.D0, board.D1, board.D2]
switches = []
for pin in sw_pins:
    sw = digitalio.DigitalInOut(pin)
    sw.direction = digitalio.Direction.INPUT
    sw.pull = digitalio.Pull.UP
    switches.append(sw)

def led_swipe():
    for led in leds:
        led.value = True
        time.sleep(0.1)
        led.value = False

led_swipe()

mode = 0
print("Fidget Toy Active!")

while True:
    s1 = not switches[0].value
    s2 = not switches[1].value
    s3 = not switches[2].value

    leds[0].value = s1
    leds[1].value = s2
    leds[2].value = s3

    if s1 and s2 and s3:
        for _ in range(5):
            random.choice(leds).value = True
            time.sleep(0.05)
            for l in leds: l.value = False
            time.sleep(0.05)
            
    time.sleep(0.01) 
    
    # Written by @DevX-Dragon 010426-1342 to 010326-1405
    