# 質數
i = int(input("請輸入一個正整數: "))
if i > 1:
    for n in range(2, i):
        if i % n == 0:
            print(f"{i}不是質數")
            break
    else:
        print(f"{i}是質數")
