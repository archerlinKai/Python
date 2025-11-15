import turtle as t  # 匯入模組turtle並命名為t

for i in range(8):
    t.penup()  # 提起畫筆,蓋章時不會有線條
    t.stamp()  # 蓋印章
    t.forward(15)
    t.right(45)
    t.home()
t.done()  # 不要關閉視窗
