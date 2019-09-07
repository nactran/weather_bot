import itchat
from getWether import getWether
import datetime
from LunarSolarConverter import LunarSolarConverter
lunarmonthDict = {1:"正",2:"二",3:"三",4:"四",5:"五",6:"六",7:"七",8:"八",9:"九",10:"十",11:"十一",12:"十二"}
lunarDateDict = {1:"初一",2:"初二",3:"初三",4:"初四",5:"初五",6:"初六",7:"初七",8:"初八",9:"初九",10:"初十",11:"十一",12:"十二",13:"十三",
                14:"十四",15:"十五",16:"十六",17:"十七",18:"十八",19:"十九",20:"二十" ,21:"廿一",22:"廿二",23:"廿三",24:"廿四",25:"廿五",
                 26:"廿六",27:"廿七",28:"廿八",29:"廿九",30:"三十"}
header = '揉揉萌三三：\n这是机器人自动生成的短消息。\n'
def getDate():
    dt = datetime.datetime.now()
    mes = "今天是"+str(dt.year)+"年"+str(dt.month)+"月"+str(dt.day)+"日"+"。"
    converter = LunarSolarConverter.LunarSolarConverter()
    solar = LunarSolarConverter.Solar(dt.year, dt.month, dt.day)
    lunar = converter.SolarToLunar(solar)
    lunarDate = vars(lunar)
    mes += "农历"
    if(lunarDate["isleap"]):
        mes += "闰"
    mes = mes + lunarmonthDict[lunarDate['lunarMonth']]+ '月' + lunarDateDict[lunarDate['lunarDay']] + '。\n'
    return mes
def sendMessage(mes):
    itchat.auto_login()
    print('****预览****\n')
    print(mes)
    input('按任意键确认发送')
    user_info = itchat.search_friends(name='萌三三')
    print(user_info)
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        itchat.send_msg(mes,user_name)
        print('发送成功')
    else:
        print('用户不存在')

if __name__ == '__main__':
    message = header
    message += getDate()
    message += getWether()
    sendMessage(message)
