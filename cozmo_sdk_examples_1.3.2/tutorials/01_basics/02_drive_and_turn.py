#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Drive And Turn

Make Cozmo drive forwards and then turn 90 degrees to the left.
'''
import pygame
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
pygame.init()


from tkinter import *

####################################
# customize these functions
####################################


def init(data):
    # load data.xyz as appropriate
    pass


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    if event.keysym == "Up":
        robot.drive_straight(distance_mm(10), speed_mmps(5000)
                             ).wait_for_completed()


def redrawAll(canvas, data):
    # draw in canvas
    pass

####################################
# use the run function as-is
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(400, 200)
robot.drive_straight(distance_mm(10), speed_mmps(5000)
                     ).wait_for_completed()

# Turn 90 degrees to the left.
# Note: To turn to the right, just use a negative number.
robot.turn_in_place(degrees(9)).wait_for_completed()
