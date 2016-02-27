import smtplib

fromname = 'LILBTHEBASEDGOD'
fromaddr = 'david.g.colley123@gmail.com'
toname = 'IDK'
toaddr = 'david.colley@particularpresence.com'
subject = 'For the troll...'
msg = 'hi'
message = message = """From: {} <{}>
To: {} <{}>
Subject: {}

{}
"""

messagetosend = message.format(fromname,fromaddr,toname,toaddr,subject,msg)

# Credentials (if needed)

username = 'david.g.colley123@gmail.com'

password = #app password was ere

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()

