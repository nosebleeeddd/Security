#!/usr/bin/python3

import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin
"""
Inspect page > Network > Make request > GET > Headers

security=low; PHPSESSID=febfed64c516a6570ee9ef43e218ad2e
"""




def convert_cookie(cookie_str):
    cookie_dict = {}
    if ';' in cookie_str:
        for each in cookie_str.split(";"):
            cookie_dict[each.split("=")[0]] = each.split("=")[1]
    else:
        cookie_dict[cookie_str.split('=')[0]] = cookie_str.split("=")[1]
    return cookie_dict



def retrieve_code(url, cookie_str):
    if cookie_str:
        response = requests.get(url, cookies=convert_cookie(cookie_str))
    else:
        response = requests.get(url)
    if response.status_code == 200:
        return response.text




def main(url, cookie_str):
    response = retrieve_code(url, cookie_str)
    html = BeautifulSoup(response, 'html.parser')
    script_tags = html.find_all('script')
    if script_tags:
        for script in script_tags:
            link = urljoin(url, script.get('src'))
            script_source = retrieve_code(link, cookie_str)
            print(script_source)
        else:
            print("[-] No script is found in the page")



if __name__ == "__main__":
    try:
        url = sys.argv[1]
        if len(sys.argv) > 2:
            cookie_str = sys.argv[2]
        else:
            cookie_str = None
        main(url, cookie_str)

    except IndexError:
        print("[-] Usage: %s <url> <cookie values>" % sys.argv[0])
        print("[-] Example: %s http://192.168.155.1/dvwa xxxxxxx" % sys.argv[0])
        sys.exit()

