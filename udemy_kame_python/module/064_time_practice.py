from functools import lru_cache
import time

# .time(): 1970/1/1秒数から表示（Unix時間）
print(time.time())
print(time.time()/(60*60*24*365)) # 年数表示

# 1703547913.3860412
# 54.01914996784852


# Unix時間を用いて処理の時間を測定できる
# lru_catheでキャッシュを保持することによって、処理時間を短縮化できる

@lru_cache()
def fib(n):
    print(f"fibonacci with {n} is running....")
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

before = time.time()

# 処理
print(fib(30))

after = time.time()
print(after - before)

# fibonacci with 30 is running....
# fibonacci with 29 is running....
# fibonacci with 28 is running....
# fibonacci with 27 is running....
# fibonacci with 26 is running....
# fibonacci with 25 is running....
# fibonacci with 24 is running....
# fibonacci with 23 is running....
# fibonacci with 22 is running....
# fibonacci with 21 is running....
# fibonacci with 20 is running....
# fibonacci with 19 is running....
# fibonacci with 18 is running....
# fibonacci with 17 is running....
# fibonacci with 16 is running....
# fibonacci with 15 is running....
# fibonacci with 14 is running....
# fibonacci with 13 is running....
# fibonacci with 12 is running....
# fibonacci with 11 is running....
# fibonacci with 10 is running....
# fibonacci with 9 is running....
# fibonacci with 8 is running....
# fibonacci with 7 is running....
# fibonacci with 6 is running....
# fibonacci with 5 is running....
# fibonacci with 4 is running....
# fibonacci with 3 is running....
# fibonacci with 2 is running....
# fibonacci with 1 is running....
# fibonacci with 0 is running....
# 832040
# 0.0001227855682373047


# .ctime()  今のローカル時間を文字列で返す
print(time.ctime()) # Thu Dec 21 09:03:18 2023


# .localtime()  構造化されたデータで返す
localtime = time.localtime()
print(localtime)
print(f'今の時間は、{localtime.tm_year}年{localtime.tm_mon}月{localtime.tm_mday}日{localtime.tm_hour}時{localtime.tm_min}分')
print('今の時間は、{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分'.format(localtime))

# time.struct_time(tm_year=2023, tm_mon=12, tm_mday=21, tm_hour=9, tm_min=7, tm_sec=8, tm_wday=3, tm_yday=355, tm_isdst=0)
# 今の時間は、2023年12月21日9時7分


# .sleep(secs)　secs秒だけプログラムが待機する
sec = 10
before = time.time()

# 処理
print(f"{sec}秒だけ待ってください")
# time.sleep(sec)

after = time.time()
print(after - before)
# 10.002277135848999


"""
• Challenge: 関数の実行時間(sec)を測るTmerデコレータを作ろう
"""
# func.__name__で関数名にアクセスすることが可能
# デコレータはinner関数をオブジェクトにして、inner関数を返す

def function_timer(func):
    def inner(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        after = time.time()
        print(f"{func.__name__}の実行時間は{after - before:.2f}秒かかりました")
    return inner


@function_timer
def lazy_func(sec):
    print(f"I'm working so hard ...")
    time.sleep(sec)
    print(f"I'm finally done")


lazy_func(4)  # lazy_funcの実行時間は4.01秒かかりました