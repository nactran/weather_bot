# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from getWether import getWether
import datetime
header = '揉揉萌三三：\n这是机器人自动生成的短消息。\n'
def getDate():
    dt = datetime.datetime.now()
    mes = "今天是"+str(dt.year)+"年"+str(dt.month)+"月"+str(dt.day)+"日"+"。\n"
    return mes
def sendMessage(mes):
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC7ec153dbfab1157c2aca4459d4063c4c'
    auth_token = '49ee45431955922827c69b5135f3fa15'
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body= mes,
                     from_='+17744506041',
                     to='+8613121772599'
                 )

    print(message.sid)

if __name__ == '__main__':
    message = header
    message += getDate()
    message += getWether()
    print('****预览****\n')
    print(message)
    input('按任意键确认发送')
    sendMessage(message)
