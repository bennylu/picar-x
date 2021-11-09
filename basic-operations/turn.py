#!/usr/bin/python3
import sys
sys.path.append(r'/opt/ezblock')

from picarmini import dir_servo_angle_calibration
from picarmini import set_dir_servo_angle
from picarmini import stop
from ezblock import delay

dir_servo_angle_calibration(0)

set_dir_servo_angle(30)
delay(1000)
set_dir_servo_angle(-30)
delay(1000)
set_dir_servo_angle(0)

stop()

print('done')
