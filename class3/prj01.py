# try except錯誤處理
# 當程式遇到錯誤時 可以不用停住程式 而是用expect的東西
# 使用:或tab分隔區塊
try:
    n = int(input("請輸入數字: "))
    print(f"你輸入的數字是{n}")
except:
    print("看不懂喔")
try:
    n = int(input("請輸入數字: "))
    print(f"你輸入的數字是{n}")
except ValueError:  # 指定錯誤類型
    print("看不懂喔")
except ZeroDivisionError:  # 用變數e來接錯誤訊息
    print("發生錯誤")
except:
    print("發生不明錯誤")
else:  # 沒有錯誤時會執行else區塊 不一定要用
    print("沒有錯誤喔")
finally:  # 不管有沒有錯誤都會執行finally區塊 不一定要用
    print("程式結束")

# 比較運算子
print(5 == 5)  # True 5等於5
print(5 != 3)  # True 5不等於3
print(5 > 3)  # True 5大於3
print(3 < 5)  # True 3小於5
print(5 >= 5)  # True 5大於等於5
print(3 <= 5)  # True 3小於等於5

# 邏輯運算子
# and 代表全部條件都要成立才會回傳True
print(True and False)  # False, False或True
print(True and True)  # True, True和True

# or 代表只要有一個條件成立就會回傳True
print(False or True)  # True, False或True
print(False or False)  # False, False或False

# not 代表將原本的布林相反
print(not True)  # False, 非True
print(not False)  # True, 非False

# 優先順序
# 1. 括號
# 2. 算術運算子 1+2 3-4 5*6 7/8 9//2 10%3 11**2
# 3. 比較運算子 1==2 2!=3 3>2 4<5 5>=5 6<=7
# 4. 邏輯運算子 1 not 2 and 3 or


# if 條件判斷
# if 判斷條件是否成立 如果成立就執行縮排區塊
# 可以有多的elif 代表其他條件
# 可以有一個else 代表以上條件都不成立
pwd = input("請輸入密碼: ")
if pwd == "0824":
    print("歡迎笨蛋回來")
elif pwd == "1031":
    print("歡迎天才回來")
elif pwd == "0709":
    print("歡迎80公斤的人回來")
elif pwd == "0827":
    print("歡迎惡魔回來")
else:
    print("密碼錯誤")
# if elif else 使用時機
# 1.需要多重條件判斷時使用if elif else
# 2.需要兩個條件判斷時使用if else
# 3.只有一個條件判斷時使用if
