#!/usr/bin/python3

"""Definition of unittests for square.py.


Unittest classes:
    TestSquare_init
    TestSquare_width
    TestSquare_x
    TestSquare_area 
    
"""

import unittest
from models.base import Base
from models.square import Square


class TestSquare_init(unittest.TestCase):
    """Unittests for Square class initialization."""

    def test_a1(self):
        self.assertIsInstance(Square(2, 3), Base)

    def test_a2(self):
        with self.assertRaises(TypeError):
            Square()

    def test_a3(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
                             

    def test_a4(self):
        r1 = Square(1, 2)
        r2 = Square(2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_a5(self):
        r1 = Square(1, 2, 4)
        r2 = Square(5, 6, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_a6(self):
        r1 = Square(1, 2, 3, 4)
        r2 = Square(2, 3, 4, 5)
        self.assertEqual(r1.id, r2.id - 1)

    def test_a7(self):
        self.assertEqual(9, Square(10, 0, 0, 9).id)

    def test_a9(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 0, 1, 1).__width)

    def test_a10(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 0, 1, 1).__width)

    def test_a11(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 4, 0, 1).__x)

    def test_a12(self):
        with self.assertRaises(AttributeError):
            print(Square(2, 4, 0, 1).__y)

    def test_a13(self):
        r = Square(7, 6, 8, 5)
        self.assertEqual(7, r.width)

    def test_a14(self):
        r = Square(7, 6, 8, 5)
        r.width = 12
        self.assertEqual(12, r.width)

    def test_a15(self):
        r = Square(7, 6, 8, 5)
        r.width = 10
        self.assertEqual(10, r.width)


class TestSquare_width(unittest.TestCase):
    """Unittests for testing initialization of Square width attribute."""

    def test_b1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 4)

    def test_b2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", 4)

    def test_b3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.1, 1)

    def test_b4(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 2)

    def test_b5(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_b6(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2)
    
    def test_b7(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 11)

    def test_b8(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_b9(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_width(unittest.TestCase):
    """Unittests for testing initialization of Square width attribute."""

    def test_c1(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 1)

    def test_c2(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inv", 1)

    def test_c3(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.1, 1)

    def test_c4(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 1)

    def test_c5(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3, 2)

    def test_c6(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 1)


class TestSquare_x(unittest.TestCase):
    """Unittests forSquare x attribute."""

    def test_d1(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None, 2)

    def test_d2(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "inv", 2)

    def test_d3(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, 8.1, 9)

class TestSquare_area(unittest.TestCase):
    """Unittests for area method of the Square class."""

    def test_e1(self):
        r = Square(5, 2, 0, 0)
        self.assertEqual(25, r.area())

    def test_e2(self):
        r = Square(6, 0, 0, 1)
        r.size = 6
        self.assertEqual(36, r.area())


if __name__ == "__main__":
    unittest.main()
