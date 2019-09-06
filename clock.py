from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from EmailActivity import EmailActivity
from JsonLoader import JsonLoader
from FileIO import FileIO
from datetime import datetime
import pytz
import os


def getCurrentDateTime(timezone):
    zone = pytz.timezone(timezone)
    return datetime.now(zone)


def apiRouteForBranch(branch):
    return 'https://borda-shopping.now.sh/items/' + branch + '/week/'


def job():
    perser = JsonLoader()
    apiRouteIstanbul = apiRouteForBranch('istanbul')
    apiRouteIzmir = apiRouteForBranch('izmir')
    getCurrentWeek = getCurrentDateTime('europe/istanbul').isocalendar()[1]
    getPreviousWeek = getCurrentWeek - 1
    apiRouteIstanbul = apiRouteIstanbul + str(getCurrentWeek) # Need to change to getPreviousWeek

    apiRouteIzmir = apiRouteIzmir + str(getCurrentWeek)  # Need to change to getPreviousWeek
    # Get json data from apiroute call
    perser.loadJsonData(apiRouteIstanbul)
    dataIstanbul = perser.getJsonData()

    perser.loadJsonData(apiRouteIzmir)
    dataIzmir = perser.getJsonData()

    # Create file that has to be sent as notification
    file = FileIO()
    fileIstanbul = file.createCSVFile(dataIstanbul, 'istanbul')
    fileIzmir = file.createCSVFile(dataIzmir, 'izmir')

    # reading environment variables

    senderEmail = os.environ['SENDER_EMAIL']
    senderPassword = os.environ['SENDER_PASSWORD']
    # getting senderName and password
    # print(senderEmail)
    # print(senderPassword)

    msg = "The attached file has last week's food request list."
    # send email activities
    email = EmailActivity()
    email.message(senderEmail, "eylul.sert@bordatech.com",
                  "Food request list", msg)
    email.addAttachment("./files/" + fileIstanbul, fileIstanbul)
    email.addAttachment("./files/" + fileIzmir, fileIzmir)
    email.sendMail(senderEmail, senderPassword, 'smtp.gmail.com', 587)


app = Flask(__name__)
# BUG(26/08/2019): ValueError: Timezone offset does not match system offset: 10800 != 7200. Please, check your config files.
# solve specify timezone
scheduler = BackgroundScheduler(timezone="europe/istanbul")
scheduler.add_job(func=job, trigger='cron', day_of_week='fri', hour='9', minute='45', second='0')
# Explicitly kick off the background thread
scheduler.start()

# BUG: flask execute job twich
# https://stackoverflow.com/questions/14874782/apscheduler-in-flask-executes-twice
# run app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
