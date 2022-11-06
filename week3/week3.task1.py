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

    pen.set_pen_color(RED)
    pen.move(DOWN)
    
    #for move in range(4):
        #drivetrain.drive_for(FORWARD, 200, MM)
        #drivetrain.turn_for(RIGHT, 90, DEGREES)
    i = 0
    brain.print("sonuc :",i)
    brain.new_line()
    while i<4:
        drivetrain.drive_for(FORWARD, 200, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        i += 1
        brain.print("sonuc :",i)
        brain.new_line()
    brain.print("loop is finished")
    
    

# VR threads — Do not delete
vr_thread(main())
