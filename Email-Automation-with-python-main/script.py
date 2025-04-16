# import the required libraries
# from cgi import test
import pandas as pd
from email import message
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# your email details

SERVER = 'smtp.gmail.com'  # your smtp server
PORT  = 587    # your port number
FROM  =  'imkartikey.ydvv@gmail.com'    # your from email id
PASS  = 'qlhlblckbpxxkdph' # your email id password

# Authentication part
server = smtplib.SMTP(SERVER,PORT)

server.set_debuglevel(1) # set 1 to help in debugging
server.ehlo()
server.starttls() # start TLS connection which is secure connection

server.login(FROM,PASS)


  
# reading the spreadsheet
email_list = pd.read_excel(r'C:\Users\Kartikey Yadav\Downloads\Email-Automation-with-python-main\Email-Automation-with-python-main\data.xlsx')


print('Getting the names and the emails................')
# getting the names and the emails
names = email_list['Full name']
emails = email_list['Email Address']
print(emails)

# email composing
print('Composing Email................')
# creating a message body
msg = MIMEMultipart()

msg['Subject'] = 'Testing purpose'
msg['From'] = FROM

print('email body settings...............')

# iterate through the records
for i in range(len(emails)):
  
    # for every record get the name and the email addresses
    name = names[i]
    email = emails[i]
  
    # the message to be emailed
    message = 'Greetings,  \n \nI am kartikey this is testing for my code.\n \nsorry for inconvinience \n\nRegards'
    msg.attach(MIMEText(message, 'plain'))

    # sending the email
    server.sendmail(FROM, [email], msg.as_string())

print('Email Sent .....') 

# close the smtp server
server.close()


