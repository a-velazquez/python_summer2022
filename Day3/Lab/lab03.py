## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    if type(txt) != str:
        raise TypeError(f"{txt} is not a string.")
    else:
        return txt.upper()


## reverse all characters in string
def reverse(txt):
    if type(txt) != str:
        raise TypeError(f"{txt} is not a string.")
    else:
        return txt[::-1]


## reverse word order in string
def reversewords(txt):
    if type(txt) != str:
        raise TypeError(f"{txt} is not a string.")
    else:
        word_list = txt.split()
        return " ".join(word_list[::-1])


## reverses letters in each word
def reversewordletters(txt):
    if type(txt) != str:
        raise TypeError(f"{txt} is not a string.")
    else:
        rev_words = []
        for word in txt.split():
            rev_words.append(word[::-1])
        return " ".join(rev_words)


## optional -- change text to piglatin.. google it!
def piglatin(txt):
    if type(txt) != str:
        raise TypeError(f"{txt} is not a string.")
    else:
        letters = ["{:c}".format(i) for i in range(97, 123)]
        vowels = ["a", "e", "i", "o", "u"]
        consonants = [l for l in letters if l not in vowels]

        word_list = txt.split()
        pl = []
        for word in word_list:
            if word[0] in consonants:
                if word[1] in consonants:
                    pl_word = word[2:] + "-" + word[0:2] + "ay"
                else:
                    pl_word = word[1:] + "-" + word[0] + "ay"
            else:
                pl_word = word + "-yay"
            pl.append(pl_word)

        return " ".join(pl)


## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.

string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

for item in string_list:
    try:
        print(reverse(item))
    except TypeError:
        print("A string was not passed")
        pass
