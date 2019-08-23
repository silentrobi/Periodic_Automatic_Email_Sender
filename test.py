
from EmailActivity import EmailActivity




from JsonLoader import JsonLoader
from FileIO import FileIO

perser = JsonLoader()
perser.loadJsonData('https://borda-shopping.now.sh/items')
print(perser.getJsonData())
file= FileIO()
file=file.createCSVFile(perser.getJsonData())
email = EmailActivity()

email.message("abu.musa.rabiul@gmail.com","dawoodmuzammil@hotmail.com","Food request list", 'sending this week\'s food list')
email.addAttachment(file)
email.setUpSenderCredential("abu.musa.rabiul@gmail.com",'Acifl1234','smtp.gmail.com',587)