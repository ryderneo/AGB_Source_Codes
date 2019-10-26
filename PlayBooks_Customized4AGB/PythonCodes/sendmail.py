import smtplib
import time
import getpass
port = 587
server = 'smtp.ipage.com'
recipients = ['sutram@agbcommunication.com']
sender = 'ayenyeinaung@agbcommunication.com'
message = 'From: ayenyeinaung@agbcommunication.com\nSubject: [PGS]: Results\n\nBlaBlaBla'
session = smtplib.SMTP('smtp.ipage.com', 587)
session.starttls()
password = getpass.getpass()
session.login(sender,password)
session.sendmail(sender,recipients,message);
session.quit()
