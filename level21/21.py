'''
Created on 9 juil. 2017

@author: leo
'''

from bs4 import BeautifulSoup
from requests import Session
# import requests
from concurrent.futures import as_completed, ProcessPoolExecutor
from subprocess import call
from itertools import permutations
import clipboard
import pyperclip

s = Session()

def get_words_from_site(url=r"https://www.0xf.at/play/21"):
    r = s.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    inp = soup.code.text
    words = inp.split(';')
    return words


def worker(word):
    answers = {}
    for perm in permutations(word):
        if perm in word_list:
            print(perm)
            answers[word] = perm
    return answers

if __name__ == '__main__':

    word_list_filename = r"dictionary.txt"
    url = r"https://www.0xf.at/play/21"
#     inp = r"taesthre;zgdalee;durretbis;iorcsecen;lielfy;fancovre;edphunia;nultxiosa;teidnatpuo;omdry"
    words = get_words_from_site(url)
    futures = []
    word_list = []
    signatures = {}
    with open(word_list_filename, 'r') as fid:
        lines = fid.readlines()

        for line in lines:
            word = line.strip()
            word_list.append(word)
            if ''.join(sorted(word)) in signatures.keys():
                print("already in dict !")
            signatures[''.join(sorted(word))] = word

    answer = []
    for word in words:
        ans = signatures[''.join(sorted(word))]
        answer.append(ans)
    answer_str = ';'.join(answer)
    clipboard.copy(answer_str)
    print(answer_str)
    url += r"?pw=" + answer_str
    r = s.post(url)
    print(r.content)

#     with ProcessPoolExecutor(8) as executor:
#         for word in words:
#             futures.append(executor.submit(worker, word))
#
#         for future in as_completed(futures):
#             print(future.result())




