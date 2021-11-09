#/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')

from ezblock import Pin
from ezblock import Ultrasonic
from ezblock import delay

pin_D0 = Pin('D0')
pin_D1 = Pin('D1')

for i in range(0, 100):
    distance = Ultrasonic(pin_D0, pin_D1).read()
    print(distance)
    delay(100)

print('done')
