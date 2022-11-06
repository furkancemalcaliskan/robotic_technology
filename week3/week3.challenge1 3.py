# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Library imports
from vexcode import *

def castleCrasher(speed):
    while True:
        wait(5, MSEC)
        drivetrain.set_drive_velocity(speed, PERCENT)
        drivetrain.set_turn_velocity(speed, PERCENT)
        while True:
            while not down_eye.detect(RED):
                wait(5, MSEC)
                if distance.found_object():
                    drivetrain.drive(FORWARD)
                else:
                    drivetrain.turn(RIGHT)

            drivetrain.drive_for(FORWARD, 80, MM)
            drivetrain.drive_for(REVERSE, 200, MM)
            drivetrain.turn_for(RIGHT, random.randint((30 - 1), 70), DEGREES)
      
def main():
    castleCrasher(100)
# VR threads — Do not delete
vr_thread(main())
