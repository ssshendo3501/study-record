from datetime import datetime, timedelta

# 現在時刻の取得
t = datetime.now()
print(t)

# フォーマット変更
fmt = t.strftime('%Y年%m月%d日')
print(fmt)

# 日付を指定
t = datetime(2022, 1, 1)
fmt = t.strftime('%Y%m%d')
print(fmt)

# あと何日？を調べる
yoteibi = datetime(2024, 7, 3)
now = datetime.now()
delta = yoteibi - now
print(f'あと {delta.days+1}日 です')

# あと何秒？を調べる
sleep_t = datetime(2024, 6, 20, 23, 0, 0)
wakeup_t = datetime(2024, 6, 20, 7, 30, 0)
delta = sleep_t - wakeup_t
print(f'あと {delta}時間です')
sec = delta.seconds
hours = sec / (60 * 60)
print(f'あと {hours}時間 です')

# N日後を調べる
base_t = datetime(2024, 7, 10)
t = base_t + timedelta(days=3)
print(t.strftime('%Y%m%d'))



