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
    drivetrain.set_turn_velocity(100,PERCENT)
    drivetrain.drive_for(FORWARD, 600, MM)
    stop_project()
    monitor_sensor("distance.get_distance")


# VR threads — Do not delete
vr_thread(main())

