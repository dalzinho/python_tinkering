class Odd_or_even:
      
    def __init__(self):
        self.number = input("Whit's yer number? ")
   
    def is_even(number):
        return number % 2 == 0

    def report(number):
        if is_even(number):
            print str(number) + " is even."
        else:
            print str(number) + " is odd."
