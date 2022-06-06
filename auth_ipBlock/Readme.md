# Authentication/challenge 3

If you try to submit more than 3 times, the application will suspend your trial for 1 minute, and this depends on our ip, so i tried to use the X\_Forward\_For header and it didn't work, but there is a flaw in the implementation of this way, as if you submit a legal credentials before the your 3 times, your 3 times will be reseted so you can continue bruteforcing.

so the code is simply about brute forcing **carlos** account with the passwords file and before finishing our 3 trials, we will enter valid credintials once, and ofcourse the password is one of this list
