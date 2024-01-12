def func(first, second, third):
    print(f"fisrt: {first}, second: {second}, third: {third}")

# argument <-> parameter
func("1", "2", "3")

# 順番を変えて引数を指定したい時は下記のように書く
func("1", third="3", second=2)

# 関数にデフォルトの値を入れたい場合
# デフォルトで指定するパラメータ：キーワードパラメータ
# 指定しないパラメータ：ポジショナルパラメータ
# キーワードパラメータは必ずポジショナルパラメータの後に書く必要がある
def func(first, second, third="3"):
    print(f"fisrt: {first}, second: {second}, third: {third}")


# デフォルトで3が記載される
func("11", "22")