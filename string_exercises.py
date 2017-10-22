# String exercises

fin = open('/home/john/Desktop/words.txt')
all_words = [word.rstrip() for word in fin]
avoid_letters = "abc"
uses_only_letters = "acefhlo"
uses_all_letters = "aeiouy"


def has_no_e(hase):
    return 'e' not in hase


def calculate_percentage(numerator, denominator):
    return '{:.5%}'.format(numerator / float(denominator))


def is_abecedarian(word):
    word = word.lower()
    initial = ord(word[0])

    for letter in word:
        if ord(letter) >= initial:
            initial = ord(letter)
        else:
            return False

    return True

def longer_than_20(word):
    return len(word) > 20

def avoids(word):
    for letter in avoid_letters:
        for char in word:
            if char == letter:
                return False

    return True


def uses_only(word):
    response = True

    for char in word:
        if char not in uses_only_letters:
            response = False

    return response


def uses_all(word):
    response = True

    for letter in uses_all_letters:
        if letter not in word:
            response = False

    return response



def filter_words(function):
    words = [word for word in all_words if function(word)]

    print words
    print "This is " + calculate_percentage(len(words), len(all_words)) + " of the total number of words."

filter_words(uses_all)