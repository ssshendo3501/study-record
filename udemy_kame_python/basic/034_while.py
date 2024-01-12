# whileループ

count = 0
while count < 10:
    print(count)
    count += 1

# break と continue
# breakでif分の分岐を終了させ、continueで継続させる
while True:
    age = int(input("あなたは何歳ですか？"))
    if not 0 <= age < 120:
        print("あなたが入力した数値は正しくありません")
        continue
    else:
        print(f"あなたは{age}歳です")
        break

# コードをリファクタリングする

"""
Challenge1:「 ユーザに年齢を聞き，18歳以上なら入れるカジノ を作成する.
カジノに入ったらゲームを選べるようにする.選択できるゲームは
• 1: ルーレット
• 2:ブラックジャック 
• 3:ポーカー
選択後，ゲーム内容をpirnt()する」 上記のコードを，1~3以外の文字が入力されたら再度ゲームを
選べるようにrefactoringする
"""
age_limit_to_casino = 18
age = int(input("あなたは何歳ですか？"))
game_text = """プレイするゲームを選択してください
1:ルーレット
2:ブラックジャック
3:ポーカー
"""
if age >= age_limit_to_casino:
    print(f"あなたは{age}歳なので、カジノへの入場を許可します")
    while True:
        game = input(game_text)
        if game == "1" or game == "2" or game == "3":
            if game == "1":
                print("あなたは 1: ルーレット を選びました")
            elif game == "2":
                print("あなたは 2: ブラックジャック を選びました")
            elif game == "3":
                print("あなたは 3: ポーカー を選びました")
            break
        else:
            print("1,2,3の中から選んで下さい")
            continue
else:
    print(f"あなたは{age}歳なので、{age_limit_to_casino}歳未満の方はカジノへ入場できません")