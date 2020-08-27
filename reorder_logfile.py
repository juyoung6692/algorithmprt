#937. reorder log files
logs = ["dig1 8 1 5 1","let3 art zero","dig2 3 6","let2 own kit dig","let1 art zero"]

digits, letters = [], []

for log in logs:
    if(log.split()[1].isdigit()):
        digits.append(log)
    else:
        letters.append(log)

letters.sort(key=lambda x: (x.split()[:1], x.split()[0]))

print(letters+digits)


#isdigit() 숫자면 True
