import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

while 1:
    provided_email = input('Please enter the emailadress i should slide for you...\n')
    position_ad = provided_email.find('@')
    sliced_part_1 = provided_email[0:position_ad]
    print('Part 1 is ' + sliced_part_1)
    sliced_part_2 = provided_email[position_ad+1:]
    print('Part 2 is ' + sliced_part_2)
    action = input('Now that i sliced it, should we send an email to the adress? Y/N')
    if action == "Y":
        print("Okay")
        mail_content = '''Hello,
        This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
        Thank You'''
        #The mail addresses and password
        sender_address = 'peterzwegertinthehood@gmail.com'
        sender_pass = 'thisiszwegert!'
        receiver_address = 'daniel.mayer22@gmail.com'
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    else:
        print("Then not")


