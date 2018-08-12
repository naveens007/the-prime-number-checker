#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
#  The Prime Number Checker (TPNC)
 
#  Encoding = UTF-8  Made for = /usr/bin/python3
#  Written by: Hemanya Sharma & Naveen Sharma
#
#   The Prime Number Checker (TPNC)
    Copyright (C) 2018  Hemanya Sharma & Naveen Sharma

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.


 
#  Please contribute to this by reporting bugs and making it better....
#  This code may have some MINOR BUGS....still very stable.
#  Does not print colored output in IDLE and may print GARBLED characters!
#  WARNING: Do not use as a module!

#  Code Version: 1.0.1 THETA Θ
#  Type "version" , "yelp" or "authors" for more info

#
#
#

"""



#__name__ = '__main__' <= Testing purposes only


import math # import math module

authors = "Hemanya Sharma & Naveen Sharma"
version = "1.0.1 THETA"
yelp = "The Prime Number Checker (TPNC) is a SUPER-EFFICIENT Prime-number finder that can find hundreds of numbers in a blink of an eye!"

minimum = 1
two = 2

class colors: # Gets a bit dark in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    NEG1 = '\033[3m'


# isPrime - Predicate function that tells whether the giver number is prime or not.
# It uses an efficient mechanism of log (N) where N is the number of digits in the input
def isPrime (num):
    
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
