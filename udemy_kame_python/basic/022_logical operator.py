# 論理演算子（logical operators）: and, or, not

a = 1
b = 1
c = 10
d = 100

print(a == b and c > d) # aとbは等しく、かつ、cはdよりも大きいか？ > False
print(a == b or c > d) # aとbは等しく、または、cはdよりも大きいか？ > True

"""
変数を作ってprint()してみよう!
• Challenge1: 年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
• Challenge2: 修士号保持もしくは5年以上実務経験があればVisaの 取得が可能
"""
# challenge1
age = 9
height = 160
print(age >= 10 and height >=110)

#challenge2
master = True
job_experience = 4
print(master is True or job_experience >= 5)