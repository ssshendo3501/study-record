# built in module一覧：https://docs.python.org/3/py-modindex.html

# Regular Expresssion（正規表現　通称RegEx）
import re

email = "mymail@gmail.com"

matched = re.search('@\w+\.', email)    # emailの中に＠があって、@の後に１文字以上あって.があるか探す
if matched:
    print(matched)
    print("Matched!!")
else:
    print("Not found")  # Matched!!


# [] : abcが入っているか探す。どれか入ってればTureを返される
print(re.search('[abc]', 'b'))
print(re.search('[abc]', 'dd'))
print(re.search('[abc]', 'apple'))
print(re.search('[abc]', '1234'))

# <re.Match object; span=(0, 1), match='b'>
# None
# <re.Match object; span=(0, 1), match='a'>
# None

print(re.search('[1-3]', '1234')) # 1~3
print(re.search('[a-c]', 'ddda')) # a~c

# <re.Match object; span=(0, 1), match='1'>
# <re.Match object; span=(3, 4), match='a'>


# ^ : 最初の文字
print(re.search('^[0-9]', '1234')) # 最初の文字が数字かどうか？
print(re.search('^[0-9]', 'abc123'))

# <re.Match object; span=(0, 1), match='1'>
# None


# {n} n回リピート
print(re.search('^[0-9]{4}', '1234')) # 最初の文字が数字で、それを４回繰り返しているか？
print(re.search('^[0-9]{4}', '2020/4/5')) # 最初の文字が数字で、それを４回繰り返しているか？
print(re.search('^[0-9]{4}', '20/4/5')) # 最初の文字が数字で、それを４回繰り返しているか？

# <re.Match object; span=(0, 4), match='1234'>
# <re.Match object; span=(0, 4), match='2020'>
# None


# {n,m} 最低n回、最高m回リピート
print(re.search('^[0-9]{2,4}', '1234')) # 最低２回、最高４回リピートしているか？
print(re.search('^[0-9]{2,4}', '20/4/5')) # 最低２回、最高４回リピートしているか？
print(re.search('^[0-9]{2,4}', 'aaaa')) # 最低２回、最高４回リピートしているか？
print(re.search('^[0-9]{2,4}', '3627618')) # 最低２回、最高４回リピートしているか？

# <re.Match object; span=(0, 4), match='1234'>
# <re.Match object; span=(0, 2), match='20'>
# None
# <re.Match object; span=(0, 4), match='3627'>


# $ : 最後の文字
print(re.search('[0-9]{2}$', '2020/4/23')) # 最後の２文字が数字であるかどうか？
print(re.search('[0-9]{2}$', '1234')) # 最後の２文字が数字であるかどうか？

# <re.Match object; span=(7, 9), match='23'>
# <re.Match object; span=(2, 4), match='34'>


# * 左のパターンを０回以上繰り返す
print(re.search('a*b', 'b')) # 左のパターン（a）を０回以上繰り返しているか？
print(re.search('a*b', 'a'))
print(re.search('a*b', 'dddb'))
print(re.search('a*b', 'bbba'))
print(re.search('a*b', 'ab'))

# <re.Match object; span=(0, 1), match='b'>
# None
# <re.Match object; span=(3, 4), match='b'>
# <re.Match object; span=(0, 1), match='b'>
# <re.Match object; span=(0, 2), match='ab'>


# + 左のパターンを１回以上繰り返す
print(re.search('a+b', 'ab')) # bの前にaが１回以上あるか？
print(re.search('a+b', 'ba'))

# <re.Match object; span=(0, 2), match='ab'>
# None

# ? 左のパターンを0回か1回繰り返す
print(re.search('ab?c', 'abc')) # cの前にbを0回か1回繰り返す
print(re.search('ab?c', 'abbbbcc')) # cの前にabを0回か1回繰り返す
print(re.search('ab?c', 'ab')) # cの前にabを0回か1回繰り返す
print(re.search('ab?c', 'bc')) # cの前にabを0回か1回繰り返す

# <re.Match object; span=(0, 3), match='abc'>
# None
# None
# None


# | or
print(re.search('abc|012', '01')) # abcもしくは012がマッチする

# None


# ()　グループ
print(re.search('te(s|x)t', 'test')) # test or text
print(re.search('te(s|x)t', 'text')) # test or text
print(re.search('te(s|x)t', 'tet')) # test or text

# <re.Match object; span=(0, 4), match='test'>
# <re.Match object; span=(0, 4), match='text'>
# None


# . 任意の1文字
print(re.search('h.t', 'hot')) # hxt
print(re.search('h.t', 'hit')) # hxt
print(re.search('h.t', 'hint')) # hxt

# <re.Match object; span=(0, 3), match='hot'>
# <re.Match object; span=(0, 3), match='hit'>
# None


# \　エスケープ
print(re.search('h\.t', 'h.t')) # h.t

# <re.Match object; span=(0, 3), match='h.t'>


# \w [a-z,A-Z, 0-9] すべてのアルファベット、数字およびアンダースコア
print(re.search('h\wt', 'hit')) # hxt
print(re.search('h\wt', 'h0t')) # hxt
print(re.search('h\wt', 'h_t')) # hxt
print(re.search('h\wt', 'hint')) # hxt

# <re.Match object; span=(0, 3), match='hit'>
# <re.Match object; span=(0, 3), match='h0t'>
# <re.Match object; span=(0, 3), match='h_t'>
# None


"""
• Chllenge1: input()で入力した生年月日(yyyy/mm/dd)のフォーマットが
正しいフォーマットになっているかをチェックするプログラムを正規表現で作ろう
(暦の正しさは無視してOK.例えば 2021/2/30や2020/11/31はOKとする.)
"""

# 最初の数字は1900年か2000年代　^(19|20)
# 年代の下二桁は0-9のうちなんでも良い数字を2回繰り返す　[0-9]{2}
# /　スラッシュ
# 月は1桁か2桁 ([1-9]|1[0-2])
# /　スラッシュ
# 日は4パターンある ([1-9]|1[0-9]|2[0-9]|3[01])

patatern_data_of_birth = "^(19|20)[0-9]{2}/([1-9]|1[0-2])/([1-9]|1[0-9]|2[0-9]|3[01])"

while True:
    date_of_birth = input("生年月日を入力してください(yyyy/mm/dd)")
    result = re.search(patatern_data_of_birth, date_of_birth)

    if result:
        print(f'{date_of_birth}は正しいフォーマットです')
        break
    else:
        print(f'{date_of_birth}は正しいフォーマットではありません')


'''
• Challenge2: input()で入力されたemailアドレスのフォーマットが
正しいフォーマットになってるかをチェックするプログラムを作ろう

my_email.address@gmail.com
2or3文字のアルファベット(大文字or小文字)
1文字以上の英数字(大文字小文字)orアンダースコア/ピリオド/ハイフン
'''

patatern_email = "^(\w|\.|\-)+@^(\w|\.|\-)+\.[a-zA-Z]{2,3}$"

while True:
    email = input("emailを入力してください")
    result = re.search(patatern_email, email)

    if result:
        print(f'{email}は正しいフォーマットです')
        break
    else:
        print(f'{email}は正しいフォーマットではありません')