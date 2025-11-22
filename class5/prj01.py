import turtle as t  # 匯入 turtle 模組並以 t 作為別名

t.pensize(5)  # 設定畫筆寬度為 5
t.color("blue")  # 設定筆色為藍色
t.fillcolor("blue")  # 設定填充顏色為藍色
t.begin_fill()  # 開始填色

for i in range(5):  # 迴圈 5 次以畫出五角星
    t.forward(200)  # 往前移動 200 單位
    t.right(144)  # 向右轉 144 度

t.end_fill()  # 結束填色
t.done()  # 停留視窗不關閉


# 列印九九乘法表（1 到 9）
for i in range(1, 10):  # 被乘數 1~9
    for s in range(1, 10):  # 乘數 1~9
        print(f"{i}*{s}={i*s}")  # 格式化輸出乘法結果
