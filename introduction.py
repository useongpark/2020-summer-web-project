# 기초 문법

a = 0.47
print(type(a))
#float #실수

b = 46
print(type(b))
#int #정수

c = "박우성"
print(type(c))
#str #문자

d = True
print(type(d))
#bool #참과 거짓

e = ["Mon", "Tue", "Wed"]
print(type(e))
#list
#list = mutable = 변할 수 있는 

print(e[0])

f = ("Mon", "Tue", "Wed")
print(type(f))
#tuple
#tuple = immutable ()=만 사용

print(e[0])

weekday = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
week = [] #대괄호
week.append(weekday)
print(week)
week.append(weekend)
print(week)
week.remove(weekend)   
print(week)

######
'''
[] = list - 안의 있는 요소들 수정 가능
{} = dict #dictionary (key, value) 단어, 정의
() = tuple - 안의 있는 요소들 수정 불가능

소문자로만 하고 싶을 땐 .lower()
대문자로만 하고 싶을 땐 .upper()

.split() -> 특정 문자로 요소를 나누고 싶을 때 
.strip() -> 양 끝의 공백을 없애고 싶을 때 
.append() -> 추가 
'''
#####

#####
'''
for 문
for 변수 in 리스트
    수행할 문장 1 #tap 필수
    수행할 문장 2
'''
#example 
days = [" Mon ", " Tue ", " Wed ", " Thu ", " Fri "]
print(days)

for day in days:
    print(day) #공백 있이 출력
    print(day.strip()) #공백없이 출력
    days.append("Sat") #("Sat", "Sun") X
    days.append("Sun")
    print(days) #Sat, Sun 추가됨
#####
'''
for in range 함수

range(10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9 

range(start, stop)
range(1,10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9

range(start, stop, step)
range(0, 20, 2) -> 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
'''
#####

#####
'''
def 함수 #def = definition
def 함수이름(매개변수):
    수행할 문장 1
    수행할 문장 2
'''
#example
def abc(a, b, c, d):
    return (a + b + c + d) #보통 print 대신 return 씀

def park(a, b):
    return (a - b)

print(park(3, abs(2 + 4 + 5 + 5)))
# -13
#####

#####
'''
조건문 - if 문 and swich 문
if 문
'''
#example
user_input = input("Enter you age: ") #이름엔 띄어쓰기 대신 _(언더바)
print(user_input) #age는 터미널에 입력

def check_soju(age):
    if age > 21:
        return("You can drint soju")
    elif age == 20 or age == 21:  # elif -> Python  , else if -> Java 
        return("You are new to drink soju")
    else: 
        return("You cannot drink soju")

print(check_soju(user_input))
#####

##### example
# how many credit you take? # if player say no then stop
def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()

def main():
  credit = int(input("TYPE HOW MANY CREDITS YOU TAKE: "))
  if credit < 20:
    print("You are freshman")
  elif credit >= 20 and credit < 40:
    print("You are sophomore")
  elif credit >= 40 and credit < 60:
    print("You are junior")
  else:
    print("You are senior")
  restart()

main()
#####

#####
def add_byuh_class(dictionary={}, course="", description=""):
    dictionary[course] = description

byuh_class = {
    #key      #value
    "MUSC 101" : "Introduction of Music",
    "CIS 101" : "Inctro to CS"
}
print(byuh_class)
print(byuh_class["CIS 101"])

add_byuh_class(byuh_class, "MATH 121", "Principle of Statistic")

print(byuh_class)
#####



#####
#example
def delete_exercise(type={}, name=""):
    del type[name]

types_of_exercise = {
#tab 
    "lat pull down" : "back",
    "bench press" : "chest",
    "push up" : "back"
}

print(type(types_of_exercise))
print(types_of_exercise)

delete_exercise(types_of_exercise, "lat pull down")
print(types_of_exercise)

for type_of_exercise in types_of_exercise:
    print(type_of_exercise)
#####



#####
#example
animals = input("Enter animal: ").split(",")
print(animals)
stripped_animals = []
for animal in animals:                       #항목별로 공백을 없애고 싶어서 for 문 삽입
    stripped_animals.append(animal.strip())  #추가하기 때문에 .append
print(stripped_animals)

#Dog, Cat, Pig  
#####




























