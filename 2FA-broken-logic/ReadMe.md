# 2FA broken logic

## Lab description
In this lab, the application add a new layer of protection against brute-forcing and enumerating, as it requires to enter 4 digits verification code, sent via user's mail.

## Security flaw
The client is one who is initiating the second requrest for verification not the server with the previously entered username and the password, so it requires to send something that will identify the user that should be verified, and this is done by a cookie called ```verify``` and it's value is the username we want to verify.

## Solution
After we login with valid credintials, We can intercept this verification step, and modify the ```verify``` cookie with the username we are interested in ```carlos```, so we now are sure that this username has now a verification code waiting to be verified, then we could intercept the request of sending this code, and make our brute-forcing attack, as it's only 4 digits.

## Hints
* You could make some requests with the valid username to know the pattern of the 4-digit code
* i used multi-threading as the requests take time
