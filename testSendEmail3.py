import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server and login credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'edresearch.in@gmail.com'
smtp_password = 'yjnadnopluupwics'
smtp_sender = 'edresearch.in@gmail.com'

# Set up the email message
msg = MIMEMultipart()
msg['From'] = smtp_sender
msg['To'] = 'office@diracai.com'
msg['Subject'] = 'Test Email'
body = 'This is a test email.'
msg.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server and send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_sender, 'office@diracai.com', msg.as_string())
