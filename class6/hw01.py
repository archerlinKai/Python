x = 0
A = int(input("請輸入商品金額: "))

while A != 0:
    x += A
    print(f"目前總金額為{ x }元")
    A = int(input("請輸入商品金額: "))

print("結帳完畢")
