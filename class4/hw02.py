# 螺旋狀圖形
import turtle as t  # 匯入模組turtle並命名為t

t.shape("circle")
t.color("red")
t.penup()  # 提起畫筆,蓋章時不會有線
for i in range(15):
    t.stamp()
    t.speed(0)
    t.shape("circle")
    t.forward(10)
    t.right(8)

for i in range(15):
    t.stamp()
    t.speed(0)
    t.forward(20)
    t.right(8)

for i in range(15):
    t.stamp()
    t.speed(0)
    t.forward(30)
    t.right(8)

for i in range(15):
    t.stamp()
    t.speed(0)
    t.forward(40)
    t.right(8)

for i in range(15):
    t.stamp()
    t.speed(0)
    t.forward(50)
    t.right(8)

for i in range(15):
    t.stamp()
    t.speed(0)
    t.forward(60)
    t.right(8)
t.done()  # 不要關閉視窗
