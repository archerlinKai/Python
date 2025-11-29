# 質數判斷範例
# 讀取使用者輸入的正整數，判斷是否為質數
i = int(input("請輸入一個正整數: "))
if i > 1:  # 1 不是質數，從 2 開始檢查
    for n in range(2, i):  # 檢查是否存在因數
        if i % n == 0:  # 若有可整除的 n，代表不是質數
            print(f"{i}不是質數")
            break  # 找到因數後跳出迴圈
    else:  # for 迴圈未被 break 時會執行 else 區塊
        print(f"{i}是質數")


# for / while 的 else 範例
# 當 for 或 while 迴圈正常結束（未被 break 中斷）時，會執行 else 區塊
# 範例：while 迴圈示範
i = 0
while i < 5:
    print(i)  # 印出目前的 i
    i += 1
else:
    print("迴圈結束")  # 迴圈正常結束時執行

# else 的其他用途：
# - try...except...else：若沒有發生例外，會執行 else 區塊
# - if...elif...else：當前面的條件都不成立時執行 else

# 倒數計時器示範
import time

n = int(input("請輸入倒數秒數: "))  # 讀取倒數秒數
while n > 0:
    print(n)  # 印出剩餘秒數
    time.sleep(1)  # 暫停 1 秒
    print(f"倒數計時:{n}秒")  # 使用 f-string 顯示變數
    n -= 1
else:
    print("時間到")  # 倒數結束

# 迴圈的 break 範例
# break 只會跳出所屬的那一層迴圈，注意縮排與範圍
for i in range(5):
    for j in range(5):
        if j == 3:
            break  # 跳出內層的 for j 迴圈
        print(f"i={i}, j={j}")
# 這裡的 break 只會跳出內層的 for j 迴圈，外層的 for i 仍會繼續


# 跳跳繩示範
# 每 10 次休息一次，並印出每次跳繩的次數
jump = int(input("請輸入跳繩次數: "))  # 讀取跳繩次數
i = 1
while i <= jump:
    if i % 10 == 0:
        print("休息一下")  # 每 10 次提醒休息
    print(f"第{i}次跳繩")  # 印出第幾次跳繩
    i += 1


# continue 範例
# continue 會跳過當前迴圈剩下的敘述，進入下一次迴圈
# 注意在使用 continue 時要確保迴圈變數會被更新，避免無限迴圈
i = 0
while i < 5:
    if i == 2:
        i += 1  # 更新變數以避免無限迴圈
        continue  # 跳過當前迴圈（不印出 2）
    print(i)  # 印出目前的 i
    i += 1
# 這裡的 continue 會跳過當前迴圈當 i 等於 2 時，所以不會印出 2

for i in range(5):
    if i == 3:
        continue  # 跳過當前迴圈（不印出 3）
    print(i)  # 印出目前的 i
# 這裡的 continue 會跳過當前迴圈當 i 等於 3 時，所以不會印出 3
