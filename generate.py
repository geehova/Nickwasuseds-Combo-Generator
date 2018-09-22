import requests
import os
import random
import string
import json
import multiprocessing
from colorama import init
from colorama import Fore, Style

init()

file = input('filename: ')

print(Style.BRIGHT + '  ')
num_lines = sum(1 for line in open('names.json'))
print('Got {} Names!'.format(num_lines))

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'aol.com', 'outlook.com', 'gmx.de', 'gmx.net',
                 'protonmail.com', 'fastmail.com', 'zoho.com',
                 'mail.com', 'hushmail.com']

names = json.loads(open('names.json').read())
surnames = json.loads(open('names.json').read())
words = json.loads(open('words.json').read())

kek = 1


def scam():
    with open(file, 'wb') as f:
        while True:
            name = random.choice(names).lower() + random.choice(surnames).lower()
            name_extra = ''.join(random.choice(string.digits) for i in range(random.randint(1, 4)))
            email_domain = random.choice(email_domains)
            word = random.choice(words)
            word_extra = ''.join(random.choice(chars) for i in range(random.randint(1, 4)))
            email = name + name_extra + '@' + email_domain
            password = word_extra + word + word_extra
            combo = ('{0}:{1} \n'.format(email, password)).encode()
            f.write(combo)
            global kek
            kek = (kek + 1)
            lel = random.randint(1, 2)
            if lel == 1:
                print(Fore.RED + '{}        {}'.format(kek, combo))
            if lel == 2:
                print(Fore.CYAN + '{}       {}'.format(kek, combo))
            pass


if __name__ == '__main__':
    worker_0 = multiprocessing.Process(
        name='worker 0',
        target=scam(),
    )
    worker_1 = multiprocessing.Process(
        name='worker 1',
        target=scam(),
    )
    worker_2 = multiprocessing.Process(
        name='worker 2',
        target=scam(),
    )
    worker_3 = multiprocessing.Process(
        name='worker 3',
        target=scam(),
    )
    worker_4 = multiprocessing.Process(
        name='worker 4',
        target=scam(),
    )
    worker_5 = multiprocessing.Process(
        name='worker 5',
        target=scam(),
    )
    worker_6 = multiprocessing.Process(
        name='worker 6',
        target=scam(),
    )
    worker_7 = multiprocessing.Process(
        name='worker 7',
        target=scam(),
    )
    worker_8 = multiprocessing.Process(
        name='worker 8',
        target=scam(),
    )
    worker_9 = multiprocessing.Process(
        name='worker 9',
        target=scam(),
    )
    worker_10 = multiprocessing.Process(
        name='worker 10',
        target=scam(),
    )
    worker_11 = multiprocessing.Process(
        name='worker 11',
        target=scam(),
    )
    worker_12 = multiprocessing.Process(
        name='worker 12',
        target=scam(),
    )
    worker_13 = multiprocessing.Process(
        name='worker 13',
        target=scam(),
    )
    worker_14 = multiprocessing.Process(
        name='worker 14',
        target=scam(),
    )
    worker_15 = multiprocessing.Process(
        name='worker 15',
        target=scam(),
    )
    worker_16 = multiprocessing.Process(
        name='worker 16',
        target=scam(),
    )
    worker_17 = multiprocessing.Process(
        name='worker 17',
        target=scam(),
    )
    worker_18 = multiprocessing.Process(
        name='worker 18',
        target=scam(),
    )
    worker_19 = multiprocessing.Process(
        name='worker 19',
        target=scam(),
    )
    worker_20 = multiprocessing.Process(
        name='worker 20',
        target=scam(),
    )
    worker_21 = multiprocessing.Process(
        name='worker 21',
        target=scam(),
    )
    worker_22 = multiprocessing.Process(
        name='worker 22',
        target=scam(),
    )
    worker_23 = multiprocessing.Process(
        name='worker 23',
        target=scam(),
    )
    worker_24 = multiprocessing.Process(
        name='worker 24',
        target=scam(),
    )
    worker_25 = multiprocessing.Process(
        name='worker 25',
        target=scam(),
    )
    worker_26 = multiprocessing.Process(
        name='worker 26',
        target=scam(),
    )
    worker_27 = multiprocessing.Process(
        name='worker 27',
        target=scam(),
    )

    worker_0.start()
    worker_1.start()
    worker_2.start()
    worker_3.start()
    worker_4.start()
    worker_5.start()
    worker_6.start()
    worker_7.start()
    worker_8.start()
    worker_9.start()
    worker_10.start()
    worker_11.start()
    worker_12.start()
    worker_13.start()
    worker_14.start()
    worker_15.start()
    worker_16.start()
    worker_17.start()
    worker_18.start()
    worker_19.start()
    worker_20.start()
    worker_21.start()
    worker_22.start()
    worker_23.start()
    worker_24.start()
    worker_25.start()
    worker_26.start()
    worker_27.start()
