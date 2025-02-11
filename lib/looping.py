#!/usr/bin/env python3

def happy_new_year():
   for i in range(10, -1, -1):
       if i >= 0:
           print(i)

   print("Happy New Year!")
    

happy_new_year()
       

def square_integers(int_list):
    return [i * i for i in int_list]
       
   

def fizzbuzz():
    for i in range(1, 101):  # Loop from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Run the function
fizzbuzz()

