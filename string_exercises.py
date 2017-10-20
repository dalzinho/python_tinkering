# String exercises

fin = open('/home/john/Desktop/words.txt')
all_words = [word.rstrip() for word in fin]


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


def filter_words(function):
    words = [word for word in all_words if function(word)]

    # print words
    print "This is " + calculate_percentage(len(words), len(all_words)) + " of the total number of words."

filter_words(is_abecedarian)
filter_words(has_no_e)
filter_words(longer_than_20)