import requests


def getTickInfoByTencent( tickNum ):

    url = 'http://qt.gtimg.cn/q='+tickNum
    tickInfo = requests.get(url).text
    tickData = tickInfo.split('=')[1].replace('"','').replace(';','').replace('\n','').split('~')

    print(tickData)