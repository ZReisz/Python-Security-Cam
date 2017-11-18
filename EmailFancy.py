import smtplib
import time
from time import sleep
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 

#This code emails photos
fromaddr = "zackreisz02@gmail.com" #Change from email
toaddr = "reisz@student.uiwtx.edu" #Change to email

msg = MIMEMultipart()

msg['From'] = fromaddr #DO NOT CHANGE
msg['To'] = toaddr #DO NOT CHANGE
msg['Subject'] = "ALERT! Activity Detected by Camera 1"  #Change subject text here

body = "Detection Date: " +  time.strftime('%A | %d-%B-%Y | %H:%M:%S') #Change body text here

msg.attach(MIMEText(body, 'plain'))

filename = (r'''C:\Users\user\Pictures\FOB.jpg''') #Change file path here
attachment = open(filename, "rb") 
                  
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Contect-Disposition', "attachment; filename " + filename)

msg.attach(part) 

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Re!962328")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print("Email Sent.")
