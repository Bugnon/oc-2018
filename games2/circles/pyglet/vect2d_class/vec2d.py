"""
Vec2D class

R. Holzer, 2019-02-20
"""

import math

class Vec2d(object):
    def __init__(self, x, y=None):
        if y==None:
            self.x, self.y = x
        else:
            self.x, self.y = x, y
    def __str__(self):
        return 'Vec2D({}, {})'.format(self.x, self.y)


if __name__ == '__main__':
    import unittest

    class UnitTestVec2d(unittest.TestCase):

        def setUp(self):
            pass

        def testCreation(self):
            a = Vec2d(11, 22)
            b = Vec2d([33, 44])
            print(a, b)
            self.assertTrue(a.x == 11 and a.y ==22)
            self.assertTrue(b.x == 33 and b.y ==44)


    unittest.main()
