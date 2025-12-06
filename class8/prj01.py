# random 模組匯入
import random as r

# random.randrange 與 range 的用法相同，不包含最後一個數字
# 不同的是 randrange 隨機取得一個數字，range 是產生一組數字
print(r.randrange(10))  # 隨機取得 0~9 之間的整數
print(r.randrange(1, 10))  # 隨機取得 1~9 之間的整數
print(r.randrange(1, 10, 2))  # 隨機取得 1,3,5,7,9 之間的奇數

# random.randint(a, b) 取得 a~b 之間的整數，包含 a 和 b
# 與 randrange 不同，randint 不能設定間隔步數
print(r.randint(1, 10))  # 隨機取得 1~10 之間的整數


# List（清單）示範
# List 可以存多筆資料，每筆資料用 , 隔開，並以 [] 包起來
# List 可以存不同型態的資料
L = [1, 2, 3, 4, 5]
print(L)

# List 中存不同型態的資料
L = [1, "hello", 3.14, True]
print(L)

# List 的取值（索引與切片）
# 取值方式與 range 相同，也不包含結束位置
print(L[0])  # 取第一個元素（索引 0）
print(L[1:3])  # 取索引 1 到 2 的元素
print(L[:3])  # 取索引 0 到 2 的元素
print(L[2:])  # 取索引 2 到最後的元素
print(L[:])  # 取全部元素

# 使用 len() 取得 List 的長度
L = [1, 2, 3, 4, 5]
print(len(L))  # 印出 L 裡面有幾個元素

# 方法 1：用 len() 搭配 range() 取得索引值進而存取元素
for i in range(len(L)):
    print(L[i])  # 利用索引值取出每個元素

# 方法 2：直接用 for 迴圈遍歷 List 中的每個元素
for i in L:
    print(i)

# 選擇哪一種方式取出 List 中的元素，看需求而定
