# 命名規則(naming convention)
# 変数名や関数(メソッド)名: snake_case 例) balance, image_height
# クラス名: CamelCase 例) Person, MyClass
# モジュールやパッケージ名: なるべく短いlower caseで，必要であればsnake_case 例) time, numpy

# アンダースコア
# - _xxx internal use only(non public)の意味
# - xxx_ Pythonで既に使われている単語を使いたいとき．(例:type_
# - __xxx クラスの属性として使うことで名前修飾される
# - __xxx__ magic methodと呼ばれるもので，Pythonが特別に設定しているもの．開発者定義することはない．(overrideすることはある)
# - _: 最近実行した戻り値や，iteration時に使わない変数

for _ in range(10):
    print("hello")


# l, I, O, : 1文字の変数は1や0に見間違えるので使わない
# correct
length = len(letter)
# wrong
l = len(letter)

# Constants(宣言後変更しない変数)は大文字のSnakeCaseを使う
PI = 3.14
PI = 3
