'''
Created on 9 juil. 2017

@author: leo
'''
import hashlib
from tqdm import tqdm
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor
import gc

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def find_answer(word1, words):

    for word2 in words:

        w = word1 + word2
        md5_hex = hashlib.md5(str.encode(w))
        if md5_hex.hexdigest() == answer:
            print("Found ! ==> %s" % w)
            return w

if __name__ == '__main__':
    answer = "2e52b110695075c2c733e2f0ee69f59f"
    f = "wordlist.txt"
    with open(f, 'r') as fid:
        words = fid.readlines()

    with open("words.rule", 'w') as rule_list:
        for word in words:
            word = word.strip()
            for c in word:
                rule_list.write('$')
                rule_list.write(c)
                rule_list.write(' ')
            rule_list.write('\n')


#     futures = []
#     with ProcessPoolExecutor(20) as executor:
#
#         for word1 in tqdm(words):
#             for chunk in chunks(words, 50000):
#                 futures.append(executor.submit(find_answer, word1, chunk))
#             if len(futures) >= 10000:
#                 print("checking done futures")
#                 for future in tqdm(as_completed(futures)):
#                     res = future.result()
#                     if res is not None:
#                         print(res)
#                         exit(0)
#                 print("\n\n\nflushing done futures")
#                 futures = []
#                 gc.collect()
#
#
#         print("finished submitting")







