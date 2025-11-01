try:
    n = float(input("請輸入華氏溫度: "))
    攝氏 = (n - 32) * 5 / 9
    print(f"攝氏溫度為{攝氏}")
except:
    print("輸入錯誤!")
