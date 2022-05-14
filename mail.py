import os
import smtplib
import imghdr

from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['upsafe06@gmail.com', 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out who has been going into your place'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'upsafe06@gmail.com'

msg.set_content('Image attached')
# with open('ronaldo.jpg','rb')as f:
#     file_data = f.read()
#     file_type = imghdr.what(f.name)
#     file_name = f.name
# msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)#Here we will send the image of unauthorized person in place of this text
#Here is the written text #
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
         <h1 style="color:SlateGray;">Hey, An unauthorized person is detected on your place</h1> 
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
