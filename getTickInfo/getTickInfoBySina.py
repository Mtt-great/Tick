import requests


def sina( tickNum ):

    url = 'http://hq.sinajs.cn/list='+tickNum
    headers = {'Referer':'https://finance.sina.com.cn/' }
    tickInfo = requests.get(url, headers=headers).text
    tickData = tickInfo.split('=')[1].replace('"','').replace(';','').replace('\n','').split(',')

    print(tickData)