# index:尋找指定元素在List中第一次出現的位置
# 如果元素不存在,會產生錯誤
L = [1, 2, 3, 4, 5, 3]
print(L.index(3))  # 印出 2，3 在索引位置 2]

# count:計算指定元素在List中出現的次數
print(L.count(3))  # 印出 2，3 在 List 中出現了兩次#

# sort:將 List 中的元素進行排序，預設為由小到大
L = [5, 2, 9, 1, 5, 6]
L.sort()
print(L)  # 印出 [1, 2, 5, 5, 6, 9]

# sort(reverse=True):將 List 中的元素進行排序，從大到小
L = [5, 2, 9, 1, 5, 6]
L.sort(reverse=True)
print(L)  # 印出 [9, 6, 5, 5, 2, 1]

# reverse:將 List 中的元素順序反轉
L = [2, 6, 3, 8, 5]
L.reverse()
print(L)  # 印出 [5, 8, 3, 6, 2]

# List 和字串有很相似的操作方式
# 我們可以像操作字串一樣

# 合併兩個List:使用+運算子江兩個list合併成一個新的list
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2
print(L3)  # 印出 [1, 2, 3, 4, 5, 6]

# 重複List:使用*運算子將List重複指定次數
L = [1, 2, 3]
L2 = L * 3
print(L2)  # 印出 [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 不同資料型態之間的轉換技巧
print(range(5))  # 印出 range(0, 5)
print(list(range(5)))  # 印出 [0, 1, 2, 3, 4]
print(list("hello"))  # 印出 ['h', 'e', 'l', 'l', 'o']

# split():將字串依指定分隔符號切割成List
s = "Hello World"
L = s.split(" ")
print(L)  # 印出 ['Hello', 'World']
calendars = "2024-06-15"
L = calendars.split("-")
print(L)  # 印出 ['2024', '06', '15']

# join():將List中的元素使用指定的連接符號合併成一個字串
L = ["Hello", "World", "Python"]
s = " ".join(L)
print(s)  # 印出 Hello World Python
