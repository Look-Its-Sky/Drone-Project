from distutils import text_file
from shutil import move
from jude_speech import *
from jude_codrone import *

if __name__ == "__main__":
    sr = speech_listener()
    drone = judedrone()

    while True:
        text = sr.listen()

        if "move up" in text:
            drone.moveUp()

        if "move down" in text:
            drone.moveDown()

        if "move left" in text:
            drone.moveLeft()

        if "move right" in text:
            drone.moveRight()

        if "move forward" in text:
            drone.moveForward()

        if "move backward" in text:
            drone.moveBackward()

        if "land" in text:
            drone.land()

        if "take off" in text:
            drone.takeOff()