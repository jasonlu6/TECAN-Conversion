# File: Convert2_testing.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Chris Rodriguez (Fluigi Team)
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Blade Olson (bladeols@bu.edu)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/18/2017

# improved version of the Convert.py TECAN <-> ECHO
# coordinate conversion program 

# imports
import csv
import os
#import xlrd
#import xlrt

'''Formulas for conversion (collaboration with Chris):

ECHO -> TECAN 

Conversion (map/reduce):
Map (tuple): {num:letter}
Reduce (coordiante tuple): (num,letter)

Conversion is in the form of type<tuple>

Formulas: 
f(T) = 8*(col-1) + conv[row]

TECAN -> ECHO

f(E) = {row=conv[num%8], col=(num-1) // 8 + 1

Conversion(map/reduce):
Map (tuple): {letter:num}
Reduce (single integer) (num)
'''

def tecan_to_echo(tecNum):
	conv = {0:"H",1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G"}
	row = (tecNum-1)//8  + 1
	col = conv[tecNum%8]
	return (col,row)

def echo_to_tecan(col,row):
	conv = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
	tecNum = (row-1) * 8 + conv[col]
	return tecNum

vals = [tecan_to_echo(x) for x in range(1,97)]
vals2 = [echo_to_tecan(x,y) for x,y in vals]
print([x for x in range(1,97)])
print("ECHO coordinates: \n")
print(vals)
print("TECAN coordiantes: \n")
print(vals2)

def main():
        # TO DO:
        # 1) Read the JoVE article CSV input from ECHO (including the source well and
        # destination well coordinates)
        # 2) Write the converted output to jove_output_final.csv (new CSV file)
        # 3) Read the JoVE article TECAN GWL / Word / txt (Plain Text) input
        # 4) Write the converted output to jove_output_final.gwl or jove_output_final.txt
        # 5) Give the user any errors (via the smtp object in Python)

        
main()
