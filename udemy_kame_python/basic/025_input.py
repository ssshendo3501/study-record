# input()：ユーザーが入力した値（文字列）を取得する

age = input("何歳ですか？")
print("あなたは{}歳です".format(age))

"""
• Challenge1: ユーザに年齢を聞き，18歳以上なら入れるカジノを
作成する
• Challenge2: カジノに入ったらゲームを選べるようにする.選択 できるゲームは
• 1: ルーレット
• 2:ブラックジャック • 3:ポーカー
選択後，ゲーム内容をpirnt()する
"""

# challenge1
# inputは,文字列型で入力するので注意。変数宣言の時にintに直してあげる必要がある

age_limit_to_casino = 18
age = int(input("あなたは何歳ですか？"))

if age >= age_limit_to_casino:
    print(f"あなたは{age}歳なので、カジノへの入場を許可します")
else:
    print(f"あなたは{age}歳なので、{age_limit_to_casino}歳未満の方はカジノへ入場できません")

# challenge2

age_limit_to_casino = 18
age = int(input("あなたは何歳ですか？"))
game_text = """プレイするゲームを選択してください
1: ルーレット
2:ブラックジャック
3:ポーカー
"""
if age >= age_limit_to_casino:
    print(f"あなたは{age}歳なので、カジノへの入場を許可します")
    game = input(game_text)
    if game == "1":
        print("あなたは 1: ルーレット を選びました")
    elif game == "2":
        print("あなたは 2: ブラックジャック を選びました")
    elif game == "3":
        print("あなたは 3: ポーカー を選びました")
    else:
        print("1,2,3の中から選んで下さい")
else:
    print(f"あなたは{age}歳なので、{age_limit_to_casino}歳未満の方はカジノへ入場できません")