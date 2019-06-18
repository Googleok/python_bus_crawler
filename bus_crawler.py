import ssl
import sys
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen
import pandas as pd
from bs4 import BeautifulSoup

def crawling_bus():
    results = []
    service_key = 'Mvvb2YR7v%2FkqieXftzctgHhiSB%2BQ6RhTS3PLa7wCPCmKY7vt4sZ9TwZxv8Q9VmSn0IxdZgHSv7661X3bu4ZaaA%3D%3D'
    stId = '120000005'
    busRouteId = '100100071'
    ord = '50'
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?serviceKey='+service_key+'&stId='+stId+'&busRouteId='+busRouteId+'&ord='+ ord

    html = request_url(url)
    print(html)
    bs = BeautifulSoup(html, 'html.parser')
    arrmsg2 = bs.find('arrmsg2')
    print(arrmsg2.text)
    # addresses = bs.findAll('div', attrs={'class': 'shopAdd'})
    #
    # for i in range(len(names)):
    #     sidogu = addresses[i].text.split(' ')[0:2]
    #     results.append((names[i].text, addresses[i].text) + tuple(sidogu))
    #
    #
    # # store      -> pandas
    # table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    # table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)

def request_url(url):
    try:
        request = Request(url)
        ssl._create_default_https_context = ssl._create_unverified_context
        response = urlopen(request)
        receive = response.read()
        html = receive.decode('utf-8', errors='replace')
        # print(html)
        print(f'{datetime.now()}: success for request [{url}]')
    except Exception as e:
        print(f'{e} : {datetime.now()}', file=sys.stderr)
    return html

if __name__ == '__main__':
    # pericana
    # crawling_pericana()

    # nene 과제
    crawling_bus()