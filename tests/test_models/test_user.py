#!/usr/bin/python3

"""Definition for Base.py unittests"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


"""Defines unittests for base.py.

    unittest classes

    TestBase_init
    TestBase_to_json_string
    TestBase_from_json_string
    TestBase_create
"""   

class TestBase_init(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_a1(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_a2(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_a3(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_a4(self):
        self.assertEqual(20, Base(20).id)

    def test_a5(self):
        b1 = Base()
        b2 = Base(20)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_a6(self):
        b = Base(20)
        b.id = 11
        self.assertEqual(11, b.id)

    def test_a7(self):
        with self.assertRaises(AttributeError):
            print(Base(20).__nb_instances)

    def test_a8(self):
        with self.assertRaises(TypeError):
            Base(0, 1)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_b1(self):
        r = Rectangle(5, 15, 3, 4, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_b2(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_b3(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_b4(self):
        s = Square(15, 1, 3, 6)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_b5(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_b6(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_b7(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_b8(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_b9(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_b10(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for from_json_string Base class method."""

    def test_c1(self):
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_c2(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_c3(self):
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_c4(self):
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_c5(self):
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_c6(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_c7(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_c8(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_c9(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_d1(self):
        r1 = Rectangle(4, 5, 1, 3, 8)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (8) 1/3 - 4/5", str(r1))

    def test_d2(self):
        r1 = Rectangle(4, 5, 1, 3, 8)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (8) 1/3 - 4/5", str(r2))

    def test_d3(self):
        r1 = Rectangle(4, 5, 1, 3, 8)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_d4(self):
        r1 = Rectangle(4, 5, 1, 3, 8)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_d5(self):
        s1 = Square(3, 2, 1, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (8) 2/1 - 3", str(s1))

    def test_d6(self):
        s1 = Square(3, 2, 1, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (8) 2/1 - 3", str(s2))

if __name__ == "__main__":
    unittest.main()
