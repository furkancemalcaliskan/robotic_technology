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



def recFunc(length,width,speed):
    
    for move in range(2):
        #length
        drivetrain.set_drive_velocity(speed,PERCENT)
        drivetrain.drive_for(FORWARD, length, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)

        #width
        drivetrain.set_drive_velocity(speed,PERCENT)
        drivetrain.drive_for(FORWARD, width, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)

def main():
    global setNumber
    setNumber = 0

    brain.timer_reset()

    pen.move(DOWN)
    pen.set_pen_color(BLUE)
    monitor_variable("setNumber")
    brain.clear()

    while True:
        recFunc(500,250,100)
        brain.print("Loop Counter: ",setNumber)
        setNumber += 1
        brain.new_line()
    stop_project()
# VR threads — Do not delete
vr_thread(main())
