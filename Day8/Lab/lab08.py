## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        remainder = x % y
        return gcd(y, remainder)


## Problem 2
## Write a function using recursion that returns prime numbers less than 121
## remember, primes are not the product of
## any two numbers except 1 and the number itself
## hint, "hardcode" 2
def find_primes(me=121, primes=[]):

    # print(me)
    # print(all([me % x for x in range(2,me)])!=0)

    if all([me % x for x in range(2, me)]) != 0:

        primes.append(me)

    new_me = me - 1

    # print(new_primes)
    # print(new_me)

    if new_me == 1:

        print(primes)
        return primes

    else:
        # new_primes = primes
        return find_primes(me=new_me, primes=primes)


## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html
