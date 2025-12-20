# append可以在已經存在的list當中加入新的資料
# 可以在程式執行的過程當中將資料加入道已存在的list的"最後面"
L = ["Hello", "World"]
L.append("phyton")
print(L)  # 印出['Hello', 'World', 'phyton']
# 使用insert可以在list的指定位置插入新的資料
# 記得list的index是從0開始算起的
# 如果新增的位置超過list的長度,會直接到最後面
# 如果新增的位置是負數,會從list的最後面開始算起
L = ["Hello", "World"]
L.insert(1, "Python")
print(L)  # 印出['Hello', 'Python', 'World']
L.insert(-1, "java")
print(L)  # 印出['Hello', 'Python', 'java', 'World']
L.insert(10, "C++")
print(L)  # 印出['Hello', 'Python', 'java', 'World', 'C++']

# remove:移除中指定的元素
# 電腦會從左側到右第一個符合元素並移除,指移除一次
L = ["Hello", "Python", "java", "World", "Python"]
L.remove("Python")
print(L)  # 印出['Hello', 'java', 'World', 'Python']
# pop:移除指定位置的元素,並回傳該元素
L = ["Hello", "Python", "java", "World"]
# 不給索引時,pop()會移除最後一個元素
L.pop()
print(L)  # 印出['Hello', 'Python', 'java']
s = L.pop(1)  # 移除索引1的元素,並回傳該元素
print(L)  # 印出['Hello', 'java']
print(s)  # 印出Python
# 如果輸入的index超過範圍,會產生錯誤
# 負數索引也可以使用
L = ["Hello", "Python", "java", "World"]
s = L.pop(-2)  # 移除索引-2的元素,並回傳該元素
print(L)  # 印出['Hello', 'Python', 'World']


# emumerate:同時取得元素的索引和值
L = ["Hello", "Python", "java", "World"]
for index, value in enumerate(L):
    print(f"索引:{index}, 值:{value}")
# 印出:
# 索引:0, 值:Hello

# in 可以用在很多地方,像是If判斷式
# 可以用來檢查某個元素是否在list當中
L = ["Hello", "Python", "java", "World"]
if "Python" in L:
    print("有找到Python")
else:
    print("沒有找到Python")

# in 也可以用在for迴圈當中
# 可以用來依序取得list當中的每一個元素
L = ["Hello", "Python", "java", "World"]
for item in L:
    print(item)

# in還可以用在字串當中,檢查某個字串是否再自川當中
s = "Hello Python World"
if "Python" in s:
    print("有找到Python")
