# ダミーデータ
dummy_data = [['伊藤', 300], 
              ['伊藤', 600], 
              ['伊藤', 200], 
              ['田中', 300],
              ['田中', 200]
              ]

# データを顧客名で辞書型に分割
users = {}
for row in dummy_data:
    name, value = row
    # 顧客名が初出ならリストを初期化
    if name not in users:
        users[name] = []
    users[name].append(value)

# 顧客ごとに集計
for name, rows in users.items():
    print(name, rows) 
    # 顧客の購入金額を計算
    total = 0
    for row in rows:
        # print(row)
        total += row
        # print(total)
    print(name, total)
