"""
Test Runner
・テスト結果をチェックしてくれたり、デバッグしやすいように結果を表示してくれる
・unittestとpytest
    ・unittest：Python標準ライブラリ
    ・pytest：テストフレームワーク、非常に有名で多くのプロジェクトで利用されている
"""

import unittest

from power import power, times


# unittestはクラス定義して、unittestのクラスを継承する必要がある
class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        # assert power(base, exp) == 8, "This should be 8"
        self.assertEqual(power(base, exp), 8)

    def test_times(self):
        num1 = 2
        num2 = 3
        # assert times(num1, num2) == 6, "This should be 6"
        self.assertEqual(times(num1, num2), 6)


if __name__ == "__main__":
    unittest.main()

# 8 != 6
#
# 予想:6
# 実際:8
# <クリックで差分を表示>
#
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/test/112_unittest.py", line 10, in test_power
#     self.assertEqual(power(base, exp), 8)
# AssertionError: 6 != 8
#
#
#
# Ran 2 tests in 0.011s
#
# FAILED (failures=2)
#
#
# 6 != 5
#
# 予想:5
# 実際:6
# <クリックで差分を表示>
#
# Traceback (most recent call last):
#   File "/Users/endousou/Desktop/PythonLecture/test/112_unittest.py", line 16, in test_times
#     self.assertEqual(times(num1, num2), 6)
# AssertionError: 5 != 6
#
#
# プロセスは終了コード 1 で終了しました


"""
テストスクリプトはターミナルから実行することも多い
・単純に全コード実行
    python unittest.py  
・モジュールのみ呼び出して実行
    python -m unittest test_power.py  
"""
