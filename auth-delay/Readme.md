# Lab: Username enumeration via response timing

This web-app has a defense mechanism against brute-forcing technique, as it block requests more than 3 times for half hour.

## Solution
By using the X-Forwarded-For header, we could pass a false value indicating the origin of the request *false-ip*, so by changin its value before the block, we will be able to pass this block mechanism.
so basically, the code is about passing post requests with the same ```X-Forwarded-For``` value for no more than 3 times, and changing it gradually, so so we can get the username, and the same for the password.
