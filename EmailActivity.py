import smtplib
#EmailMessage class is used to structure email message
from email.message import EmailMessage
import mimetypes
from datetime import datetime
'''
EmailActivity class does email sending operations, 
which includes Setting up mail server, add attachment, add html, add sender and recipient 
'''
class EmailActivity:
    def __init__(self):
        self.__message= EmailMessage()



    #To Add attachment(Ex: pdf, image, csv ...) to the email
    def addAttachment(self, filePath, fileName):
        with open(filePath, 'rb') as f:
            try:
                file_data = f.read()
                ctype, encoding = mimetypes.guess_type(f.name)
                if ctype is None or encoding is not None:
                    ctype = "application/octet-stream"
                maintype, subtype = ctype.split("/", 1)
                print(maintype)
                print(subtype)
            except Exception as e:
                print(e)
        self.__message.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=fileName)

    #Set up email server and secure connection
    def sendMail(self, userEmail, password, mailServer, port):
        with smtplib.SMTP(mailServer, port) as smtp:  # setting up source mail server
            try:
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
            except Exception as e:
                print(e)

        # To add html content
    def addHtmlToMessage(self,html):
        try:
            self.__message.add_alternative(html, subtype='html')
        except Exception as e:
            print(e)

    def message(self,From, To ,Subject=None,textContent=None ): # To, From take string
            self.__message['Subject']= str(Subject)
            self.__message['From']= str(From)
            self.__message['To']= str(To)
            self.__message.set_content(textContent)

    def setContext(self,textContent):
        self.__message.set_content(textContent)

    def appendTextContext(self):
            """appaned textContext"""
    def getMessageObject(self):
            return self.__message



