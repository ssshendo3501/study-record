# join: list内の文字を文章化などつなげる
text_list = ["Hi", "my", "name", "is", "John"]
print(text_list)
print(" ".join(text_list)) # Hi my name is John: 半角スペースを開けることで単語が文章になる
print("-".join(text_list)) # Hi-my-name-is-John
print("*".join(text_list)) # Hi*my*name*is*John

# split: joinの逆
text = "Hi my name is John"
print(text.split(" ")) # ['Hi', 'my', 'name', 'is', 'John'] : 半角スペースで区切る
print(text.split()) # ['Hi', 'my', 'name', 'is', 'John'] : 半角スペースで区切りたいときは引数に何も入れなくてOK
print("Hi-my-name-is-John".split("-")) # ['Hi', 'my', 'name', 'is', 'John']
print("Hi*my*name*is*John".split("*")) # ['Hi', 'my', 'name', 'is', 'John']

filename = "sample.py"
print(filename.split(".")[0]) # sample: こういう書き方でファイル名から拡張子を取ってできる