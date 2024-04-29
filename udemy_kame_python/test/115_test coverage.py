"""
テストカバレッジ
・テストコードを書いてすべてのテストが通ったからといって、それでOKかというとそうではない
・このテストコードがサンプルのどれぐらいの水準をカバーしているかわからないため
・このテストカバー率のことをテストカバレッジという

・pip install pytest-cov：pytestのテストカバレッジのプラグインをインストール
・ターミナル上で、下記実行
    pytest 114_pytest.py --cov=power
・Stmtsはコードの行。（if文などはifとelseは合わせて一行で扱う）

・テストが通ったからといって、すべての場合分けでテストされているわけではない
・また、テストコードにassert文を入れない（print文とかでも）のテストコードでも、
  テストが通ればカバー率は100%になるので、テストコードも含めきちんと確認するのが良い
・下記のカバレッジの結果をhtmlやxmlでで出力することも可能
    pytest 114_pytest.py --cov=power --cov-report html
    pytest 114_pytest.py --cov=power --cov-report xml
    pytest 114_pytest.py --cov=power --cov-report xml --cov-append
        既存のxmlを更新する形で出力する（テスト結果が膨大な時、ファイルが過多になるのを防ぐ）

TDD：Test Driven Development
・今回扱った内容は開発におけるテスト領域の基礎の基礎
・開発の際は、テストコードを先に書いてから、このテストが通るような関数を作るということが推奨される（TDD）
・TDDに慣れると、テストコード無しにコードを書くのが怖くなってくる
・テストコードをきちんと書くというのはとても重要で、開発する前から準備しておくのが良い
"""

# power.pyに新しく、divideの関数を付与
# ---------- coverage: platform darwin, python 3.12.0-final-0 ----------
# Name       Stmts   Miss  Cover
# ------------------------------
# power.py       8      3    62%
# ------------------------------
# TOTAL          8      3    62%

# 114_pytest.pyのコードにdivide関数のテストコードを付与
# ---------- coverage: platform darwin, python 3.12.0-final-0 ----------
# Name       Stmts   Miss  Cover
# ------------------------------
# power.py       8      1    88%
# ------------------------------
# TOTAL          8      1    88%


# 114_pytest.pyのコードにtest_divide_by_zeroのテストコードを付与
# ---------- coverage: platform darwin, python 3.12.0-final-0 ----------
# Name       Stmts   Miss  Cover
# ------------------------------
# power.py       8      0   100%
# ------------------------------
# TOTAL          8      0   100%


