import unittest
<<<<<<< HEAD
import os

os.chdir("./Documents/GitHub/python_summer2022/Day3/Lab")

from lab03 import *
=======
from lab03 import * # needs to be same wd as lab03.py
>>>>>>> f530330142add644bce33598475f97ce2fe1dd05


class labTests(unittest.TestCase):

    ## fill in a few tests for each
    ## make sure to account for correct and incorrect input

    def test_shout(self):
        self.assertEqual(shout("foo"), "FOO")
        w = 5
        with self.assertRaises(TypeError):
            shout(w)

    def test_reverse(self):
        self.assertEqual(reverse("foo"), "oof")
        self.assertEqual(reverse("here it is"), "si ti ereh")
        w = 5
        with self.assertRaises(TypeError):
            reverse(w)

    def test_reversewords(self):
        self.assertEqual(reversewords("here it is"), "is it here")
        self.assertEqual(reversewords("foo"), "foo")
        w = 5
        with self.assertRaises(TypeError):
            reversewords(w)

    def test_reversewordletters(self):
        self.assertEqual(reversewordletters("here it is"), "ereh ti si")
        self.assertEqual(reversewordletters("foo"), "oof")
        w = 5
        with self.assertRaises(TypeError):
            reversewordletters(w)

    def test_piglatin(self):
        self.assertEqual(piglatin("foo"), "oo-fay")
        self.assertEqual(piglatin("foo bar"), "oo-fay ar-bay")
        w = 5
        with self.assertRaises(TypeError):
            piglatin(w)


if __name__ == "__main__":
    unittest.main()
