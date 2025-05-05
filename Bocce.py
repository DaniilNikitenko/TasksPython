# Bocce Description
# Bocce is a game played by two competing teams, with three types of balls.
# Each team has its own set of balls (in this kata red and black) and there is a neutral ball called the jack.
# The jack is thrown at the beginning of each round,
# followed by the players trying to throw their balls as closely to it as possible. The team with their balls closest to the jack wins the round!

# The number of points the winning team scores equals the number of their balls being closer to jack than any of the other team's balls:
# if the red team has 3 balls closer to jack than any of the black team's balls, they will win scoring 3 points.
# Equidistant balls on opposing teams will cancel out and neither team will
import math
from collections import defaultdict


def distance(point1, boccino):
    return round(
        math.sqrt((boccino[0] - point1[0]) ** 2 + (boccino[1] - point1[1]) ** 2), 3
    )


def bocce_score(balls):
    score = 0
    jack = ()
    result = defaultdict(list)
    for i in balls:
        if i["type"] == "jack":
            jack += i["distance"]
            balls.remove(i)
    for i in balls:
        if i["type"] == "black":
            result["black"].append(distance(i["distance"], jack))
        elif i["type"] == "red":
            result["red"].append(distance(i["distance"], jack))
    result = dict(result)
    index = 0
    redScores = 0
    blackScores = 0
    result["black"].sort()
    result["red"].sort()

    if result["black"][0] < result["red"][0]:
        for dist in result["black"]:
            if dist < result["red"][0]:
                blackScores += 1
            else:
                break
        return f"black scores {blackScores}"

    elif result["red"][0] < result["black"][0]:
        for dist in result["red"]:
            if dist < result["black"][0]:
                redScores += 1
            else:
                break
        return f"red scores {redScores}"

    else:
        return "No points scored"
