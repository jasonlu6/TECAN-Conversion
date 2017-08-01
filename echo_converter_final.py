# File: echo_converter.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/17/2017 - 8/11/2017 

'''Extension: Using system argv parsing to read direct CSV files (no required hard code input)'''

'''Extension 2 (7/27/2017): Re-arrange the parameters of the file so that the file could be properly
read in the conversion from ECHO to TECAN'''

# This program will take the input of a CSV / ECHO file (with five main
# parameters of command, source well, destination well, plate name, and transfer
# volume) and translate the data into English pseudocode for TECAN conversion

# conversion directly to TECAN is more difficult since the TECAN aspirate,
# dispense, and wash parameters have significantly more parameters
# than the ECHO counterparts

import csv
import sys
import os

def echo_to_tecan(echoStr):
        row = echoStr[0]
        # col = int(echoStr[1:])
        conv = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
        # want to get the string index instead
        # initialize a number num
        # 8*(col)-1
        try:
            s = conv[row]
        except KeyError:
            return -1
        
        try:
            col = int(echoStr[1:])
        except ValueError:
            return -1
    
        tecNum = 8*(col-1) + conv[row]
        
        if tecNum > 96 or tecNum < 1:
            return -1
        else:
            return tecNum

# main function to test it out
# for simplicity, only conversion.csv will be parsed
# if no CSV file available, then the commands will be put in manually
def main():

    print("Starting the ECHO conversion: ")

    # parsing command
    filename = sys.argv[1]
    outfile = sys.argv[2]

    fp2 = open(outfile,'w')
    body_msg = []
    
    try:
        csvfile = open(filename)
    except IOError:
        print('%s does not exist!' % filename)
    else:
        # reader object to parse the file
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        # for loop to process the parsed lines
        next(csvreader)
        
        for row in csvreader:
            
            data = "".join(row)
            val = data.split(',')

            # throw transfer volume error
            try:
                int(val[4])
            except ValueError:
                body_msg.append("Liquid Detection Error: %s \n" % data)
                continue
        
            if int(val[4]) <= 0 or int(val[4]) > 100:
                body_msg.append("Liquid Detection Error: %s \n" % data)
                continue
                
            # define the source plate and (converted) source well number 
            source_plate = val[0]
            source_well = echo_to_tecan(val[1])
            
            if source_well == -1:
                body_msg.append("Source Well Error: %s \n" % data)
                continue
                
            dest_plate = val[2]
            dest_well = echo_to_tecan(val[3])

            if dest_well == -1:
                body_msg.append("Destination Well Error: %s \n" % data)
                continue

            string = "A;" + source_plate + ";;" + "96 Well Microplate;" + str(source_well) + ";;" + "2.0\n"
            
            fp2.write(string)

            string = "D;" + dest_plate + ";;" + "96 Well Microplate;" + str(dest_well) + ";;" + "2.0\n"
            
            fp2.write(string)

            fp2.write("W;\n")

    fp2.close()

    to_user = 'jasonlu968@gmail.com'
    subject = "ECHO Conversion Error"

    # send error email
    
    cmd = "echo \"" + "".join(body_msg) + "\" | mailx -s \" " + subject + "\" " + to_user + ""
    if len(body_msg) != 0:
        os.system(cmd)

    print("ECHO conversion is completed.")
                
main()






