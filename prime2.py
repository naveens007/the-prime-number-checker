#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
#  The Prime Number Checker (TPNC)

#   Encoding = UTF-8  Made for = /usr/bin/python
#   Written by: Hemanya Sharma & Naveen Sharma
#
#   The Prime Number Checker (TPNC)
#   Copyright (C) 2018  Hemanya Sharma & Naveen Sharma

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

#   Please contribute to this by reporting bugs and making it better....
#   This code may have some MINOR BUGS....still very stable.
#   Does not print colored output in IDLE and may print GARBLED characters!

#   Code Version: 1.0.5 Py2 Stable
#   Type "version" , "yelp" or "authors" for more info

"""


import math # import math module

authors = "Hemanya Sharma & Naveen Sharma"
version = "1.0.5 Stable"
yelp = "The Prime Number Checker (TPNC) is a SUPER-EFFICIENT Prime-number finder. Please upgrade to python3!"

minimum = 1
two = 2

class colors: # You may need to change color settings in iPython
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'


# isPrime - Predicate function that tells whether the giver number is prime or not...
# It uses an efficient mechanism of log (N) where N is the number of digits in the input.

def isPrime (num):
   num = abs (num) # Get abs (absolute) value
   if (num <= minimum):
       print colors.GREEN + "The number" , num , "is neither a prime number nor a composite number." 
       print colors.ENDC
       return False # Return False if the number is not prime
   for i in range (two , two + int(math.log(num))):
       if (num % i) == 0:
           print colors.GREEN + "The number",num,"is not a prime number..."
           print "because",num,"divided by", i,"is" , num//i
           print colors.ENDC
           return False # Return False if the number is not prime
   print colors.GREEN + "The number",num,"is a prime number."
   print colors.ENDC
   return True # Return True if the number is prime


def mains ():
    try:
        num = int(raw_input('Enter an integer: '))
        isPrime (num)
        return "isPrime called!"
    except ValueError:
        print colors.RED + "Invalid input, Please enter a INTEGER only. QUITTING 😞"
        print colors.ENDC
        return "ERROR"



if (__name__ == '__main__'):
    mains ()


##########################
