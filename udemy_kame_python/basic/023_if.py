# if文

age = 19
age_alcohol = 20

if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You can not young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if you have a driver license")

# if not : Falseの時返す
if not 0 < age < 120:
    print("The value is invalid")

"""
• Challenge1:もしbalance(残高)がwithdraw(引き出し額)より大きければ，
　balanceを更新し，そうでなければ引き出せないATMを作る
• Challenge2:Challenge1に加えて，引き出し額の上限を100万に設定し，
　上限を超えて引き出そうとすると引き出せないATMを作る
"""

# challenge1
balance = 1000
withdrawl = 20

if withdrawl < balance:
    # balance = balance - withdrawl
    balance -= withdrawl # 上記をこういう書き方にもできる
    print(f"残高は{balance}円です。")
else:
    print("残高不足で引き出せません。")

# challenge2
withdrawl_th = 100
if withdrawl > withdrawl_th:
    print(f"引き出し額上限:{withdrawl_th}で引き出せません")
elif withdrawl < balance:
    balance -= withdrawl
    print(f"残高は{balance}円です。")
else:
    print("残高不足で引き出せません。")

#