# 関数をテストするものはテストスクリプトとして別のファイルの書くのが一般的
from power import power, times


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8, "This should be 8"


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6, "This should be 6"


# pythonで一度tracebackが発生するとプログラムがクラッシュするので、
# その場でテストスクリプトが終了してしまい、すべての関数のテストができない
# そこで、テストランナーを使用する　-> 次セクション
if __name__ == "__main__":
    test_power()
    test_times()

# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/test/111_test_script.py", line 21, in <module>
#     test_times()
#   File "/Users/endousou/Desktop/PythonLecture/test/111_test_script.py", line 13, in test_times
#     assert times(num1, num2) == 6, "This should be 6"
# AssertionError: This should be 6

