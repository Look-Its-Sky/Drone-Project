from codrone_edu.drone import *
import os

class judedrone():
    dronee = None
    power = 1

    def __init__(self) -> None:
        self.dronee = Drone()
        self.dronee.pair()

    def takeOff(self):
        self.dronee.takeoff()

    def moveRight(self):
        print("Moving Right!")
        self.dronee.set_yaw(50)
        self.dronee.move(self.power)
        self.dronee.set_yaw(0)

    def moveLeft(self):
        print("Moving Left!")
        self.dronee.set_yaw(-50)
        self.dronee.move(self.power)
        self.dronee.set_yaw(0)

    def moveUp(self):
        print("Moving Up!")
        self.dronee.set_throttle(50)

    def moveDown(self):
        print("Moving Down!")
        self.dronee.set_throttle(-50)

    def moveForward(self):
        print("Moving Forward!")
        self.dronee.set_pitch(30)
        self.dronee.move(self.power)
        self.dronee.set_yaw(0)

    def moveBackward(self):
        print("Moving Backward!")
        self.dronee.set_pitch(-30)
        self.dronee.move(self.power)
        self.dronee.set_yaw(0)

    def land(self):
        print("Landing!")
        self.dronee.land()

    def __del__(self):
        self.dronee.close()