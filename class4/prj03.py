# 匯入模組
import turtle as t

t.forward(100)  # 向前移動 100 單位
t.right(90)  # 向右轉 90 度
t.done()  # 不要關閉視窗

import turtle as t  # 匯入模組turtle並命名為t

t.forward(100)  # 向前移動 100 單位
t.right(90)  # 向右轉 90 度
t.forward(100)  # 向前移動 100 單位
t.right(90)  # 向右轉 90 度
t.forward(100)  # 向前移動 100 單位
t.right(90)  # 向右轉 90 度
t.forward(100)  # 向前移動 100 單位
t.done()  # 不要關閉視窗

"""
for的組成有3個部分
for 迴圈變數 範圍
範圍的部分可以用range()來產生
迴圈變數只能活在for迴圈裏面
迴圈變數每次都會從範圍內取出一個值
"""
for i in range(4):  # 產生一組數字,0到3
    print(i)  # 印出迴圈變數,range=0到3

for i in range(1, 5):  # 產生一組數字,1到4
    print(i)  # 印出迴圈變數,range=1到4
for i in range(1, 10, 2):  # 產生一組數字,1到9,間隔2
    print(i)  # 印出迴圈變數,range=1,3,5,7,9

import turtle as t

for i in range(4):  # 重複4次
    t.forward(100)  # 向前移動100單位
    t.right(90)  # 向右轉90度
t.done()  # 不要關閉視窗

# 蓋印章示範
t.penup()  # 提起畫筆,蓋章時不會有線條
t.color("red")  # 設定顏色為紅色
t.shape("turtle")  # 設定圖案為烏龜
import turtle as t

for i in range(120):  # 重複120次
    t.shape("turtle")  # 設定圖案為烏龜
    t.forward(20)  # 向前移動20單位
    t.stamp()  # 蓋印章
    t.right(6)  # 向右轉6度
t.done()  # 不要關閉視窗
