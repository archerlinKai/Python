# 螺旋狀圖形
import turtle as t  # 匯入模組turtle並命名為t

for i in range(15):

    t.shape("circle")
    t.forward(10)
    t.stamp()
    t.right(8)
for i in range(15):

    t.forward(20)
    t.stamp()
    t.right(10)
for i in range(15):

    t.forward(30)
    t.stamp()
    t.right(12)
for i in range(15):

    t.forward(40)
    t.stamp()
    t.right(14)
for i in range(15):

    t.forward(50)
    t.stamp()
    t.right(16)
for i in range(15):

    t.forward(60)
    t.stamp()
    t.right(18)
t.done()  # 不要關閉視窗
