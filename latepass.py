import sys
import os
from tkinter import *
import csv
import smtplib, ssl
import time

def run():
   
    name = " "
    port = 587  
    smtp_server = "smtp.gmail.com"
    sender_email = "passbot@student.kis.or.kr"
    receiver_email = " "
    password = "YoureLate2019!"
   

    context = ssl.create_default_context()
    barcode = input()
   
    if(str(barcode)[0] == '0'):
        barcode = int(str(barcode[1:7]))
        receiver_email = " "
    with open('Secondary_Info_For_PassBot.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif row[0] == barcode:
                name = row[1] + " " + row[2]
                print(name)
                receiver_email = row[4]
            else:
                line_count += 1


    message = """\
    Latepass for """ + name + """

    The pass serves as notice that """ + name + """" has arrived to class"""

    #email code
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        server.sendmail(sender_email, "aimmie.kellar@kis.or.kr", message) 
       
       
   
    timenow = time.asctime(time.localtime(time.time()))
   
    #print code here
    os.system("echo 'Student name: " + name + "\n Arrival time " + timenow + "\n\nThis is a late pass to class. This pass was also sent to your parent and school administrator.' | lp")
       
while True:
    run()
