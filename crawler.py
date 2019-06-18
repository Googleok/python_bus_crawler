import ssl
import sys
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup


def crawling_pericana():
    results = []
    for page in count(start=11):

        url = 'https://pelicana.co.kr/store/stroe_search.html?page=1&branch_name=&gu=&si=&page=%d'
        html = request_url(url, page)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split(' ')[:2]
            results.append((name, address) + tuple(sidogu))

        # store      -> pandas
        table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
        table.to_csv('__results__/pericana.csv', encoding='utf-8', mode='w', index=True)
def crawling_nene():
    results = []
    for page in count(start=1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?ex_select=1&ex_select2=&IndexSword=&GUBUN=A&page=%d'
        html = request_url(url, page)

        bs = BeautifulSoup(html, 'html.parser')
        names = bs.findAll('div', attrs={'class': 'shopName'})
        addresses = bs.findAll('div', attrs={'class': 'shopAdd'})

        for i in range(len(names)):
            sidogu = addresses[i].text.split(' ')[0:2]
            results.append((names[i].text, addresses[i].text) + tuple(sidogu))

        # 끝 검출
        if(len(names) != 24):
            break

        # store      -> pandas
        table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
        table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)

def request_url(url, page):
    url = url % page
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
    crawling_nene()