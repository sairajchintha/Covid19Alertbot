import requests
import json
import time
from twilio.rest import Client
import os

r = requests.get('https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise')
pdata=r.json()


def sendmsg(msg,number):
    account_sid = "Your Twilio SID here"
    auth_token = "Your Auth_Token Here"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body=msg,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+'+number,
                          )
    print(message.sid)

def update(pdata):
    r = requests.get('https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise')
    data=r.json()
    duty=data['data']['statewise']
    pduty=pdata['data']['statewise']
    if duty!=pduty:
        return data
    else:
        return False

numbers=['919999999999']#add your recievers mobile numbers in this list in specified format seperated by a comma,
while True:

    if update(pdata):
        newdata=update(pdata)
        duty=newdata['data']['statewise']
        pduty=pdata['data']['statewise']
        for i,j in zip(pduty,duty):
            #print('state : '+i['state'])
            #print('------>Confirmed :' +str(i['confirmed']))
            #print('------>Recovered :' +str(i['recovered']))
            #print('------>Death :'+str(i['deaths']))
            #print('------>Active :' +str(i['active']))
            if(i['confirmed']!=j['confirmed']):
                for num in numbers:
                    #print(f"The State  {i['state']} got {j['confirmed']-i['confirmed']} new cases \n Script is Made with Python by Sairaj",num)
                    #print(f"Total cases in india are {newdata['data']['total']['confirmed']}")
                    sendmsg(f"The State  {i['state']} got {j['confirmed']-i['confirmed']} new cases \nTotal cases in india are {newdata['data']['total']['confirmed']} \n Script is Made with Python by Sairaj",num)
        pdata=newdata
    time.sleep(1)



