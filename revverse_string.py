# 344. Reverse String

# 내 풀이 reverse()안쓰고 풀어보기
s = ["h", "e", "l", "l", "o"]

for idx, ele in enumerate(s[:int(len(s) / 2)]):
    s[idx], s[len(s) - 1 - idx] = s[len(s) - 1 - idx], s[idx]

#reverse() 속도가 더 빠름
s2 = ["h", "e", "l", "l", "o"]
s2.reverse()
print(s)

#풀이방법2
s[:] = s[::-1]