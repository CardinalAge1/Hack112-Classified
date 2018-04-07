def isLeft(lines, left, right, orientation):
    wallDist = 50
    if orientation == "left":
        for line in lines:
            if (min(line[0][0], line[1][0]) <= left[0] <= max(line[0][0], line[1][0]) and
                    0 <= left[1] - line[0][1] <= wallDist): return True
    elif orientation == "right":
        for line in lines:
            if (min(line[0][0], line[1][0]) <= right[0] <= max(line[0][0], line[1][1]) and
                0 <= left[1] - line[0][1] <= wallDist): return True
