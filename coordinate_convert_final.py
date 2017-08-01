# File: coordinate_convert_final.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Chris Rodriguez (Fluigi Team)
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Blade Olson (bladeols@bu.edu)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/18/2017 - 7/22/2017 

# improved version of the Convert.py TECAN <-> ECHO
# coordinate conversion program 

# imports
import csv
import os
# for emailing the user any Tecan errors 
# import stmp
#import xlrd
#import xlrt

# make values global variables
global vals
global vals2

'''Formulas for conversion (collaboration with Chris):

TECAN -> ECHO

Conversion (map/reduce):
Map (tuple): {num:letter}
Reduce (coordiante tuple): (num,letter)

Conversion is in the form of type<tuple>

Formulas: 
f(T) = 8*(col-1) + conv[row]

ECHO -> TECAN 

f(E) = {row=conv[num%8], col=(num-1) // 8 + 1

Conversion(map/reduce):
Map (tuple): {letter:num}
Reduce (single integer): (num)
'''

# map/reduce of the TECAN to ECHO coordinate conversion
'''
def tecan_to_echo(tecNum):
	conv = {0:"H",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
	row = (tecNum-1)//8  + 1
	col = conv[tecNum % 8]
	return (col,row)
'''

# new approach (using 0 = A indexing)
def tecan_to_echo(tecNum):
        conv = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}
        # floating division (to get whole integer indices) 
        row = (int(tecNum) - 1) // 8 + 1
        col = (int(tecNum) - 1) % 8

        # must cast or get KeyError 
        s = str(conv[int(col)]) + str(row)
        return s 
        

# map/reduce of the ECHO to TECAN coordinate conversion
# example: ("A",1)
# new approach: take a string as input, get int as output (do not use tuple!) 
def echo_to_tecan(echoStr):
        row = echoStr[0]
        col = int(echoStr[1:])
        conv = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
        # want to get the string index instead
        # initialize a number num
        # 8*(col)-1
        tecNum = 8*(col-1)2 + conv[row]
        return tecNum

vals = [tecan_to_echo(x) for x in range(1,97)]
vals2 = [echo_to_tecan(x) for x in vals]

# debug statements 
# print([x for x in range(1,97)])
# print(vals)
# print(vals2)

def main():

        # read the JoVE article (similar to the previous approach)
        print("Converting the coordinates from TECAN robot: ")
        # give the user the choice to convert
        print("Which way do you want to convert?")
        selection = input("Please select either 1 or 2:" )
        # user chooses the way to convert
        if selection == '1':
        # list comprehension: [tecan_to_echo(x) for x in range(1,97)]
           print("ECHO coordinates: \n")
           print(vals)
        elif selection == '2':
        # list comprehension: [echo_to_tecan(x,y) for x,y in vals]
           print("TECAN coordinates: \n")
           print(vals2)
        else:
           print("Unrecognizable command!")
           
main()
