file = 'File.xlsx'
username=''
password=''
send_from = ''
send_to = 'recipient1 , recipient2'
Cc = 'recipient'
msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = send_to
msg['Cc'] = Cc
msg['Date'] = formatdate(localtime = True)
msg['Subject'] = ''
server = smtplib.SMTP('smtp.gmail.com')
port = '587'
fp = open(file, 'rb')
part = MIMEBase('application','vnd.ms-excel')
part.set_payload(fp.read())
fp.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename='Name File Here')
msg.attach(part)
smtp = smtplib.SMTP('smtp.gmail.com')
smtp.ehlo()
smtp.starttls()
smtp.login(username,password)
smtp.sendmail(send_from, send_to.split(',') + msg['Cc'].split(','), msg.as_string())
smtp.quit()
