# python basic quiz

# 1. 아래 문자열의 길이를 구해보시오.
q1 = "qw;oeiuda;l kjsdfn vkoi124921029teugj"
print(len(q1))


# 2. print 함수를 사용해서 아래와 같이 출력해보시오.
# apple;orange;banana;lemon
print("apple;orange;banana;lemon")


# 3. 화면에 *기호 100개를 표시하시오.
a = "*"
print(a*100)


# 4. 문자열 "30" 을 각각 정수형, 실수형, 복수수형, 문자형으로 변환해보시오.
z = "30"
print(float(z))
print(int(z))
print(complex(z))
print(str(z))


# 5. 다음 문자열 "Niceman"에서 "man" 문자열만 추출해보시오.
f = "Niceman"
# replace_all = f.replace("Nice", "")
print(f[4:7])


# 6. 다음 문자열을 거꾸로 출력해보시오. : "Strawberry"
e = "Strawberry"
# print(list(reversed(e)))
print(e[::-1])


# 7. 다음 문자열에서 '-'를 제거 후 출력하시오. : "010-7777-9999"
r = "010-7777-9999"
print(r[0:3]+r[4:8]+r[9:13])
# 정규표현식
import re
print(re.sub('[^0-9]', '', r))


# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하시오. : "http://daum.net"
y = "http://daum.net"

print(y[7:15])


# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보시오. : "NiceMan"
ase = "NiceMan"
print(ase.upper())
print(ase.lower())


# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하시오. : "abcdefghijklmn"
tye = "abcdefghijklmn"

print(tye[2:5])


# 11. 다음 리스트에서 "Apple" 항목만 삭제하시오. : ["Banana", "Apple", "Orange"]
i = ["Banana", "Apple", "Orange"]

i.remove("Apple")
print(i)

# 12. 다음 튜플을 리스트로 변환하시오. : (1,2,3,4)
u = (1,2,3,4)

print(list(u))


# 13. 다음 항목을 dict으로 선언해보시오. : <성인 - 100000 , 청소년 - 70000, 아동 - 30000>

o = {"성인": 100000, "청소년": 70000, "아동": 30000}


# 14. 13번에서 선언한 didctionary(dict) 항목에 <소아 - 0> 항목을 추가해보시오.
o["소아"] = 0


# 15. 13번에서 선언한 dictionary(dict)에서 key 항목만 출력해보시요.
print(o.keys())


# 16. 13번에서 선언한 dictionary(dict)에서 value 항목한 출력해보시오.
print(o.values())
