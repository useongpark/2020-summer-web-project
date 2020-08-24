import os
import requests
from bs4 import BeautifulSoup

os.system("clear")

URL = "https://www.iban.com/currency-codes"
result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser') #html source 가져오는거
tbody = soup.find("tbody")
trs = tbody.find_all('tr') #trs 다 가져오려고 'all'

countries = []
currencies = []
codes = []
numbers = []

for tr in trs:  #각각의 리스트를 가져오려고 .append 씀
  if tr.find_next('td').find_next('td').string != "No universal currency": # != 같지 않음
    countries.append(tr.find_next('td').string
    currencies.append(tr.find_next('td').find_next('td').sting)
    codes.append(tr.find_next('td').find_next('td').find_next('td').sting)
    numbers.append(tr.find_next('td').find_next('td').find_next('td').find_next('td').sting)

for index, country in enumerate(trs): #반복문 사용시 몇 번째 반복문인지 확인 할때 enumerate
  print("Number: {}, Country: {}".format(index, country))

max_num = len(countries)

def run_program():
  user_input = input("Enter a number to find currency: ")
  try: 
    if int(user_input) >= 0 and int(user_input) < max_num:
      print("You typed: " + user_input)
    else:
      print("Type a number between the index. ")
      return run_program()
except:
  print("Please type a number. ")
  return run_program()

run_program()