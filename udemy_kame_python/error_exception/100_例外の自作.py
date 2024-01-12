"""
例外を自作する
・Exceptionクラスを継承する（BaseExceptionは継承されることを意図されていないので注意）
・XXXErrorという名前にするとわかりやすい（もしその例外がエラーなら）
・自作の例外はなるべく別ファイルにまとめておく
    exceptions.pyとかerrors.py　など
"""
class MyError(Exception):

    def __str__(self):
        return "my error occured"


if __name__ == "__main__":
    response = input("y/n?: ")

    try:
        if response != "y" and response != "n":
            raise MyError
    except MyError as e:
        print(e)  # e.__str__()

    # y/n?: ｋ
    # my error occured


    # tryキャッチを無くしても可能
    if response != "y" and response != "n":
        raise MyError

    # Traceback (most recent call last):
    #   File "/Users/endousou/Desktop/PythonLecture/error_exception/100_例外の自作.py", line 18, in <module>
    #     raise MyError
    # MyError: my error occured
