num = input("請輸入身高(m): ")
n = input("請輸入體重(kg): ")
int(n)
int(num)
bmi =( / (num / n) ** 2)
if bmi < 18.5:
    print(f"BMI值為{bmi:.2f},體重過輕")
elif 18.5 <= bmi < 24:
    print(f"BMI值為{bmi:.2f},體重正常")
elif 24 <= bmi < 27:
    print(f"BMI值為{bmi:.2f},體重過重")
