import requests
import os
import random
import string
import json
import sys
import argparse
import concurrent.futures
import NicksLibary as nick
from colorama import init
from colorama import Fore, Style
from tqdm import tqdm

nick.settitle('Nickwasused´s Combo Generator')

init()

file = input('filename: ')

counter = 0
kek = 0

try:
    print(Style.BRIGHT + '  ')
    num_lines = sum(1 for line in open('names.json'))
    print('Got {} Names!'.format(num_lines))

    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(2048))
    email_domains = ['gmail.', 'yahoo.', 'hotmail.', 'aol.', 'outlook.', 'gmx.', 'Yandex.', 'icloud', 'tutanota',
                     'protonmail.', 'fastmail.', 'zoho.', 'mail.', 'hushmail.', 'aichi.', 'aim.', 'airforce.', 'airforceemail.', 'airmail.', 'airpost.']

    domain_end = ['com', 'org', 'net', 'int', 'edu', 'gov', 'ac', 'ad', 'ae', 'af', 'ag', 'ai', 'al', 'am', 'an', 'ao', 'aq', 'ar', 'as', 'at', 'au', 'aw', 'ax', 'az', 'ba', 'bb', 'bd',
                  'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bl', 'bm', 'bn', 'bn', 'bm', 'bo', 'bq', 'br', 'bs', 'bt', 'bw', 'by', 'bz', 'ca', 'cc', 'cd', 'cf', 'cg', 'ch', 'ci', 'ck', 'cl',
                  'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'fi', 'fj', 'fk', 'fm', 'fo', 'fr', 'ga', 'gd', 'ge', 'gf', 'gg', 'gh', 'hk', 'hm', 'hn', 'hr', 'ht', 'hu',
                  'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'er', 'es', 'et', 'eu', 'id', 'ie', 'il', 'im', 'in', 'io', 'iq', 'is', 'it', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh',
                  'ki', 'km', 'kn', 'kp', 'kr', 'li', 'ma', 'mc', 'md', 'mh', 'nl', 'no', 'np', 'nz', 'om', 'pa', 'pl', 'rs', 'ru', 'sa', 'sd', 'se', 'sg', 'si', 'sk', 'tc', 'td', 'tr',
                  'tw', 'ua', 'ug', 'uk', 'um', 'us', 'uz', 'uy', 'vn', 'vu', 'za', 'zm', 'zw', 'mail']

    names = json.loads(open('names.json', encoding="utf8").read())
    surnames = json.loads(open('names.json', encoding="utf8").read())
    passwordlist = json.loads(open('passlist.json', encoding="utf8").read())

except FileNotFoundError:
    print('You are missing the Following Files: names.json, passlist.json')

def maincombo():
    global counter
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    password = random.choice(passwordlist)
    combo = ('{0}:{1}'.format(email, password)).encode()
    counter = (counter + 1)
    return combo

def mainmail():
    global counter
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    combo = ('{0}'.format(email)).encode()
    counter = (counter + 1)
    return combo

def writecombo():
    with open(file, 'ab') as f:
            combo = maincombo() + '\n'.encode()
            f.write(combo)
            f.close()

def writemail():
    with open(file, 'ab') as f:
            combo = mainmail() + '\n'.encode()
            f.write(combo)
            f.close()

def generatecombo():
    global kek
    while True:
        kek = (kek + 1)
        print('Generating Wave: {}'.format(kek))
        for counter in tqdm(range(10000), unit='Combos'):
            writecombo()
            
def generateemail():
    global kek
    while True:
        kek = (kek + 1)
        print('Generating Wave: {}'.format(kek))
        for counter in tqdm(range(10000), unit='Combos'):
            writemail()

with concurrent.futures.ProcessPoolExecutor() as executor:
    print('avalible modes: standard(email:pass), email(email)')
    argument = input('Mode: ')
    if argument == 'email':
        while True:
            generateemail()
    else:
        while True:
            generatecombo()
