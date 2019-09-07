import requests
from bs4 import BeautifulSoup
import re
import os
import json
def getWether():
    mes = ''
    hasWeather = False
    r = requests.get('http://www.weather.com.cn/weather1d/101230101.shtml')
    r.encoding = 'utf-8'
    wres = re.search(r'hour3data=(.*?)}',r.text)
    #print(res[0])
    fileObj = open('hour3data.json','w')
    fileObj.write(wres[1]+'}')
    fileObj.close()
    if os.path.exists(os.path.join(os.getcwd(),'hour3data.json')):
        with open("hour3data.json",'r') as load_f:
            data = json.load(load_f)
        for sen in data['1d']:
            if '08时' in sen:
                hasWeather = True
                senl = sen.split(',')
                if senl[2] in['小雨']:
                    mes = '福州'+senl[0]+'天气状况：'+ senl[2]+'，记得带伞哦'+ '；气温：'+senl[3]+'；风向：'+ senl[4]+'；风力：'+ senl[5]+'。\n'
                else:
                    mes = '福州'+senl[0]+'天气状况：'+ senl[2]+ '；气温：'+senl[3]+'；风向：'+ senl[4]+'；风力：'+ senl[5]+'。\n'
        if not hasWeather:
            print('Something is wrong: Did not find weather data.\n')
            return False

    else:
        print('Something is wrong: Did not find hour3data.json\n')
        return False

    soup = BeautifulSoup(r.text,"html.parser")
    for index in [1,3,6]:
        a = soup.find_all('li','li'+str(index))[0]
        lidx = a.find_all('em')[0].text+'：'+a.find_all('span')[0].text +'；'+a.find_all('p')[0].text
        mes = mes + lidx +'\n'
    return mes

if __name__ == '__main__':
    res = getWether()
    if res:
        print(res)

