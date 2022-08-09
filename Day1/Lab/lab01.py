# You can find information on how to convert numbers to a different base here:
# https://www.tutorialspoint.com/computer_logical_organization/number_system_conversion.htm

# You can find information on how to convert numbers to roman numerals here:
# https://www.romannumerals.org/converter


def binarify(num):
    """convert positive integer to base 2"""
    digits = []
    if num <= 0:
        return "0"

    while num > 0:
        digits.append(str(num % 2))
        num = num // 2
    return "".join(digits[::-1])


def int_to_base(num, base):
    """convert positive integer to a string in any base"""
    if num <= 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num = num // base
    return "".join(digits[::-1])


def base_to_int(string, base):
    """take a string-formatted number and its base and return the base-10 integer"""
    if string == "0" or base <= 0:
        return 0
    result = sum(
        [int(d) * (base ** i) for i, d in zip(reversed(range(0, len(string))), string)]
    )
    return result


def base_to_int(string, base):
    """take a string-formatted number and its base and return the base-10 integer"""
    if string == "0" or base <= 0:
        return 0
    result = []
    for i, d in zip(reversed(range(0, len(string))), string):
        result.append(int(d) * (base ** i))
    return sum(result)


def flexibase_add(str1, str2, base1, base2):
    """add two numbers of different bases and return the sum"""
    num1 = base_to_int(str1, base1)
    num2 = base_to_int(str2, base2)

    result = num1 + num2

    return result


def flexibase_multiply(str1, str2, base1, base2):
    """multiply two numbers of different bases and return the product"""
    num1 = base_to_int(str1, base1)
    num2 = base_to_int(str2, base2)

    result = num1 * num2

    return result


def romanify(num):
    """given an integer, return the Roman numeral version"""
    rom = {"m": 1000, "d": 500, "c": 100, "l": 50, "x": 10, "v": 5, "i": 1}

    numerals = {}
    for k, v in rom.items():
        numerals[k] = num // v
    # find min, non-zero key
    nonzero = dict(filter(lambda elem: elem[1] != 0, numerals.items()))
    if all([v == 0 for v in numerals.values()]):
        min_key = "i"
    else:
        min_key = min(nonzero, key=nonzero.get)

    result = []
    # check if i,x,c greater than 3
    if min_key == "i" and nonzero[min_key] > 3:
        result.append("i" * (5 - numerals["i"]) + "v")
    elif min_key == "x" and nonzero[min_key] > 3:
        result.append("x" * (5 - numerals["x"]) + "l")
    elif min_key == "c" and nonzero[min_key] > 3:
        result.append("c" * (5 - numerals["c"]) + "d")
    else:
        result.append(min_key * nonzero[min_key])
    if num - (nonzero[min_key] * rom[min_key]) != 0:
        result.append(romanify(num - (nonzero[min_key] * rom[min_key])))

    return "".join(result)


# Copyright (c) 2014 Matt Dickenson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
