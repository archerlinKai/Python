juice_list = ["蘋果汁", "柳橙汁", "葡萄汁", "系統關閉"]

for index in range(len(juice_list)):
    print(f"{index + 1}. {juice_list[index]}")
choice = int(input("請選擇飲料編號: "))

while True:
    for index in range(len(juice_list)):
        print(f"{index + 1}. {juice_list[index]}")
    choice = int(input("請選擇飲料編號: "))
    if choice < 1 or choice > len(juice_list):
        print("選擇錯誤，請重新選擇")
        continue
    if choice == len(juice_list):
        print("系統關閉，謝謝使用")
        break
    print(f"您選擇的飲料是 {juice_list[choice - 1]}")
