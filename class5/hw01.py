import turtle as t  # 匯入模組turtle並命名為t

t.penup()  # 提起畫筆,蓋章時不會有線條

for i in range(8):
    t.stamp()
    t.forward(15)
    t.home()
    t.right(45)
t.done()  # 不要關閉視窗
