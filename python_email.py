# File: python_email.py
# Author: Jason Lu (jasonlu6@bu.edu)
# Collaborations:
# Rohin Banerji (rohinb96@bu.edu) (Class of 2019 Fellow Undergraduate CE student)
# Professor Douglas Densmore (dougd@bu.edu)
# Marliene Pavan (mapavan@bu.edu) (Supervisor / Senior Researcher at BU)
# Luis Ortiz (lortiz15@bu.edu) (Graduate supervisor of TECAN / ECHO conversion)
# Christopher Rodriguez (chrizrodz@gmail.com) (Fluigi / Programmer in CIDAR) 
# Densmore CIDARLAB UROP Project #4 (WETLAB division)
# Date: 7/13/2017 - 8/11/2017 

# Description: third of the "error-checking" deliverables, which now includes
# a subject header title (default is 'TEST'), and a list for the user
# (TECAN Robot server) to put the desired Gmail account urls (with the
# other person(s)' permission) as potential sender requests.

# simplified version (only send a message from TECAN robot, no subject specified) 

# TECAN Robot ficticious gmail address:
# tecanserver@gmail.com

# source:
# http://stackabuse.com/how-to-send-emails-with-gmail-using-python/

'''Manual Freedom EVOware 2.3 Research Use Only copy.pdf (Ch 18.1)'''

''' 7/13/2017: make sure that the TECAN robot simulator can catch
the exceptions in a regular manner (purposely try some error-raising commands
in the aspirate and dispense commands)'''

''' 7/25/2017: connect to the email.py and tecanconnect.py (or another programming language form)
in order to allow the TECAN robot to directly show / email to the user(s) via a text message / email
exactly to the user(s) what is the error, and how to diagnose it, and potential solutions'''

'''7/25/2017: make a "fake" / doppelganger TECAN robot account
to send error messages to the user(s) '''

import smtplib

gmail_user = 'tecanserver@gmail.com'
# abstract away its password 
gmail_password = 'mybro543212345'

sent_from = gmail_user
to = ['jasonlu968@gmail.com']

#['chrizrodz@gmail.com']
# emails for the rest of people in lab
# mapavan@bu.edu, lortiz15@bu.edu, jasonlu968@gmail.com, dougd@bu.edu 
subject = 'TECAN Error: liquid handling'
body = 'TECAN robot reservior has run out! Please refill.'

# make additional subject and error messages
subject2 = 'TECAN Error: source well'
body2 = 'TECAN robot source well not defined.'

subject3 = 'TECAN Error: destination well'
body3 = 'TECAN robot destination well not defined.'

subject4 = 'TECAN Error: liquid detection'
body4 = '''TECAN DiTi Script Sample as no liquid or not enough
liquid in the reservior'''

subject5 = 'TECAN Error: clot'
body5 = ''' '''

message = 'Subject: {}\n\n{}'.format(subject,body)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.sendmail(sent_from, to, message)
server.close()
print('Email sent!')
