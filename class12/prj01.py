水果價格 = {"蘋果": 30, "香蕉": 20, "橘子": 25}
print(水果價格)

while True:
    print("1. 新增水果價格")
    print("2. 修改水果價格")
    print("3. 刪除水果")
    print("4. 離開程式")

    choice = input("請輸入功能編號：")

    if choice == "1":
        item = input("請輸入要新增的水果：")
        coin = input("請輸入水果價格：")
        水果價格[item] = int(coin)
        print("新增完成")

    elif choice == "2":
        item = input("請輸入要修改的水果：")
        if item in 水果價格:
            coin = input("請輸入新的水果價格：")
            水果價格[item] = int(coin)
            print("修改完成")
        else:
            print("沒有這個水果喔")

    elif choice == "3":
        item = input("請輸入要刪除的水果：")
        if item in 水果價格:
            del 水果價格[item]
            print("刪除完成")
        else:
            print("沒有這個水果喔")

    elif choice == "4":
        print("程式結束")
        break

    else:
        print("請輸入正確的編號")

    print("目前水果價格：", 水果價格)
