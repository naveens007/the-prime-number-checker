#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
#  The Prime Number Checker (TPNC)
 
#  Encoding = UTF-8  Made for = /usr/bin/python3
#  Written by: Hemanya Sharma & Naveen Sharma
#  This code is completely FREE and OPEN-SOURCE but comes WITHOUT ANY WARRANTY!
#  Do whatever you want to do with this code...and all that GPL stuff...
#  This Code comes under the licence: GNU GPL Version 3+
#  FREE means free as in freedom...not free as in beer!
 
#  Please contribute to this by reporting bugs and making it better....
#  This code may have some MINOR BUGS....still very stable.
#  Does not print colored output in IDLE and may print GARBLED characters!
#  WARNING: Do not use as a module!

#  Code Version: 2.8.4 THETA Θ
#  Type "version" , "yelp" or "authors" for more info

#  Thanks to the Anaconda team, Python.org & iPython for making this program come true
#  & making programming assessible to everyone. :-)
#  Without them this program would not have come true.

"""



#__name__ = '__main__'
# uncomment to always ensure __name__ = '__main__' and avoid errors


import math # import math module

authors = "Hemanya Sharma & Naveen Sharma"
version = "2.8.4"
yelp = "The Prime Number Checker (TPNC) is a SUPER-EFFICIENT Prime-number finder that can find hundreds of numbers in a blink of an eye!"


minimum = 1
two = 2


class colors: # Gets a bit dark in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    NEG1 = '\033[3m'


# isPrime - Predicate function that tells whether the giver number is prime or not.
# It uses an efficient mechamism of log (N) where N is the number of digits in the input
def isPrime (num): # make a function called isPrime
    
   num = abs (num) # Get abs (absolute) value

   if (num <= minimum):
       print (colors.GREEN + "The number" , num , "is neither a prime number nor a composite number.\n" , colors.ENDC)
       return False # Return False if the number is not prime

   for i in range (two , two + int(math.log(num))):
       if (num % i) == 0:
           print ( colors.GREEN + "The number",num,"is not a prime number...")
           print ("because",num,"divided by", i,"is" , num//i , "\n" , colors.ENDC)
           return False # Return False if the number is not prime

   print (colors.GREEN + "The number",num,"is a prime number.\n" , colors.ENDC)
   return True # Return Talse if the number is prime




def mains ():
    try:
        num = int(input('Enter an integer: '))

    except ValueError:
        print (colors.RED + "Invalid input, Please enter a INTEGER only. QUITTING -_- \n" , colors.ENDC)
        return "ERROR"

    isPrime (num)
    return




if (__name__ == '__main__'):
    mains ()

else:
    if (__name__ != '__main__'):

        print ("An error occured: __name__ of" , type(__name__) , "equals" , colors.NEG1 + __name__ , colors.ENDC)
        __name__ = '__main__'
        print ("Fixed the problem...",colors.GREEN + "OK\n" , colors.ENDC)
    else:
        print ("An unknown error occured: Unknown! *_*\n")



##########################