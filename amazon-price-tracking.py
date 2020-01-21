"""

@Author : AJDAINI Ilyass
@GitHub : https://github.com/ilyass200

"""

import requests 
import smtplib 
from bs4 import BeautifulSoup 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = "https://www.amazon.fr/dp/B07XRQM32Q/ref=fr_a_phonex_0" # put your amazon product url here 
MY_USER_AGENT = "" # search on Google "My user agent"

headers = {"User-Agent":MY_USER_AGENT}
print('init...')

request = requests.get(url,headers=headers)

print(request.status_code)

if request.status_code == 200:
	print('request done !')
else:
	raise Exception('Oops, Error',request.status_code)

content = request.content
soup = BeautifulSoup(content,'html.parser')

price_obj = str(soup.find(id="priceblock_ourprice").text)
product_title = str(soup.find(id="productTitle").text.strip())
price_obj = float(price_obj.strip()[:-1].replace(',','.'))
price_to_display = str(soup.find(id="priceblock_ourprice").text)

desired_price = 790

def sendmail():
	
	SMTP_HOST = "smtp.gmail.com" # smtp server
	SMTP_PORT = 587 # smtp server port

	# Authentication of your smtp server 
	MAIL_ADDRESS = ""
	PASSWORD = ""

	FROM = MAIL_ADDRESS # YOUR MAIL ADDRESS
	TO = MAIL_ADDRESS # you can use a LIST type or STRING type)


	server = smtplib.SMTP(SMTP_HOST,SMTP_PORT)	
	server.ehlo()
	server.starttls()
	server.ehlo()

	login = server.login(MAIL_ADDRESS,PASSWORD)

	Subject = "amazon price tracking"
	Body = "your product ",product_title," has had the price that you have desired link : ",url

	msg = MIMEMultipart()
	msg['Subject'] = Subject
	msg['From'] = FROM
	msg['To'] = TO

	html = """\
	<html>
	  <head>
	  	<link href="https://fonts.googleapis.com/css?family=Roboto&display=swap" rel="stylesheet">
	  </head>
	  <body>
	    <h2>{}</h2>
	    <img src="https://cdn.1min30.com/wp-content/uploads/2017/12/symbole-amazone.jpg" height="300" width="500"></img>
	    <h2 style="color:#DF7401;"><strong><span style="position: relative; top: -20px;">your product has had the price that you have desired <em>(desired price : {})</em>!</span></strong></h2>
	    <h2>price : <strong style="color:#04B486;">{}</strong></h2>
	    <h2>url : <a href="{}"><strong>{}</strong></a></h2>
	  </body>
	</html>
	""".format(product_title,desired_price,price_to_display,url,url)

	content = MIMEText(html, 'html')

	msg.attach(content)
	server.sendmail(FROM, TO, msg.as_string())
	server.quit()

	if isinstance(TO,list):
		print('Message sended to',' & '.join(TO))
	else:
		print('Message sended to',TO)

if desired_price <= price_obj:
	try:
		sendmail()
	except Exception as e:
		raise Exception("Oops, an error occurred, ",e)
else:
	print('the price still does not have the price you want, wait and try again !')


