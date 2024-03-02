#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    counter = 10
    while counter > 0:
        print(counter)
        counter +-1
    print("Happy New Year!")


happy_new_year()
def square_integers(int_list):
    # code goes here!
    eturn [num**2 for num in int_list]

def fizzbuzz():
    # code goes here!
     if num % 3 == 0 and num % 5 ==0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)
