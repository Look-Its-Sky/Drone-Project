from jude_speech import *
from jude_codrone import *
import atexit

def onExit():
    dronee.land()

if __name__ == "__main__":
    sr = speech_listener()
    dronee = judedrone()

    atexit.register(onExit)

    while True:
        text = sr.listen()

        if "up" in text:
            dronee.moveUp()

        if "down" in text:
            dronee.moveDown()

        if "left" in text:
            dronee.moveLeft()

        if "right" in text:
            dronee.moveRight()

        if "forward" in text:
            dronee.moveForward()

        if "backward" in text:
            dronee.moveBackward()

        if "land" in text:
            dronee.land()

        if "take off" or "takeoff" in text:
            dronee.takeOff()