#!/usr/bin/env python3

import os
import requests
import sys
import termcolor
import argparse

class MyDirb:
    def __init__(self):
        banner = """
        dir_finder V1.0
        Directory enumeration tool
        by nosebleeeddd
        """
        print(banner)
        self.url_base = self.get_info()[0]
        self.wordlist = self.get_info()[1]

    def get_info(self):
        parser = argparse.ArgumentParser(description="Directory finder")
        parser.add_argument("-u", "--url", required=True, help="Base URL")
        parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist")
        options = parser.parse_args()

        print(options.url)
        print(options.wordlist)
        if options.url is None or options.wordlist is None:
            print("[-] Please specify url or wordlist to start!")
            print(parser.usage)
            sys.exit()
        url = options.url
        wordlist = options.wordlist
        if not os.path.exists(wordlist):
            print("[-] The wordlist does not exist!")
            sys.exit()
        if not url.startswith('http://') and not url.startswith('https://'):
            url ='http://' + url
        if not url.endswith('/'):
            url = url + '/'
        return url, wordlist


    def check_page(self, url):
        try:
            response = requests.get(url)
            response_code = response.status_code
            response_size = len(response.content)
            if response_code == 200:
                print(termcolor.colored(f'+ {url} (CODE: {response_code} SIZE: {response_size})', 'blue'))
            elif response_code == 404:
                pass
            else:
                print(f'+ {url} (CODE: {response_code} SIZE: {response_size})')
        except:
            pass

    def run(self):
        with open(self.wordlist, 'r') as f:
            for word in f.readlines():
                url = self.url_base + word.strip()
                #print(url)
                self.check_page(url)

if __name__ == '__main__':
    dirb = MyDirb()
    dirb.run()
