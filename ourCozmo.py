
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


def cozmo_left(robot: cozmo.robot.Robot):
    robot.turn_in_place(degrees(90)).wait_for_completed()


def cozmo_right(robot: cozmo.robot.Robot):
    robot.turn_in_place(degrees(-90)).wait_for_completed()


def cozmo_straight(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(150), speed_mmps(5000)
                         ).wait_for_completed()


def cozmo_deadend(robot: cozmo.robot.Robot):
    robot.turn_in_place(degrees(180)).wait_for_completed()


def run(type):
    if type == "straight":
        cozmo.run_program(cozmo_straight)
    if type == "left":
        cozmo.run_program(cozmo_left)
    if type == "right":
        cozmo.run_program(cozmo_right)
    if type == "deadend":
        cozmo.run_program(cozmo_deadend)
