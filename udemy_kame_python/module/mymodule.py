myvaliable = "This is global valiable"


def myfunc():
    print("This is my function!")


def anotherfunc():
    print("This is another function!")


# moduleのトップレベルに出力を書くとimportした時に出力されてしまう
if __name__ == "__main__":
    myfunc()
    anotherfunc()
    print(myvaliable)
    print("This is my module!!")
    print(f"mymodule.name: {__name__}")