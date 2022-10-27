class judedrone():
    drone = None
    power = 1

    def __init__(self) -> None:
        self.drone = CoDrone.CoDrone()
        self.drone.pair(Drone.Nearest)

    def takeOff():
        self.drone.takeoff()

    def moveRight():
        print("Moving Right!")
        self.drone.set_yaw(50)
        self.drone.move(power)
        self.drone.set_yaw(0)

    def moveLeft():
        print("Moving Left!")
        self.drone.set_yaw(-50)
        self.drone.move(power)
        self.drone.set_yaw(0)

    def moveUp():
        print("Moving Up!")
        self.drone.set_throttle(20)
        wait(1)
        self.drone.set_throttle(0)

    def moveDown():
        print("Moving Down!")
        self.drone.set_throttle(-20)
        wait(1)
        self.drone.set_throttle(0)

    def moveForward():
        print("Moving Forward!")
        self.drone.set_pitch(30)
        self.drone.move(power)
        self.drone.set_yaw(0)

    def moveBackward():
        print("Moving Backward!")
        self.drone.set_pitch(-30)
        self.drone.move(power)
        self.drone.set_yaw(0)

    def land():
        print("Landing!")
        self.drone.land()

    def __del__(self):
        drone.close()