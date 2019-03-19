import pyglet, math


def distance(point_1=(0, 0), point_2=(0, 0)):
    """
    Returns the distance between two points
    :return: The distance between the two supplied points
    """
    #TODO: Is this the best way to do this?
    return math.sqrt(
        (point_1[0] - point_2[0]) ** 2 +
        (point_1[1] - point_2[1]) ** 2
    )