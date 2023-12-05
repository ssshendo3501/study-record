# 「:」を使って、複数の要素を取ってくることができる

even = [2, 4, 6, 8, 10, 12]
print(even[1:4]) # [4, 6, 8]: 1以上4未満のindex

print(even[0:4])  # [2, 4, 6, 8]: o以上４未満のindex
print(even[:4])   # [2, 4, 6, 8]: 0は省略できる

print(even[3:5]) # [8, 10]: 3以上5未満
print(even[3:-1]) # [8, 10]: 上と同じ意味

print(even[3:]) # [8, 10, 12]
print(even[:])  # [2, 4, 6, 8, 10, 12]

text = 'hello world'
print(text[3:]) # lo world

# [開始:未満:step]
print(text[2:10:2]) # lowr: 2以上10未満を2刻みで

# 逆順
print(text[::-1])