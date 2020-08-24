# 숫자 3개 입력 " " 공백으로 숫자를 구분하고 리스트 형식으로 저장
lines = [int(x) for x in input("Enter three lines: ").split()]
# 3 4 5 => [3, 4, 5]
# print(lines)
def checkRAT(lines):
  # lines 리스트에서 max값 = c로 가져오기
  # lines 리스트에서 min값 = a로 가져오기
  # lines 리스트에서 나머지값 = b로 가져오기
  # 피타고라스 정리 이용해서 직각삼각형인지 판별하기
  # a^2 + b^2 = c^2
  a = min(lines)
  lines.remove(a)
  c = max(lines)
  lines.remove(c)
  b = lines[0]
  if a * a + b * b == c * c:
    print("직각삼각형입니다.")
  else:
    print("직각삼각형이 아닙니다.")

# 함수 실행
checkRAT(lines)
