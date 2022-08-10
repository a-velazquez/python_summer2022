## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test in your script and see your results.
def count_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    if type(word) == int:
        raise TypeError(f"{word} is of type integer, please pass a string.")
    else:
        count = len([letter for letter in word if letter in vowels])
        return count


count_vowels("computer")
count_vowels(10)


import unittest


class TestCountVowels(unittest.TestCase):
    def test_int_recognition(self):
        self.assertTrue(type(10) == int)

    def test_str_recognition(self):
        self.assertTrue(type("foo" == str))

    def test_count_vowels(self):
        w = 5
        with self.assertRaises(TypeError):
            count_vowels(w)


if __name__ == "__main__":
    unittest.main()
