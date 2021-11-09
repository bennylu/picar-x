#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')

from picarmini import forward
from picarmini import backward
from picarmini import stop
from ezblock import delay

forward(50)
delay(1000)
backward(50)
delay(1000)
stop()

print('done')
