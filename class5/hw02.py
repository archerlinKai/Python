# 秒針
import time as t
import turtle as tr

tr.speed(0)  # 設定畫筆速度為最快
tr.forward(100)  # 向前移動100單位
tr.hideturtle()  # 隱藏畫筆箭頭

for i in range(60):  # 重複60次
    tr.clear()  # 清除畫面
    tr.right(6)  # 向右轉6度
    tr.stamp()  # 蓋印章
    t.sleep(1)  # 暫停1秒鐘
    tr.home()  # 回到原點
tr.done()  # 不要關閉視窗
