import random as r

a = r.randrange(1, 101)  # 只產生一個答案

while True:
    b = int(input("請輸入1~100的整數: "))

    if a == b:
        print("恭喜你答對了!")
        break
    elif a > b:
        print("你猜的數字太小了")
    else:
        print("你猜的數字太大了")
