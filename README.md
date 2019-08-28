# Periodic automatic weekly email nofication sender microservice

# Project documantation
The project has following classes and script files.

# EmailActivity -- *class*

EmailActivity class responsible for sending email.
**Methods:**

*  **addAttachment**(self,filePath, fileName) method add attchment to message. Attachment type is "application" and subtype is "octet-stream". Method parameters are str type.
*  **sendMail**(self, userEmail, password, mailServer, port) does initial setup that includes secure connection establishment, login to server and send email.
* **message**(self,From, To ,Subject=None,textContent=None ) initialize message structure. Subject and text content is optional.
*  **setContext**(self,textContent) can be used to modify the text context
*  **getMessageObject(self)** return message obeject
*  **! appendTextContext(self)**  *Under development*. ! means under development

# FileIO -- *class*
FileIO class creates CSV file. More methods can be added to this class like 'createPdfFile()

**Methods:**

*  *createCSVFile*(self, jsonData) takes json data as input and create a csv file of that data. This method can be modifed to create a csv file of variable numbers of fields.

# JsonLoader -- *class*
JsonLoader class load jsondata from url

# clock -- *script file*

clock.py script file runs cron job that sends weekly mail. 

*  **getCurrentDateTime**(timezone) return the current date
*  **job**()  contains all operations to send email weekly.

In this script file APScheluder library is used to create 'cron' job. 
There are different scheduler in APScheduler. Most suitables are BlockingScheduler and BackgroundScheduler class.

**Note:** if BlockScheduler is used, then there is no need to use Flask or infinite loop in clock.py file as start() method never returns. However if BackgroundScheduler is used then we need 
`if __name__ == '__main__':
    app.run(debug= True, use_reloader=False)`
code or infinite loop `while True:
    time.sleep(2)` code at the end of the clock.py file.

Check the following links for more information:
[BlockScheduler](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/blocking.html#apscheduler.schedulers.blocking.BlockingScheduler)
[BackgroundScheduler](https://apscheduler.readthedocs.io/en/latest/modules/schedulers/background.html#apscheduler.schedulers.background.BackgroundScheduler)

# Hosting on Heroku

1. Login to hereku `hereku login`
2. Create a new Git repository:<br/>
     `cd my-project/`
     `git init`
     `heroku git:remote -a <project name>`
3.set environment variable
     `heroku config:set SENDER_EMAIL=<email> SENDER_PASSWORD=<password>`
    
4. Deploy the application 
     `git add .`
     `git commit -am "message"`
     `git push heroku master`
     `heroku ps:scale clock=1` --This is a singleton process, meaning you’ll never need to scale up more than 1 of these processes. 
  

