'''
Created on 9 juil. 2017

@author: leo
'''
import hashlib
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def find_answer(words):
    for word1 in words:

        for word2 in words:

            w = word1 + word2
            md5_hex = hashlib.md5(str.encode(w))
            if md5_hex.hexdigest() == answer:
                return w

if __name__ == '__main__':
    answer = "2e52b110695075c2c733e2f0ee69f59f"
    f = "wordlist.txt"
    with open(f, 'r') as fid:
        words = fid.read()

    futures = []
    with ProcessPoolExecutor(20) as executor:


        for chunk in chunks(words, int(len(words) / 10)):
            futures.append(executor.submit(find_answer, chunk))

        for x in as_completed(futures):
            if x.result() is not None:
                print(x.result())



