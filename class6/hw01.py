x = 0
A = float(input("請輸入商品經額:"))
while A != 0:
    A += x
    print(f"目前總額為:{A}")
    A = int(input("請輸入商品經額:"))
if A == 0:
    print("結帳完畢")
