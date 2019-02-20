import random
import string
import json
import os
import sys
import urllib3
import colorama
import ctypes
import requests
import concurrent.futures
from pathlib import Path
from colorama import init
from colorama import Fore, Style
from tqdm import tqdm


def checkfilewindows():
    my_file = Path("proxylist.txt")
    if my_file.is_file():
        print('removing proxylist.txt')
        os.remove("proxylist.txt")  # removing the File "proxylist.txt" to remove duplicats
        os.system('fsutil file createnew proxylist.txt 1')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass
    else:
        os.system('fsutil file createnew proxylist.txt 1')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass


def checkfilelinux():
    my_file = Path("proxylist.txt")
    if my_file.is_file():
        print('removing proxylist.txt')
        os.system("rm proxylist.txt")  # removing the File "proxylist.txt" to remove duplicats
        os.system('touch proxylist.txt 1')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass
    else:
        os.system('touch proxylist.txt')  # creating the File "procylist.txt"
        print('creating proxylist.txt')
        pass

def download(url, filename):
    chunk_size = 1000000
    url = url
    filename = filename
    a = requests.get(url, stream=True)
    total_size_1 = int(a.headers['content-length'])
    with open(filename, 'wb') as f:
        for data in tqdm(iterable=a.iter_content(chunk_size=chunk_size), total=total_size_1 / chunk_size, unit='MB'):
            f.write(data)

def settitle(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
