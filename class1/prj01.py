# 這是一般註解
print("Hello World")  # 這是程式碼後的註解
# print("Hello World")ctrl+? 這是註解的快捷鍵
"""
這
是
多
行
註
解
"""


# 基本型態
print(123)  # 0123456789整數,integer,int
print(3.14)  # 123.0 5.3浮點數,float,float
print("Hello")  # ""字串,string,str
print(True)  # True/False 布林值,boolean,bool


# 變數,Variable,var
# 變數是存放資料的空間,每個變數都要有自己的名稱
# 存啥都可以,但不能存有空格的名稱
# 命名規則:只能用英文字母,數字,底線組合而成,且不能以數字開頭
a = 10  # =的功能是把(右邊的資料)存到左邊的變數
b = 20
c = a + b
print(c)


# 算術運算子
print(a + b)  # 加法
print(a - b)  # 減法
print(a * b)  # 乘法
print(a / b)  # 小數除法
print(a // b)  # 整除除法
print(a % b)  # 取餘數
print(a**b)  # 次方


# 運算子優先順序
# 1. 括號()
# 2. 次方**
# 3. +,- 正負號
# 4. *乘法 /小數除法 //整除除法 %取餘數
# 5. +加法 -減法


# 字串運算
print("Hello" + "World")  # 字串串接
print("Hello" * 3)  # 字串重複
# print("Hello"+3) #錯誤,字串無法加整數
# 除了字串乘法可以跟數字相乘外,其他運算都不行(不同型態之間無法運算)
# 字串跟字串之間只能做加法
