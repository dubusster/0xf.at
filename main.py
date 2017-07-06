'''
Created on 6 juil. 2017

@author: leo
'''

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

def get_number():
    pass

if __name__ == '__main__':
    inp = 'hey'
    res = 0
    for c in inp:
        for key in LETTER_DICT.keys():
            if c in key:
                idx = key.index(c) + 1
                res += LETTER_DICT[key]

    print(res)
