import turtle as t

for i in range(120):  # 重複120次
    t.shape("turtle")  # 設定圖案為烏龜
    t.forward(20)  # 向前移動20單位
    t.stamp()  # 蓋印章
    t.right(6)  # 向右轉6度
t.done()  # 不要關閉視窗
