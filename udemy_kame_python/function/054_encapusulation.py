# カプセル化（encapusulation）:外からアクセスできないようにする（情報隠蔽）
# カプセル化はオブジェクト指向の分野で用いられる

# if以下がouter_function、def inner~以下がinner function　
# メインのinner_casino_entranceの関数には外からアクセスできなくなる　->カジノへ入るためにはcasino_entranceを呼ばなきゃいけなくなる
# カジノのメインの関数と、入場制限の関数で機能が分離できる -> レスポンシビリティの分離
def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f"{min_age}歳未満お断り")
        return

    def inner_casino_entrance():
        print("ようこそカジノへ")

    return inner_casino_entrance()


casino_entrance(34) # ようこそカジノへ
