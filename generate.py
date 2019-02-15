import requests
import os
import random
import string
import json
import concurrent.futures
from colorama import init
from colorama import Fore, Style

init()

file = input('filename: ')

print(Style.BRIGHT + '  ')
num_lines = sum(1 for line in open('names.json'))
print('Got {} Names!'.format(num_lines))

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
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

def generate():
    name = random.choice(names).lower() + random.choice(surnames).lower()
    name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
    email_domain = random.choice(email_domains) + random.choice(domain_end)
    email = name + name_extra + '@' + email_domain
    password = random.choice(passwordlist)
    combo = ('{0}:{1}'.format(email, password)).encode()
    return combo

def gen():
    with open(file, 'ab') as f:
            combo = generate() + '\n'.encode()
            f.write(combo)
            f.close()

with concurrent.futures.ProcessPoolExecutor() as executor:
    while True:
        gen()
