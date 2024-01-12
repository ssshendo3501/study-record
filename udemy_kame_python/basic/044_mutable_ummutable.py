# mutable: 変更可能なオブジェクト　list, dict, set
# listは変更可能なオブジェクトなのでidは変わらない
fruits = ['apple', 'peach', 'banana']
print(fruits)
print(f'fruitsのIDは{id(fruits)}')
fruits.append('lemon')
print(fruits)
print(f'fruitsのIDは{id(fruits)}')

# ['apple', 'peach', 'banana']
# fruitsのIDは4558260480
# ['apple', 'peach', 'banana', 'lemon']
# fruitsのIDは4558260480


# immutable: 変更不可能なオブジェクト　int, floot, str, bool, tuple
# 文字型は変更不可能なオブジェクトなのでidが変わる
fruit = 'apple'
print(fruit)
print(f'fruitのIDは{id(fruit)}')
fruit += ', lemon'
print(fruit)
print(f'fruitのIDは{id(fruit)}')

# apple
# fruitのIDは4540842656
# apple, lemon
# fruitのIDは4541058480

# text = 1-2-3-4-5-...　というのを出力したいとき
# 下記はtextでイミュータブルな型を使っているのでfor文の度に毎回メモリを使うので効率が悪いとされている
text = ''
for i in range(1,10):
    if i == 1:
        text += str(i)
    else:
        text += '-' + str(i)
    print(id(text))
print(text)

# listを使うことでミュータブルな型を使うことでメモリを消費せず良い書き方とされている
# より良いコードを書くことをpythonicで書くと言う
text_list = []
for i in range(1,10):
    text_list.append(str(i))
    print(id(text_list))
text ='-'.join(text_list)
print(text)