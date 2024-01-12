# 034_whileで書いたコードをリファクタリングしていく

age_limit_to_casino = 18
age = int(input("あなたは何歳ですか？"))
game_text = """プレイするゲームを選択してください
1:ルーレット
2:ブラックジャック
3:ポーカー
"""

game_dict = {1 : 'ルーレット', 2 : 'ブラックジャック', 3 : 'ポーカー', 4 : 'スロット'}



if age >= age_limit_to_casino:
    print(f"あなたは{age}歳なので、カジノへの入場を許可します")
    while True:
        print('プレイするゲームを選択してください。:')
        for num, game_name in game_dict.items():
            print(f'{num} : {game_name}')
        game = int(input(":"))
        if game in game_dict:
            print(f'あなたは{game_dict[game]}を選びました。')
            break
        else:
            print("正しい選択肢から選んで下さい")
            continue
else:
    print(f"あなたは{age}歳なので、{age_limit_to_casino}歳未満の方はカジノへ入場できません")