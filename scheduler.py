#https://stackoverflow.com/questions/21214270/scheduling-a-function-to-run-every-hour-on-flask
import time
import atexit
from datetime import timezone

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from EmailActivity import EmailActivity
from JsonLoader import JsonLoader
from FileIO import FileIO
from datetime import datetime

def job():
    perser = JsonLoader()
    perser.loadJsonData('https://borda-shopping.now.sh/items')
    print(perser.getJsonData())
    file= FileIO()
    file=file.createCSVFile(perser.getJsonData())
    email = EmailActivity()
    email.message("abu.musa.rabiul@gmail.com","dawoodmuzammil@hotmail.com","Food request list", 'sending this week\'s food list')
    email.addAttachment(file)
    email.setUpSenderCredential("abu.musa.rabiul@gmail.com",'Acifl1234','smtp.gmail.com',587)
def hello():
    print("hellow")
app = Flask(__name__)
# BUG: ValueError: Timezone offset does not match system offset: 10800 != 7200. Please, check your config files.
#solve specific timezone
scheduler = BackgroundScheduler(timezone="europe/istanbul")
#https://apscheduler.readthedocs.io/en/latest/modules/triggers/date.html
scheduler.add_job(func=hello, trigger="date", run_date= datetime(2019,8,23,18, 18, 0 ))
# Explicitly kick off the background thread
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
#run app
#BUG: flask execute job twich
#https://stackoverflow.com/questions/14874782/apscheduler-in-flask-executes-twice
if __name__ == '__main__':
    app.run(debug= True, use_reloader=False)