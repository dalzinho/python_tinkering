'''
Write a program that reads a file, breaks each line into words, strips 
whitespace and punctuation from the words, and converts them to lowercase.
'''

import string
import cProfile

def get_path(filename):
    return '/home/john/python/data_structures/' + filename 

def read_file(path):
    return open(path)

def count_words(file):
    
    words = []

    for line in file:
        words += [word.strip(string.punctuation) for word in line.split()]

    return len(words)
    

path = get_path('example.txt')
path = get_path('vojna_i_mir.txt')
cProfile.run('count_words(read_file(path))')