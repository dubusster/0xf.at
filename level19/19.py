'''
Created on 6 juil. 2017

@author: leo
'''
from bs4 import BeautifulSoup
import requests



LETTER_DICT = {
    'abc':2,
    'def':3,
    'ghi':4,
    'jkl':5,
    'mno':6,
    'pqrs':7,
    'tuv':8,
    'wxyz':9,
    ' ': 0
    }

def get_number(inp):
    inp = str(inp)
    res = 0
    for c in inp:
        if c in '0123456789':
            res += int(c)
        else:
            for key in LETTER_DICT.keys():
                if c in key:
                    idx = key.index(c) + 2
                    res += idx * LETTER_DICT[key]


    return res

def get_inp(url):
    pass


if __name__ == '__main__':

    url = r"https://www.0xf.at/play/19"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    inp = soup.code.text
    inp = get_inp(url)
#     inp = "73c373439df3be72004143632fef2e0c"
    res = get_number(inp)
    url += "?pw=" + str(res)
    r2 = requests.get(url)
    print(r2)
    soup = BeautifulSoup(r2.content, 'html.parser')
    print(soup)
    print(res)
