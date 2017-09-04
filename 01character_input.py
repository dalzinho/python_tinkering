import datetime

name = raw_input("What is your name? ")
age = input("How old are you?")
this_year = datetime.datetime.now().year
born_in = this_year - age

one_hundred_in = born_in + 100

print "you will turn 100 in " + str(one_hundred_in) + "AD."
