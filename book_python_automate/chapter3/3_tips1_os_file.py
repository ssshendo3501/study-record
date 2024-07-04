import os

# カレントディレクトリを得る
print(os.getcwd())

# 作業フォルダを変更する
os.chdir('/Users/endousou/Desktop/sample')

# ファイルの存在確認
print(os.path.exists('hoge.xlsx'))

# 対象のパスがフォルダかどうか確認する
print(os.path.isdir('hoge.xlsx'))
print(os.path.isdir('/Users/endousou/Desktop/sample'))

# フォルダの作成
os.chdir('/Users/endousou/Desktop/sample/chapter3')
if not os.path.exists('data'):
    os.mkdir('data')

# フォルダ作成2
os.makedirs('data2', exist_ok=True)

