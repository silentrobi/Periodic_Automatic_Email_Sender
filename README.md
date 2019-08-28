# Periodic automatic weekly email nofication sender microservice

# Project documantation
The project has following classes and script files.

# EmailActivity -- *class*

EmailActivity class responsible for sending email
**Methods:**

*  **addAttachment**(self,filePath, fileName) method add attchment to message. Attachment type is "application" and subtype is "octet-stream". Method parameters are str type.
*  **sendMail**(self, userEmail, password, mailServer, port) does initial setup that includes secure connection establishment, login to server and send email.
* **message**(self,From, To ,Subject=None,textContent=None ) initialize message structure. Subject and text content is optional.
*  **setContext**(self,textContent) can be used to modify the text context
*  **getMessageObject(self)** return message obeject
*  **! appendTextContext(self)**  *Under development* ! means under development



