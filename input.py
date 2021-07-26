import time
import board
import busio
import adafruit_mpr121

i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

zero_has_changed = 1
one_has_changed = 1
two_has_changed = 1
three_has_changed = 1

while True:
    if mpr121[0].value and zero_has_changed == 1:
        print("0")
        zero_has_changed = 0
        one_has_changed = 1
        two_has_changed = 1
        three_has_changed = 1
    if mpr121[1].value and one_has_changed == 1:
        print("1")
        zero_has_changed = 1
        one_has_changed = 0
        two_has_changed = 1
        three_has_changed = 1
    if mpr121[2].value and two_has_changed == 1:
        print("2")
        zero_has_changed = 1
        one_has_changed = 1
        two_has_changed = 0
        three_has_changed = 1
    if mpr121[3].value and three_has_changed == 1:
        print("3")
        zero_has_changed = 1
        one_has_changed = 1
        two_has_changed = 1
        three_has_changed = 0
