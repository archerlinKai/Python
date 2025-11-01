# 字串格式化f-string
name = "Archer"
age = 11
print(f"我叫{name},今年{age}歲")
# 只要在字串的前面加上f,就可以在字串當中直接用{}大括號
# 把變數或運算式包起來,程式會自動幫你轉換成字串並且放到該位置
# 就會形成新的字串
# 這叫f-string


# 函式max
# 函式是由名稱,括號組成
# 括號裡可以放參數(材料),每個參數都要用,間隔
# 函式max會提供參數中最大的值
print(max(10, 20, 30, 5, 15))  # 30

# 函式len
# 函式len會提供參數(字串)的長度(字數)
print(len("Hello Apple"))  # 空格也算一個字元 11

# 函式type
# 函式type會提供參數的型態
print(type(123))
print(type("Hello"))
print(type(3.14))
print(type(True))
print(type(False))

# 函式int
# 函式int會把參數轉換成整數型態
print(int(3.14))
print(int("456"))
# print(int("Hello")) #錯誤,無法轉換成整數

# 函式float
# 函式float會把參數轉換成浮點數型態
print(float(123))
print(float("3.14"))
# print(float("Hello")) #錯誤,無法轉換成浮點數

# 函式bool
# 函式bool會把參數轉換成布林值型態
print(bool(1))  # True
print(bool(0))  # False
print(bool("Hello"))  # True
print(bool(""))  # False

# 函式str
# 函式str會把參數轉換成字串型態
print(str(123))
print(str(3.14))
print(str(True))
print(str(False))
print(str([1, 2, 3]))

# 函式input
# 函式input會讓程式暫停並等待使用者輸入資料
name = input("請輸入你的名字: ")  # 等待使用者輸入名字()後面的不算name
# print(type(name))  # input輸入的資料型態都是字串
print(f"你好{name}!")
age = input("請輸入你的年齡: ")  # 等待使用者輸入年齡()後面的不算age
age = int(age)  # 把輸入的年齡轉換成整數
print(f"明年你就{age+1}歲了!")

# 圓形面積
半徑 = float(input("請輸入圓形半徑"))
面積 = 3.14 * 半徑 * 半徑
print(f"圓形面積為{面積}")
