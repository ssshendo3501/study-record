"""
ジェネレーター：
・メモリを節約する仕組み、もしくはジェネレーターの機能を持つオブジェクトのこと
・すべてのデータをメモリに置く代わりに、イテレーション時に毎回出力する
  （HDから取得したり、計算したり、もしくはその両方）
・ジェネレーターはデータ分析など大きなデータを扱うときに効果を発揮する

イテレーター
・イテレーターはもう少し一般的な呼び方
・イテレーターはジェネレーターの特別な形
"""

import csv
import sys


range_nums = range(20)
for i in range_nums:
    print(i)

list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
for i in list_nums:
    print(i)


# 上記2つのコードは同じ出力がされるがメモリの消費量が異なる
# rangeの方がメモリの節約される。これがジネレーターを使う理由
# range_numsは、1回どこかメモリを確保して出力する時（上記であればfor文を回す時）に、毎回メモリの中で計算が起こる
# メモリに載せるのは最低限のデータのみで、出力する時に毎回必要な分だけ計算し、メモリの消費を抑える
# list_numsは、最初にlistの領域を確保しているので、メモリのサイズが大きくなる
print(sys.getsizeof(range_nums))
print(sys.getsizeof(list_nums))

# 48
# 136

# このreaderのオブジェクトもジェネレーターとなる
# 少ないメモリを蓄積しておき、必要な分だけ都度出力する
with open('example.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
        print(sys.getsizeof(reader))  # 48