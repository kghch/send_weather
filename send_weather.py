# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

m_host = "smtp.163.com"
m_user = "fdwanghan"
m_password = "tongtong"

sender = 'fdwanghan@163.com'
receivers = ['fdwanghan@163.com']

sender_name = "i@github.com"
receiver_name = ""

f = open('./weather/wea.txt', 'r')
content = f.read()
f.close()

message = MIMEText(content, 'plain', 'utf-8')
message['From'] = Header(sender_name)
message['To'] = Header(receiver_name)

subject = '天气预报:)'
message['subject'] = Header(subject, 'utf-8')

try:
	smtpObj = smtplib.SMTP()
	smtpObj.connect(m_host, 25)
	smtpObj.login(m_user, m_password)
	smtpObj.sendmail(sender, receivers, message.as_string())
	print "email sent."

except Exception, e:
	print e