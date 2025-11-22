import turtle as t  # 匯入 turtle 模組並以 t 作為別名

t.speed(0)  # 設定畫筆速度為最快

# 第一組：畫出4個印章並每次旋轉 30 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(30)  # 向右轉 30 度

# 第二組：畫出4個印章並每次旋轉 55 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(55)  # 向右轉 55 度

# 第三組：畫出4個印章並每次旋轉 75 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位（補上距離參數以避免執行錯誤）
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(75)  # 向右轉 75 度

# 第四組：畫出4個印章並每次旋轉 90 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(90)  # 向右轉 90 度

# 第五組：畫出4個印章並每次旋轉 105 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(105)  # 向右轉 105 度

# 第六組：畫出4個印章並每次旋轉 125 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(125)  # 向右轉 125 度

# 第七組：畫出4個印章並每次旋轉 150 度
for i in range(4):
    t.forward(80)  # 向前移動 80 單位
    t.stamp()  # 蓋印章
    t.home()  # 回到原點
    t.right(150)  # 向右轉 150 度

t.done()  # 停留視窗不關閉
