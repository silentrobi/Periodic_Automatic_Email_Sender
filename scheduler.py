
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from EmailActivity import EmailActivity
from JsonLoader import JsonLoader
from FileIO import FileIO
from datetime import datetime
import pytz
import yaml


def getCurrentDateTime(timezone):
    zone = pytz.timezone(timezone)
    return datetime.now(zone)


def job():
    perser = JsonLoader()
    route= 'https://borda-shopping.now.sh/items/week/'
    getCurrentWeek = getCurrentDateTime('europe/istanbul').isocalendar()[1]
    getPreviousWeek= getCurrentWeek - 1
    apiRoute= route+ str(getPreviousWeek)

    #Get json data from apiroute call
    perser.loadJsonData(apiRoute)
    print(perser.getJsonData())

    #Create file that has to be sent as notification
    file= FileIO()
    file=file.createCSVFile(perser.getJsonData())

    #reading yml file
    try:
        conf= yaml.safe_load(open('./conf/config.yml'))
    except Exception as e:
        print(e)
    #getting senderName and password
    senderEmail= conf['user']['email']
    senderPassword= conf['user']['password']

    #send email activities
    email = EmailActivity()
    email.message(senderEmail,"mohammad.rabiul@bordatech.com",
                  "Food request list",
                  'First successful test of shopping list and email sending micro services. '
                  'I have attached  the list of items to be bought for Izmir office for the next week.ş')
    email.addAttachment("./files/"+file, file)
    email.sendMail(senderEmail,senderPassword,'smtp.gmail.com',587)

app = Flask(__name__)
# BUG(26/08/2019): ValueError: Timezone offset does not match system offset: 10800 != 7200. Please, check your config files.
#solve specific timezone
scheduler = BackgroundScheduler(timezone="europe/istanbul")
scheduler.add_job(func=job, trigger='cron', day_of_week= 'mon', hour='17', minute= '21', second='0')

# Explicitly kick off the background thread
scheduler.start()

#BUG: flask execute job twich
#https://stackoverflow.com/questions/14874782/apscheduler-in-flask-executes-twice
#run app
if __name__ == '__main__':
    app.run(debug= True, use_reloader=False)