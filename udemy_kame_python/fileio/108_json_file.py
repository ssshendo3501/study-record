"""
jsonモジュール
・json.load: jsonファイルをpythonデータ構造で読み込み
・json.dumps: pythonのデータ構造をjsonファイルに書き込み
・json.loads: json文字列をpythonのデータ構造に変換
・json.dumps: pythonのデータ構造をjson文字列に変換
"""

import json

# jsonの読み込み
with open('example.json') as f:
    data = json.load(f)

print(data["glossary"]["GlossDiv"])

# {'title': 'S', 'GlossList': {'GlossEntry': {'ID': 'SGML', 'SortAs': 'SGML', 'GlossTerm': 'Standard Generalized Markup Language', 'Acronym': 'SGML', 'Abbrev': 'ISO 8879:1986', 'GlossDef': {'para': 'A meta-markup language, used to create markup languages such as DocBook.', 'GlossSeeAlso': ['GML', 'XML']}, 'GlossSee': 'markup'}}}


# jsonの書き込み
new_json = {'key1': 'value1', 'key2': (1, 'value2')}
with open("new_json.json",  'w') as f:
    json.dump(new_json, f)

# タプルをjsonで書き込むとリストで返される
# {"key1": "value1", "key2": [1, "value2"]}


# jsonのリロード
with open("new_json.json",  'r') as f:
    new_json_reload = json.load(f)

print(new_json_reload)

# タプルをjsonでロードして、再度リロードするとリストで戻ってくる
# {'key1': 'value1', 'key2': [1, 'value2']}


# jsonフォーマットを文字列として読み込む
new_json = {'key1': 'value1', 'key2': (1, 'value2')}
json_str = json.dumps(new_json)

print(json_str)
print(type(json_str))

# {"key1": "value1", "key2": [1, "value2"]}
# <class 'str'>

# jsonフォーマットをpythonデータとしてロードする
python_data = json.loads(json_str)

print(python_data)
print(type(python_data))

# {'key1': 'value1', 'key2': [1, 'value2']}
# <class 'dict'>



"""
デバッグポイントの使いかた
・赤丸をつけることで、デバッグポイントをつけることが可能
・今までデータの型などをtypeで見てきたが、デバッグモードで変数の型などを確認することが可能
・いくつかデバッグポイントに書いて、再開を押せば、次のデバッグポイントに進める
・ステップオーバーで一行先に進める
・ステップインをすると実際に関数に入って確認することが可能
"""