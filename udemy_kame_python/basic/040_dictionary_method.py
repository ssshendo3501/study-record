# 辞書型のメソッド
fruits_colors = {'apple' : 'red', 'lemon' : 'yellow', 'grapes' : 'purple'}

# 辞書から何か値を取ってきたいとき
# 辞書['キー']　で実施するが、指定するキーがないときエラーになる
print(fruits_colors['apple'])
# print(fruits_colors['peach']) # KeyError: 'peach'

# .get():辞書から値を取ってきたいとき、辞書にないものはデフォルトで値を返す
# 辞書.get('指定したいキー' ,　'指定したキーがないときデフォルトの値')
print(fruits_colors.get('apple', 'nothing')) # red：appleがあるのでredが入ってくる
print(fruits_colors.get('peach', 'nothing')) # nothing：peachがないのでデフォルトの値が返ってくる

fruit = input('フルーツの名前を指定してください')
print(fruits_colors.get(fruit, 'そんなフルーツはありません'))

# .update(): 辞書同士の結合（リストで言うappendみたいなもの）
fruits_colors2 = {'peach' : 'pink', 'kiwi' : 'green'}
fruits_colors.update(fruits_colors)
print(fruits_colors)

