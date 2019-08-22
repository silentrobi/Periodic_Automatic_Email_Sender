
from EmailActivity import EmailActivity

email = EmailActivity()

email.message("abu.musa.rabiul@gmail.com","silentrobi840@gmail.com","Food request list", 'sending this week\'s food list')
email.addAttachment("1.csv")
email.setUpSenderCredential("abu.musa.rabiul@gmail.com",'12345','smtp.gmail.com',587)
