import datetime

name = raw_input("What is your name? ")
age = input("How old are you?")
this_year = datetime.datetime.now().year
born_in = this_year - age

one_hundred_in = born_in + 100

def turns_100(one_hundred_in, name):
    print name + ", you will turn 100 in " + str(one_hundred_in) + "AD."

turns_100(one_hundred_in, name)
frequency = input("How many times should I tell you that? ")

i = 0
while i < frequency:
    turns_100(one_hundred_in, name)
    i += 1
