shopping_list = []

while True:
    print("\n目前購物清單：", shopping_list)
    print("========== 功能選單 ==========")
    print("1. 新增東西")
    print("2. 修改東西")
    print("3. 刪除東西")
    print("4. 離開程式")
    print("==============================")

    choice = input("請輸入功能編號：")

    # ① 新增東西（兩種方式）
    if choice == "1":
        print("\n新增方式：")
        print("1. 加到最後（append）")
        print("2. 插入指定位置（insert）")
        add_choice = input("請選擇新增方式：")

        item = input("請輸入要新增的東西：")

        if add_choice == "1":
            shopping_list.append(item)

        elif add_choice == "2":
            index = int(input("請輸入插入的位置（從 0 開始）："))
            shopping_list.insert(index, item)

        else:
            print("新增方式輸入錯誤！")

    # ② 修改東西
    elif choice == "2":
        index = int(input("請輸入要修改的編號（從 0 開始）："))
        new_item = input("請輸入新的東西名稱：")
        shopping_list[index] = new_item

    # ③ 刪除東西（兩種方式）
    elif choice == "3":
        print("\n刪除方式：")
        print("1. 用名稱刪除（remove）")
        print("2. 用位置刪除（pop）")
        del_choice = input("請選擇刪除方式：")

        if del_choice == "1":
            item = input("請輸入要刪除的東西名稱：")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("清單裡沒有這個東西喔！")

        elif del_choice == "2":
            index = int(input("請輸入要刪除的位置（從 0 開始）："))
            shopping_list.pop(index)

        else:
            print("刪除方式輸入錯誤！")

    # ④ 離開程式
    elif choice == "4":
        print("不想逛了就回家！👋")
        break

    else:
        print("請輸入正確的功能編號！")
