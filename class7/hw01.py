# 質數
n = int(input("請輸入一個正整數: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{i}")
