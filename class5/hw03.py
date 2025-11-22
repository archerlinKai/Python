n = int(input("請輸入正整數: "))  # 讀取使用者輸入的正整數

for i in range(1, n + 1):  # 迴圈從 1 到 n
    # 若 i 可被 3 或 7 整除，則印出該數字
    if i % 3 == 0 or i % 7 == 0:
        print(i)
