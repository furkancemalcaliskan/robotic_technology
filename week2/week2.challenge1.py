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

# Add project code in "main"
def main():
    drivetrain.set_drive_velocity(100,PERCENT)
    drivetrain.turn_for(LEFT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 800, MM)
    for rotation in range(3):
        drivetrain.turn_for(RIGHT,90,DEGREES)
        drivetrain.drive_for(FORWARD, 1600, MM)
    drivetrain.turn_for(RIGHT,90,DEGREES)
    drivetrain.drive_for(FORWARD,800,MM)
    drivetrain.turn_for(RIGHT,90,DEGREES)
    drivetrain.drive_for(FORWARD, 1600, MM)

    stop_project()

# VR threads — Do not delete
vr_thread(main())
