'''
Created on 9 juil. 2017

@author: leo
'''

from requests import Request, Session
from bs4 import BeautifulSoup
session = Session()

if __name__ == '__main__':
    url = r"https://www.0xf.at/play/22"
    r = session.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    inp = r"1833891c2ff53708a4de8612cfb51cc1"
    print (inp)
    answer = inp + ''.join(reversed(inp[:-1]))
    print (answer)
    url += r"?pw=" + answer
    r = session.post(url)
    with open("answer_22.html", 'wb') as fid:
        fid.write(r.content)

