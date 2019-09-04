
from EmailActivity import EmailActivity

from datetime import datetime
import pytz
utc = pytz.utc
istanbul= pytz.timezone('europe/istanbul')
import os


from JsonLoader import JsonLoader
from FileIO import FileIO
perser = JsonLoader()
perser.loadJsonData('https://borda-shopping.now.sh/items/izmir/week/36')
print(perser.getJsonData())
file= FileIO()
file=file.createCSVFile(perser.getJsonData())
email = EmailActivity()


'''
email.message("abu.musa.rabiul@gmail.com","silentrobi840@gmail.com","Food request list", 'First successful test of shopping list and email sending micro services. Attached is the list of items to be bought for Izmir office for the next week.')
email.addAttachment(file)
email.setUpSenderCredential("abu.musa.rabiul@gmail.com",'Acifl1234','smtp.gmail.com',587)

'''

'''
print(datetime.now().isocalendar()[1])
print(datetime.now(istanbul))
username = os.environ["DEBUSSY"]
print(username)
'''