#주어진 문자열이 팰린드롬인지 확인

#(regular expression의 약어) 정규표현식
import re

s = "A man, a plan, a canal: Panama"

#소문자로 바꿈
s = s.lower()

#문자, 숫자 제외 제거하기
s = re.sub('[^a-z0-9]','',s)

#문자열 뒤집어서 확인
print(s == s[::-1])

#''.join(reversed(s))를 사용해서 뒤집는 것보다 문자열 슬라이싱을 사용하는게 속도가 더빠름

