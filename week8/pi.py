from random import random


def find_pi(count_of_points: int) -> float:
    points_inside = 0
    for i in range(0, count_of_points):
        x, y = random(), random()
        if (x*x + y*y)**0.5 <= 1.0:
            points_inside += 1

    return 4 * points_inside / count_of_points
