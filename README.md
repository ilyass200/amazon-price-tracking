# amazon-price-tracking
A Pyton script that allows you to track the price of your favorite Amazon product and send you an email when the desired price is reached

## Installation
- Install pyhton 3
- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the modules.
  ```bash
  pip install requests
  pip install smtplib
  pip install bs4
  pip install email
  ```
## How to use it ?
you have to modify some variables for the script to work well, first modify the **url** variable by putting the link of your favorite productfrom amazon and the variable **MY_USER_AGENT** by putting your user agent (search on Google : "My user agent") 

extracted from the **sendmail()** function 
```python
SMTP_HOST = "smtp.gmail.com" # smtp server
SMTP_PORT = 587 # smtp server port

# Authentication of your smtp server 
MAIL_ADDRESS = ""
PASSWORD = ""

FROM = MAIL_ADDRESS # YOUR MAIL ADDRESS
TO = MAIL_ADDRESS # you can use a LIST type or STRING type
```
1. for the **SMTP_HOST** variable it is the DNS of the smtp **(Simple Mail Transfer Protocol)** server and for **SMTP_PORT** it is the port where it will listen by default I used port 587 (**TLS,Transport Layer Security**) which will allow to encrypt the communication between client-server.
for more information about this port : [Transport Layer Security](https://fr.wikipedia.org/wiki/Transport_Layer_Security)

2. you must then modify the variables **MAIL_ADDRESS** and **PASSWORD**, to connect to the smtp server, if you do not want to put your real password I know that for Google we can generate passwords for applications, for more informations click here : [App passwords](https://devanswers.co/create-application-specific-password-gmail) 

![Generated app password](https://www.shoutmeloud.com/wp-content/uploads/2013/04/Google-Authenticator-app-password.png)

to finish you just have to modify the **FROM** and **TO** variables for sending mail, for the **TO** variable you can use a list if you want to send to several people (ex : [example1@gmail.com, example2@gmail.com])

## Make the script more powerful

instead of using this command 
```bash
python .\amazon-price-tracking.py
```
it's better to run your script regularly and automatically on your computer, for **Linux** there is a **[crontab](https://www.raspberrypi.org/documentation/linux/usage/cron.md)** command, for **Windows** I don't know any particular command but I've seen that **[Scheduled Tasks](https://www.digitalcitizen.life/how-create-task-basic-task-wizard)** can do the job.

