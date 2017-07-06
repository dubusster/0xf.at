'''
Created on 6 juil. 2017

@author: leo
'''

LETTER_DICT = {
    'abc2':2,
    'def3':3,
    'ghi4':4,
    'jkl5':5,
    'mno6':6,
    'pqrs7':7,
    'tuv8':8,
    'wxyz9':9,
    ' 0': 0
    }

def get_number(inp):
    inp = str(inp)
    res = 0
    for c in inp:
        for key in LETTER_DICT.keys():
            if c in key:
                idx = key.index(c) + 2
                res += idx * LETTER_DICT[key]
    return res

def get_inp(url):
    pass


if __name__ == '__main__':
    inp = '29c9f7c4b35e2213079440ab776f57db'
    res = get_number(inp)

    print(res)
