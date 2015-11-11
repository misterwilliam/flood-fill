import collections
import unittest

# Implements a flood fill operation
# Example Usage:
# data = [ [0, 0, 1],
#          [1, 1, 1],
#          [0, 1, 1] ]
# GetFloodFillPath(Point(0, 0), data)  # returns set([Point(0,0), Point(0, 1)])

Point = collections.namedtuple('Point', ['x', 'y'])


def GenAdjacentPoints(origin):
    """Generates adjacent points to origin"""
    for i in [1, 0, -1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            yield Point(origin.x + j, origin.y + i)


def IsInBounds(point, width, height):
    """Returns if a point is within the bounds"""
    return 0 <= point.x < width and 0 <= point.y < height


def FindConnectedPointsWithSameColor(root, data, width, height):
    """Returns list of points connected to |root| that are the same color as root"""
    todo = collections.deque([root])
    seenPoints = set()
    seenPoints.add(root)
    sameColorPoints = set()
    startColor = data[root.x][root.y]
    while todo:
        currentPoint = todo.popleft()
        if data[currentPoint.x][currentPoint.y] == startColor:
            sameColorPoints.add(currentPoint)
            for adjacentPoint in GenAdjacentPoints(currentPoint):
                if adjacentPoint not in seenPoints and \
                       IsInBounds(adjacentPoint, width, height):
                    seenPoints.add(adjacentPoint)
                    todo.append(adjacentPoint)
    return sameColorPoints


def GetFloodFillPath(point, data):
    """Returns list of Point's to flood fill"""
    return FindConnectedPointsWithSameColor(point, data, len(data[0]), len(data))


# TESTS ------------------------------

class GenAdjacentPointsTest(unittest.TestCase):

    def test_Origin(self):
        adjacentPoints = [point for point in GenAdjacentPoints(Point(0,0))]
        self.assertEqual([Point(-1, 1), Point(0, 1), Point(1, 1),
                          Point(-1, 0), Point(1, 0),
                          Point(-1, -1), Point(0, -1), Point(1, -1)],
                         adjacentPoints)


class FindConnectedPointsWithSameColorTest(unittest.TestCase):

    def test_ExampleOne(self):
        data = [
            [0, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
        ]
        self.assertEqual(FindConnectedPointsWithSameColor(Point(0,0), data, 3, 3),
            set([Point(0,0), Point(0, 1)]))

    def test_ExampleTwo(self):
        data = [
            [0, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
        ]
        self.assertEqual(FindConnectedPointsWithSameColor(Point(1,1), data, 3, 3),
            set([Point(1,1), Point(1, 0), Point(0, 2), Point(1, 2), Point(2, 1),
                 Point(2, 2)]))


class FloodFillTest(unittest.TestCase):

    def test_Example(self):
        data = [ [0, 0, 1],
                 [1, 1, 1],
                 [0, 1, 1] ]
        floodPath = GetFloodFillPath(Point(0, 0), data)
        self.assertEqual(floodPath, set([Point(0,0), Point(0, 1)]))


if __name__ == '__main__':
    unittest.main()
