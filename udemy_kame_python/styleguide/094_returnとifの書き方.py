# return

# xの政府を見て平方根を返す関数
# return Noneは書く必要がないが、StyleGuideでは書くようにする
# returnを書くなら全部書く、書かないなら全部書くことを徹底する
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None


# if文などでオブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int)
# wrong
if type(obj) is type(1)


# Booleanに対して比較演算子を使わない
# wrong
if bool_ver == True
# correct
if bool_var


# type_hint
# 一つでもhintをつけたら全てにつける
# Pythonがtypeのチェックをしてくれるわけではない（str以外でも問題なく関数を呼ぶことは可能）
# Pythonは動的型付け言語であるため。
# type_hintを矯正したり、命名規約に入れるべきではない
def greeting(name: str) -> str:
    return "Hello" + name


