# 我的超市清單
shopping_list = []

while True:
    print(f"目前購物清單："{shopping_list})
    print("1. 新增  2. 修改  3. 刪除  4. 離開")
    choice = input("請選擇功能：")

    if choice == "1":
        item = input("輸入商品名稱：")
        shopping_list.append(item)

    elif choice == "2":
        if shopping_list:
            num = int(input(f"輸入編號 (1~{len(shopping_list)}):")) - 1
            shopping_list[num] = input("輸入新名稱：")
        elif not shopping_list:
            item = "請輸入商品名稱"
            shopping_list.append(item)

    elif choice == "3":
        if shopping_list:
            num = int(input(f"輸入要刪除的編號 (1~{len(shopping_list)}): ")) - 1
            shopping_list.pop(num)
        else:
            print("清單是空的！")

    elif choice == "4":
        print("掰掰！")
        break

    else:
        print("文盲嗎？請輸入 1~4 之間的數字！")
