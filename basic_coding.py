# 기본 코딩 문법

# import this
import sys

# 기본 인코딩
print(sys.stdin.encoding) # utf-8
print(sys.stdout.encoding) # utf-8

# 출력문
print("My name is Useong Park")

# 변수 선언
myName = "Useong"

# 조건문
if myName == "Useong": 
    print('Ok')   # 조건 = myName이 "Useong"이면 Ok를 출력해라

# 반복문 (구구단 출력)
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i, j), i*j)

# indent = Tab = Space*4

# 함수 선언
def greeting():
    print("Hello !")

greeting()

# 클래스 (1)
class Cookie:
    pass

# 객체생성 (2)
cookie = Cookie()

print(id(cookie))
print(dir(cookie))




# python data type (데이터타입)
'''
Boolean:  참과 거짓 1 = True, 0 = False
Numbers:
String: 문자열
Bytes: 
Lists:
Tuples:
Sets:
Dictionaries:
'''

v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3 # 실수
v_int = 4 # 정수
v_ditt = {
    "name" : "Park",
    "age" : 22
}
v_list = [3, 5, 7]
v_tuple = (3, 5, 7)
v_set = {7, 8, 9} # 집합

# print(type()) # 함수이름 대입


# 숫자형 및 연산자
'''
+ : 더하기
- : 빼기
* : 곱하기
/ : 나누기
// : 나누기(몫)
% : 나누기(나머지)
** : 제곱
'''



# 형변환    int <-> float <-> complex
# int, float, complex(복소수)

a = 5. #float
b = 3  #int
result = a + b

print(result) # 8.0 -> float

print(int(result)) # 8 -> int
print(complex(result)) #(8+0j) -> complex

y = 100
y += 100 # y = y + 100
print(y)




# 수치 연산 함수
# https://docs.python.org/3/library/math.html -> 파이썬의 모든 함수가 나와있음

print(abs(-7)) # abs = 절댓값을 나타내주는 함수
n, m = divmod(100, 8) # divmod: 100을 8로 나눠서 몫은 n으로 나머지는 m으로 나타내준다.
print(n, m) # 12 4

import math # 수학관련 패키지를 사용할 수 있는 모듈 가져오기 # 코드의 맨 위에 나타내 주는게 정석

print(math.ceil(5.1)) # ceil: 5.1 보다 크면서 가장 작은 정수를 나타내준다. # 6
print(math.floor(3.874)) # floor: 3.874 보다 가장 가까우면서 작은 함수를 나타내준다. # 3





# 문자열, 문자열연산, 슬라이싱
# 문자열의 길이 구하는 방법 = len -> 공백도 한공간으로 침

str1 = "I am a boy"
str2 = "Who are you?"
str3 = '' # 1
str4 = str('a') # 1

print(len(str1)) # 10

escape_str1 = "DO you have \"big company\"" # DO you have "big company"
print(escape_str1)
escape_str2 = "Tab \t Tab \t Tab" # Tab      Tab     Tab -> tab이 적용되서 나옴
print(escape_str2)





# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1) # C:\Programs\Test\Bin -> 그대로 출력
raw_s2 = r"\aa\\aa\a"
print(raw_s2) # \aa\\aa\a -> 그대로 출력



# Multi-Line Statements \ -> 줄을 계속 사용할 수 있음
multi = "이대로 출력하고 싶다" 
print(multi)




# 문자열 함수
# http://www.w3schools.com/python/python_ref_string_.asp

a = "niceman"
b = "orange"

print(a.islower()) # a는 소문자로만 되어있다. # True
print(a.capitalize()) # a의 앞글자를 대문자로 바꿔준다.
print(b.endswith('s')) # b의 끝문자가 s이다. # False
print(a.replace("nice", "good")) # 바꿔주는 함수
print(list(reversed(b))) # ['e', 'g', 'n', 'a', 'r', 'o']


# silcing
# 정방향은 0부터 시작
print(a[0:3]) # nic
print(a[0:4]) # nice
print(a[:4]) # nice 앞에 것과 같다 
print(a[:]) # niceman 전체 다 나옴
print(a[0:len(a)-1]) # nicema # -> -1 했기 때문에 n이 나오지 않는다
print(b[0:4:2]) # oa
print(b[1:-2]) # ran
print(b[::-1]) # egnaro 거꾸로 출력



# list, tuple
# list [순서o, 중복o, 수정o, 삭제o]
a = list()
a = []
b = [1, 10, 'pen', 'banana']
c = [10, 100, ['pen'], ['banana']]

# indexing
print(c[3]) # ['banana']
print(c[-1]) # ['banana']
print(c[0]+c[1]) # 110
print(c[2][-1]) # []가 2개 있기 때문

# silcing
print(b[0:2]) # [1, 10]
print(c[2][:1])

# 연산
print(b+c) # [1, 10, 'pen', 'banana', 10, 100, ['pen'], ['banana']]
print(str(b)+"hi") # [1, 10, 'pen', 'banana']hi

# list 함수
a = [1,8,3,9,5]

a.append(2) # 끝의 항에 추가
print(a)
a.sort() # 숫자배열 정렬
print(a)
a.reverse()
print(a)
a.insert(2, 7) # 삽입 -> 2번 index에 숫자 7 삽입
print(a)
a.remove(3)
print(a)
a.pop() # 맨 마지막 항을 삭제
print(a)
ex = [99,88]
a.extend(ex) # 현재 list 자체에서 추가됨
a.append(ex) # list 자체가 추가됨
print(a)

# 삭제: del, remove, pop

# tuple (순서O, 중복O, 삭제O, 수정O)
# tuple 함수

z = (5,3,6,4,3)

print(3 in z)
print(z.index(3)) # 1번째 index에 있다.
print(z.count(1)) # how many 1 in this tuple




# dictionary, set
# Dictionary(dict): 순서X, 중복X, 수정O, 삭제O

# key, value (Json)

a = {"name": "Park", "phone": "0101-4294-0622", "birth": "990623"}
b = {0: "Hello Python", 1: "Coding"} # 잘 사용하지 않는 형태
c = {"abc": [1,2,3,4,5]}

print(type(a)) # dict

# 출력하는 방법
print(a["name"]) # Park # 직접접근 방법
print(a.get("name")) # Park # 안전하게 조회하는 방법 # 안전하게 코딩하는 방법
print(c["abc"])

# dictionary 추가
a["address"] = "Seoul" 
a["rank"] = [1,2,3,4,5,] # list
a["number"] = (11,22,33,44,55) # tuple
print(a)

# keys, values, items
example = {"age": [1,2,3,4,5]}
# key = "age"
# value = [1,2,3,4,5]
# item = "age": [1,2,3,4,5]

print(a.keys()) # # key만 가져옴
print(list(a.keys())) # ['name', 'phone', 'birth', 'address', 'rank', 'number'] -> ()없이 list 형태로만 가져옴
print(a.values()) # value만 가져옴
print(a.items()) # 전체 다 가져옴

# set(집합): 순서X, 중복X
a = set()
b = set([1,2,3,4])
c = set([1,4,5,6])

print(type(a)) # set

s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8])

print(s1.intersection(s2)) # intersection: 교집합
print(s1 & s2) # 교집합

print(s1.union(s2)) # union: 합집합
print(s1 | s2) # 합집합

print(s1.difference(s2)) # difference: 차집합
print(s1 - s2) # 차집합

s1.add(18) # 추가
s1.remove(5) # 제거
print(s1)

