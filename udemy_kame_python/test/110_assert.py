"""
Pythonのテスト
・書いたコードは必ずテストする
・機能を開発するだけなら簡単、品質を保ちながら開発することが難しい
・テストの実行：
    ・コードを実行しながら行うテスト
    ・自動で実行するテスト
    ・他モジュールや機能との結合部分のテスト
    ・ユーザー目線での動作テスト
    ・etc...
・単体テスト(UnitTest)と結合テスト(IntegrationTest)
    ・コンポーネント単位のテストとコンポーネント間のテスト
"""


# assert

# コードを実行しながら行うテスト：a+bが3であることを確認すること
a = 1
b = 2
print(a + b)

# 自動で実行するテスト
assert a + b == 3, 'a + b is equal to 3!!'

# a + bが3でない時、下記のようなTraceback表示
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/test/110_assert.py", line 24, in <module>
#     assert a + b == 3, 'a + b is equal to 3!!'
# AssertionError: a + b is equal to 3!!


def power(base, exp):
    return base ** exp

assert power(3, 2) == 9, "3 ** 2 must be 9"

# * が1個ないと下記のTraceback
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/test/110_assert.py", line 36, in <module>
#     assert power(3, 2) == 9, "3 ** 2 must be 9"
# AssertionError: 3 ** 2 must be 9


# 1**1は1でテスト水準を決めると、**でも*でもテストが通ってしまう
# そのため、テストコードを書く際は、テストケースをあらかじめ一覧にして作るべき
def power(base, exp):
    return base ** exp

assert power(1, 1) == 1, "1 ** 1 must be 1"
