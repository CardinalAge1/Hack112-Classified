import ourCozmo


def isLeft(lines, left, right, orientation):
    wallDist = 20
    if orientation == 0:  # up
        for line in lines:
            if (min(line[0][1], line[1][1]) <= left[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= left[0] - line[0][0] <= wallDist):
                    return True
    if orientation == 2:  # down
        for line in lines:
            if (min(line[0][1], line[1][1]) <= left[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= line[0][0] - left[0] <= wallDist):
                    return True
    if orientation == 3:  # left
        for line in lines:
            if (min(line[0][0], line[1][0]) <= left[0] <= max(line[0][0], line[1][0]) and
                    0 <= left[1] - line[0][1] <= wallDist):
                return True
    elif orientation == 1:  # right
        for line in lines:
            if (min(line[0][0], line[1][0]) <= left[0] <= max(line[0][0], line[1][0]) and
                    0 <= left[1] - line[0][1] <= wallDist):
                return True


def isRight(lines, left, right, orientation):
    wallDist = 20
    if orientation == 0:
        for line in lines:
            if (min(line[0][1], line[1][1]) <= right[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= line[0][0] - right[0] <= wallDist):
                    return True
    if orientation == 2:
        for line in lines:
            if (min(line[0][1], line[1][1]) <= right[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= right[0] - line[0][0] <= wallDist):
                    return True
    if orientation == 3:
        for line in lines:
            if (min(line[0][0], line[1][0]) <= right[0]
                    <= max(line[0][0], line[1][0])):
                if (0 <= right[1] - line[0][1] <= wallDist):
                    return True
    if orientation == 1:
        for line in lines:
            if (min(line[0][0], line[1][0]) <= right[0]
                    <= max(line[0][0], line[1][0])):
                if (0 <= line[0][1] - right[1] <= wallDist):
                    return True


def isFront(lines, left, right, orientation):
    wallDist = 20
    middle = ((left[0] + right[0]) / 2, (left[1] + right[1]) / 2)
    if orientation == 0:
        for line in lines:
            if (min(line[0][0], line[1][0]) <= middle[0]
                    <= max(line[0][0], line[1][0])):
                if (0 <= middle[1] - line[0][1] <= wallDist):
                    return True
    if orientation == 2:
        for line in lines:
            if (min(line[0][0], line[1][0]) <= middle[0]
                    <= max(line[0][0], line[1][0])):
                if (0 <= line[0][1] - middle[1] <= wallDist):
                    return True
    if orientation == 3:
        for line in lines:
            if (min(line[0][1], line[1][1]) <= middle[0]
                    <= max(line[0][1], line[1][1])):
                if (0 <= middle[0] - line[0][0] <= wallDist):
                    return True
    if orientation == 1:
        for line in lines:
            if (min(line[0][1], line[1][1]) <= middle[0]
                    <= max(line[0][1], line[1][1])):
                if (0 <= line[0][0] - middle[0] <= wallDist):
                    return True


def solveMazeLeft(lines, left, right, orientation):
    if not isLeft(lines, left, right, orientation):
        ourCozmo.run("left")
        return (orientation - 1) % 4
    elif not isFront(lines, left, right, orientation):
        ourCozmo.run("straight")
        return orientation
    elif not isRight(lines, left, right, orientation):
        ourCozmo.run("right")
        return (orientation + 1) % 4
    else:
        ourCozmo.run("deadend")
        return (orientation + 2) % 4
