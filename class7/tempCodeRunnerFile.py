# 跳跳繩
jump = int(input("請輸入跳繩次數:"))
i=1
while i <= jump:
    if i % 10 == 0:
        print("休息一下")
        continue
print("第"+str(i)+"次跳繩")