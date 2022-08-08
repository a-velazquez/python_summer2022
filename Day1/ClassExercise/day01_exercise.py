# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence


# Function
def fib_func(l):
    if len(l) == 1:
        l.append(sum(l))
    else:
        l.append(l[-1] + l[-2])
    if len(l) == 10:
        return l
    else:
        return fib_func(l)


# For loop
fib_seq = [1]
for i in range(1, 10):
    if len(fib_seq) == 1:
        fib_seq.append(sum(fib_seq))
    else:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])


"""return true if there is no e in 'word', else false"""


def has_no_e(word):
    bool_list = [letter != "e" for letter in word]
    return all(bool_list)


def has_no_e(word):
    if "e" not in word:
        return True
    else:
        return False


"""return true if there is e in 'word', else false"""


def has_e(word):
    bool_list = [letter == "e" for letter in word]
    return any(bool_list)


def has_e(word):
    if "e" in word:
        return True
    else:
        return False


"""return true if word1 contains only letters from word2, else false"""


def uses_only(word1, word2):
    return all([letter in word2 for letter in word1])


"""return true if word1 uses all the letters in word2, else false"""


def uses_all(word1, word2):
    return all([letter in word1 for letter in word2])


"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
dir([])


def is_abecedarian(word):
    return [letter for letter in word] == sorted([letter for letter in word])


def is_abecedarian(word):
    list1 = [letter for letter in word]
    list2 = [letter for letter in word]
    list2.sort()
    return list1 == list2
