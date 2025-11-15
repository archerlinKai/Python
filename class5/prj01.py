import turtle as t  # 匯入模組turtle並命名為t

t.pensize(5)  # 設定畫筆粗細為5
t.color("blue")  # 設定顏色為藍色
t.fillcolor("blue")  # 設定填充顏色為藍色
t.begin_fill()  # 開始填充顏色

for i in range(5):  # 重複5次
    t.forward(200)  # 向前移動200單位
    t.right(144)  # 向右轉144度

t.end_fill()  # 結束填充顏色
t.done()  # 不要關閉視窗


# 九九乘法表
for i in range(1, 10):
    for s in range(1, 10):
        print(f"{i}*{s}={i*s}")
