# File: tecan_converter2.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Blad Olson (bladeols@bu.edu) (Programming / graduate supervisor for Densmore lab / Aquarium Developer)
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/17/2017 - 8/11/2017 

# This program converts TECAN to ECHO via middleware function tecan_to_echo(), and then
# if the TECAN script has errors, the program sends emails of warning / error 

import os 
import sys
import csv
import re 

# This program is a simulation of a TECAN robot using TECAN instructions, and
# through a middleware class coordinate_convert_final.py, will give out the instructions
# of the simulation in ECHO format, which can then be used
# as a source text file for Excel CSV format

# map/reduce of TECAN to ECHO
def tecan_to_echo(tecNum):
    conv = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H"}

    # if tecan number is not an integer 
    try:
        int(tecNum)
    except ValueError:
        return -1

    # if the tecan number index is greater than 96, less than 1 
    if int(tecNum) > 96 or int(tecNum) < 1:
        return -1
    
    row = (int(tecNum) - 1) // 8 + 1 
    col = (int(tecNum)-1) % 8

    s = str(conv[int(col)]) + str(row)
    return s 

def main():

    filename = sys.argv[1]
    outfile = sys.argv[2]
    
    fp2 = open(outfile,"w")
    wra = csv.writer(fp2)
    
    body_msg = []
    warning_msg = []
    title = []

    print("Starting the TECAN conversion: ")
    
    title.append("source plate")
    title.append("source well")
    title.append("destination plate name")
    title.append("destination well")
    title.append("Transfer Volume")
    wra.writerow(title)
    
    # read the full version of JoVE
    try:
        fp = open(filename)
    except IOError:
        print('%s does not exist!' % filename)
    else:
        
        for line in fp:
            string = []
            
            if line[0] == 'R':
                continue

            if line[0] == 'A':
                lst = line.split(';')
                source_plate = lst[1]
                
                if source_plate != 'Reservoir':

                    if source_plate == "":
                        body_msg.append("Source Plate Error: %s \n" % line)
                        print(body_msg)
                        fp.next()
                        fp.next()
                        continue
    
                    source_well = tecan_to_echo(lst[4])

                    if source_well == -1:
                        body_msg.append("Source Well Error: %s \n" % line)
                        fp.next()
                        fp.next()
                        continue

                    # get destination well, plate
                    line = fp.next()
                    lst = line.split(';')
                    dest_plate = lst[1]

                    if dest_plate == "":
                        body_msg.append("Destination Plate Error: %s \n" % line)
                        fp.next()
                        continue

                    dest_well = tecan_to_echo(lst[4])

                    if dest_well == -1:
                        body_msg.append("Destination Well Error: %s \n" % line)
                        fp.next()
                        continue

                    vol = lst[-1]
                    
                    try:
                        float(vol)
                    except ValueError:
                        body_msg.append("Volume Type Error: %s \n" % line)
                        fp.next()
                        continue

                    if float(vol) < 0.0:
                        body_msg.append("Volume Value Error: %s \n" % line)
                        fp.next()
                        continue

                    # skip the wash command 
                    fp.next()

                    string.append(source_plate)
                    string.append(source_well)
                    string.append(dest_plate)
                    string.append(dest_well)
                    string.append("100")

                    # write out csv file
                    wra.writerow(string)
                    
                else:
                    # reservior step
                    # regex to get out only the integer values of reservoir command
                    
                    trough = re.findall("Trough \d+",lst[3])

                    # the trough does not have enough liquid left 
                    if len(trough) == 0:
                        warning_msg.append("Lack of Reservoir Liquid Warning: %s \n" % line)
                        fp.next()
                        fp.next()
                        continue

                    # the trough has invalid liquid value 
                    elif int(trough[0][7:]) == 0:
                        warning_msg.append("Invalid Reservoir Volume Liquid Warning: %s \n" % line)
                        fp.next()
                        fp.next()
                        continue

                    fp.next()
                    fp.next()

    fp2.close()
    fp.close()

    # send user email attributes
    # user email, subject (error and warning) 
    to_user = 'jasonlu968@gmail.com'
    err_subject = "TECAN Conversion Error"
    warn_subject = "TECAN Conversion Warning"

    # error message sent 
    error_cmd = "echo \"" + "".join(body_msg) + "\" | mailx -s \" " + err_subject + "\" " + to_user + ""
    if len(body_msg) != 0:
        os.system(error_cmd)

    # warning message sent 
    warn_cmd = "echo \"" + "".join(warning_msg) + "\" | mailx -s \" " + warn_subject + "\" " + to_user + ""
    if len(warning_msg) != 0:
        os.system(warn_cmd)
    
    print("TECAN conversion is completed.")
              
main()




