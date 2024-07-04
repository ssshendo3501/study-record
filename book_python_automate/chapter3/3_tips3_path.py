# ファイルパスに関する命令：絶対パスと相対パス

# 絶対パス：コンピュータのrootからパスを指定する
#   ex) /Users/endousou/Desktop/sample/salesbooks
# 相対パス：実行するプログラム自身や、いつも使う経理用のフォルダから見てどこなるか示したもの
#   . 作業フォルダ自身
#   ./data　作業フォルダにあるdataフォルダ
#   ./data//aaa　作業フォルダにある大たフォルダにあるaaaフォルダ
#   .. 一つ上のフォルダ
#   ../hoge　1つ上のhogeフォルダ
#   ../../hoge 2つ上のhogeフォルダ


import os

# 相対パスを絶対パスに変更する
print(os.getcwd())
print(os.path.abspath('../'))

# 
# パスからフォルダパスだけ取り出す方法
a = '/Users/endousou/Desktop/sample/salesbooks/sales-inoue.xlsx'
print(os.path.dirname(a))


# パスからファイル名だけを取り出す方法
print(os.path.basename(a))


# OS依存なしでパスを結合する
# Windowsのパスは'¥', macOSのパスは'/'
# os.path.joinを使うことにより、Windowsでは"a¥¥b¥¥c", macOSでは"a/b/c"で表示される
print(os.path.join('a', 'b', 'c'))


# 作業フォルダから対象フォルダの絶対パスを得る
path1 = os.path.abspath('./invoice-template.xlsx')
print(path1)

# プログラム自身から対象フォルダの絶対パスを得る
base_dir = os.path.dirname(__file__)
print(base_dir)
path2 = os.path.join(base_dir, 'aaa.xlsx')
print(path2)
path2 = os.path.abspath(path2)
print(path2)

