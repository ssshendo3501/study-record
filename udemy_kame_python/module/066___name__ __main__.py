# __name__, __main__：Pythonがシステム的に使っている文字列

# __main__
import mymodule

# __name__: importされると自分のmodule名が入るが、そのスクリプト自体がcallされると__main__が出力される
mymodule.myfunc()
print(__name__)

# This is my module!!　# mymoduleのトップレベルの出力
# mymodule.name: mymodule　# mymoduleのトップレベルの出力
# This is my function!
# __main__

# if __name__ == "__main__":   を書くと、トップレベルの出力を書いても呼び出す時出力されなくなる
# This is my function!
# __main__