# 飲料點餐示範
# 使用清單儲存選項，並用 while 迴圈重複顯示選單直到使用者選擇離開
juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]  # 選單項目

# 顯示初始選單（可省略，迴圈內也會顯示）
for index in range(len(juice_list)):
    print(f"{index + 1}. {juice_list[index]}")

# 進入互動式選單
while True:
    # 顯示所有選項
    for index in range(len(juice_list)):
        print(f"{index + 1}. {juice_list[index]}")

    # 讀取使用者輸入（轉為整數以便比較）
    try:
        choice = int(input("請選擇飲料編號: "))
    except ValueError:
        print("輸入錯誤，請輸入數字編號")
        continue

    # 檢查輸入是否在合法範圍
    if choice < 1 or choice > len(juice_list):
        print("選擇錯誤，請重新選擇")
        continue

    # 若選到最後一個選項，結束程式
    if choice == len(juice_list):
        print("系統關閉，謝謝使用")
        break

    # 正常回應使用者選擇的飲料
    print(f"您選擇的飲料是 {juice_list[choice - 1]}")
