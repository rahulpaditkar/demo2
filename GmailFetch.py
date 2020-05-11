import email
import imaplib
import re

username="email address"
password="password"

mail=imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)

mail.select("inbox")
mail.create("items")

result,data=mail.uid('search',None,"All")

inbox_items_list=data[0].split()
old=inbox_items_list[0]

result2,email_data=mail.uid('fetch',old,'(RFC822)')

raw_email=email_data[0][1].decode("UTF-8")

email_message=email.message_from_string(raw_email)
to_=email_message['To']
from_=email_message['From']
Subject_=email_message['Subject']
email_message.get_payload()

counter=1
for part in email_message.walk():
    if part.get_content_maintype()=="multipart":
        continue
    filename=part.get_filename()
    if not filename:
        ext='.html'
        filename='msg-part-%08d%s' %(counter,ext)
    counter +=1

content_type=part.get_content_type()
mails=re.findall(["congratulation"],content_type)
most_recent=mails[-5:-1]
print(mails)







