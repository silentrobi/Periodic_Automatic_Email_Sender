import smtplib
#EmailMessage class is used to structure email message
from email.message import EmailMessage
import mimetypes
from datetime import datetime

class EmailActivity:
    def __init__(self):
        self.__message= EmailMessage()



    #Add attachment(Ex: pdf, image, csv ...) to the email
    def addAttachment(self, fileName):
        with open(fileName, 'rb') as f:
            file_data = f.read()
            ctype, encoding = mimetypes.guess_type(f.name)
            if ctype is None or encoding is not None:
                ctype = "application/octet-stream"
            maintype, subtype = ctype.split("/", 1)
            print(maintype)
            print(subtype)
        self.__message.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=fileName)

    #Set up email server and secure connection
    def setUpSenderCredential(self, userEmail, password, mailServer, port):
        with smtplib.SMTP(mailServer, port) as smtp:  # setting up source mail server
            # initial set up connection
            print(mailServer)
            smtp.ehlo()  # identifies the mail server we are using
            smtp.starttls()  # To encrypt the connection
            smtp.ehlo()  # To re-identify as encrypted connection
            smtp.login(userEmail, password)
            print("connection set up successful")
            print(smtp == None)
            smtp.send_message(self.__message)
            print("Message Sent Successfully!")
            print("LOG: Message sent on " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            # log message send time
            # < !Need to implement: save send log information to database>

        # To add html content
    def addHtmlToMessage(self,html):
            self.__message.add_alternative(html, subtype='html')

    def message(self,From, To ,Subject=None,textContent=None ): # To, From take string
            self.__message['Subject']= Subject
            self.__message['From']= From
            self.__message['To']= To
            self.__message.set_content(textContent)

    def appendTextContext(self):
            """appaned textContext"""
    def getMessageObject(self):
            return self.__message



