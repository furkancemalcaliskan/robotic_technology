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
    drivetrain.drive(FORWARD)
    pen.move(DOWN)
    while distance.get_distance(MM) > 1500:
        pen.set_pen_color(GREEN)
        wait(10,MSEC)
    brain.print("first loop ends at: ",distance.get_distance(MM)," mm")
    brain.new_line()

    while distance.get_distance(MM) > 1000:
        pen.set_pen_color(BLACK)
        wait(10,MSEC)
    brain.print("first loop ends at: ",distance.get_distance(MM)," mm")
    brain.new_line()

    while distance.get_distance(MM) > 500:
        pen.set_pen_color(BLUE)
        wait(10,MSEC)
    brain.print("first loop ends at: ",distance.get_distance(MM)," mm")
    brain.new_line()

    while distance.get_distance(MM) > 100:
        pen.set_pen_color(RED)
        wait(10,MSEC)
    brain.print("first loop ends at: ",distance.get_distance(MM)," mm")
    brain.new_line()

stop_project()

# VR threads — Do not delete
vr_thread(main())
