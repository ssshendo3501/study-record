import os
import glob

# 可憐度ディレクトリの全てのファイルを列挙
print(glob.glob('*'))

# .xlsxファイルのみ列挙
print(glob.glob('*.xlsx'))

# inから始まる.xlsxファイルのみ列挙
print(glob.glob('in*.xlsx'))

# 末尾に1が入っているエクセルファイル
print(glob.glob('*1.xlsx'))


# osと組み合わせてファイル操作
os.chdir('/Users/endousou/Desktop/sample/salesbooks')
print(glob.glob('sales-*.xlsx'))
