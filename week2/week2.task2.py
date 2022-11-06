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
    #drivetrain.turn_for(LEFT, 90, DEGREES)
    #drivetrain.turn_to_heading(270, DEGREES)
    drivetrain.turn_to_rotation(270, DEGREES)

    drivetrain.set_drive_velocity(100,PERCENT)
    drivetrain.drive_for(FORWARD, 800, MM)
    stop_project()

# VR threads — Do not delete
vr_thread(main())
