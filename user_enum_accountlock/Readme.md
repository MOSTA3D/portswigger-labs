# Username enumeration via account locking

## Target
To get authenticated with any account.

## Problem
The Error message doesn't make it clear that if the username or password is wrong, so it will be hard to be authenticated.

## Logic flaw
If you enter a valid username more than 3 times, application will show a different error message.

## Methodology
We will enumerate the username first by brute-forcing with the help of the **usernames** list, and to make 4 requests for every username, if we get the different error message at the forth try, then this username is the valid one.

After getting the username, we will make another brute-forcing to get the password, but now as our username is valid, we have to wait a **minute** after every 3 requests.
