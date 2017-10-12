from email.mime.text import MIMEText

msg = MIMEText('hello, send by Python', 'plain', 'utf-8')

from_addr = 'hello@gmail.com'
password = input('Password:')

to_addr = 'hello2@gmail.com'

import smtplib

server = smtplib.SMTP('smtp.gmail.com', 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()