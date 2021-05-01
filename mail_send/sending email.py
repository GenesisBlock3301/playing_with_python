import smtplib

sender = 'mdnuraminsifat@gmail.com'
receiver = 'nur15-1463@diu.edu.bd'

message = """Hello Sifat"""
try:
    smtpobj = smtplib.SMTP('localhost.com')  # my smtp server is localhost
    smtpobj.sendmail(sender, receiver, message)
    print("Successfully sent mail")
except smtplib.SMTPException:
    print('Error: unable to send mail')
