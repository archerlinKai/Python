weather = [
    "晴天",
    "陰天",
    "雨天",
    "多雲",
    "雷陣雨",
    "颱風",
    "大晴天",
]  # 初始化一週天氣列表

print("目前一週天氣預報：")  # 列出目前一週天氣
print(weather)

while True:  # 讓使用者輸入要修改的星期（重覆直到合法）
    try:
        day = int(input("請輸入要修改的星期數字(1~7): "))  # 讀取數字並轉為整數
    except ValueError:
        print("請輸入數字編號")
        continue

    if day < 1 or day > 7:
        print("輸入錯誤，沒有此星期，請重新輸入")  # 檢查輸入範圍
        continue
    else:
        break

print(f"您要修改的星期是 {day}")  # 顯示使用者選擇的星期
print(f"原本的天氣是 {weather[day - 1]}")  # 顯示該星期原本的天氣

new_weather = input("請輸入新的天氣: ")  # 讀取使用者輸入的新天氣
weather[day - 1] = new_weather  # 更新列表中對應星期的天氣

print(f"修改後的天氣是 {new_weather}")  # 顯示修改後結果
print(weather)  # 顯示整週更新後的天氣
