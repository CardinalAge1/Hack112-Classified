def isLeft(lines, left, right, orientation):
    wallDist = 50
    if orientation == "up":
        for line in lines:
            if (min(line[0][1], line[1][1]) <= left[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= left[0] - line[0][0] <= wallDist):
                    return True
    if orientation == "down":
        for line in lines:
            if (min(line[0][1], line[1][1]) <= left[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= line[0][0] - left[0] <= wallDist):
                    return True


def isRight(lines, left, right, orientation):
    wallDist = 50
    if orientation == "up":
        for line in lines:
            if (min(line[0][1], line[1][1]) <= right[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= line[0][0] - right[0] <= wallDist):
                    return True
    if orientation == "down":
        for line in lines:
            if (min(line[0][1], line[1][1]) <= right[1]
                    <= max(line[0][1], line[1][1])):
                if (0 <= right[0] - line[0][0] <= wallDist):
                    return True


def isFront(lines, left, right, orientation):
    wallDist = 50
    middle = (left[0] + right[0] / 2, left[1] + right[1] / 2)
    if orientation == "up":
        for line in lines:
            if (min(line[0][0], line[1][0]) <= middle[0]
                    <= max(line[0][0], line[1][0])):
                if (0 <= right[1] - line[0][1] <= wallDist):
                    return True
    if orientation == "down":
        for line in lines:
            if (min(line[0][0], line[1][0]) <= middle[0]
                    <= max(line[0][0], line[1][0])):
                if (0 <= right[1] - line[0][1] <= wallDist):
                    return True
