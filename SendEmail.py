import smtplib
import os
import mimetypes

import mimetypes
# Issue 1 found: https://stackoverflow.com/questions/33313858/importerror-no-module-named-email-mime-email-is-not-a-package
#solved issue 1
# email sending tutorial: https://stackoverflow.com/questions/23171140/how-do-i-send-an-email-with-a-csv-attachment-using-python
from email.message import EmailMessage
#EmailMessage class is used to structure email message

#https://www.programiz.com/python-programming/args-and-kwargs
'''
class EmailMessage(MIMEPart):

    def set_content(self, *args, **kw):
        super().set_content(*args, **kw)
    
'''
#
message= EmailMessage()
message['Subject'] = 'Weekly Food Request'
message['From'] = "abu.musa.rabiul@gmail.com"
message['To'] = "silentrobi840@gmail.com"
message.set_content("+++++ Weekly food request report +++++")
#To add html content
"""
three quote in the argument defines that text is multilines
"""
message.add_alternative("""
<!DOCTYPE html>
<body>
<h1> This is html email</h1>
</body>
</html>
""", subtype='html')

# with doesn't create scope
with open('1.csv', 'rb') as f:
    file_data = f.read()
    kind = mimetypes.guess_type(f.name)
    if kind is None:
        print('Cannot guess file type!')
    else:

        type= kind[0]
        extension = mimetypes.guess_extension(type)
    print(type)
    print(extension)
    file_name= f.name
    print(file_name)
message.add_attachment(file_data, maintype='application',subtype= 'octet-stream', filename=file_name)

print('a')



# The 'with' statement clarifies code that
# previously would use try...finally blocks to ensure that clean-up code is executed.

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:  # setting up source mail server
    # ++++++++with block start +++++++++
    # initial set up connection
    smtp.ehlo()  # identifies the mail server we are using
    smtp.starttls()  # To encrypt the connection
    smtp.ehlo()  # To re-identfy as encrypted connection

    # Note: To  use SSL instead of TSL use following convenstion
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # ............

    smtp.login("abu.musa.rabiul@gmail.com", "Acifl1234")  # !need to imporve: passaword shouldn't be visible

    '''
    subject = 'Test message'
    body = "Is the message reachable?"
    message = f'Subject: {subject}\n\n{body}'  # note can use normal string
    '''
    print("hi")
    #smtp.sendmail("abu.musa.rabiul@gmail,com", "silentrobi840@gmail.com", message) #explictily methon sender and receiver
    smtp.send_message(message)



    # Testing emails are actually sent
    # python3 -m smtpd -c DebuggingServer -n localhost:<port>

