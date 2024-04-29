"""
例外ケースのテスト
・誤ったデータを入れたらきちんとエラーを返すかテストする
・考えられる例外は無数に出てくるので、ある程度絞ってテストをする
・withステートメントを使ってテストをする

unittestのassert
https://docs.python.org/3/library/unittest.html
"""

import unittest

from power import power, times


class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        # assert power(base, exp) == 8, "This should be 8"
        self.assertEqual(power(base, exp), 8)
        # context manager
        with self.assertRaises(TypeError):
            power(3, 2)

    def test_times(self):
        num1 = 2
        num2 = 3
        # assert times(num1, num2) == 6, "This should be 6"
        self.assertEqual(times(num1, num2), 6)


if __name__ == "__main__":
    unittest.main()
