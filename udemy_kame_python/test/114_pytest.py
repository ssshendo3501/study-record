"""
pytest
・pythonのテストフレームワークで、多くのプロジェクトが採用している
・python標準のassertを使って簡潔に書ける
・pip install pytestを使ってインストールする
・ターミナルから実行するのが便利
    ・pytest 114_pytest：テストの実行
    ・pytest 114_pytest -v：詳細を記載して、テストの実行
    ・pytest <フォルダ名>：フォルダの中のすべてのテストコードを実行
・pytestを使うと非常にシンプルな方法でテストコードを書くことができる
    ・unittestのようにクラス定義によるテスト継承しメソッド化が不要（わかりやすいようにクラスに定義しても良い）
    ・assertEqualなど特定のassert関数を付与する必要がない
・テストの際はunittestとpytestを混同することはない
"""

import pytest

from power import power, times, divide


def test_power():
    base = 2
    exp = 3
    # 標準のassertを使ってテスト可能
    assert power(base, exp) == 8
    # 例外のテストをするためにはimport pytestをする必要がある
    with pytest.raises(TypeError):
        power("3", "2")


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6


def test_divide():
    num1 = 4
    num2 = 2
    assert divide(num1, num2) == 2


def test_divide_by_zero():
    num1 = 4
    num2 = 0
    assert divide(num1, num2) is None


# ~/Desktop/PythonLecture/test ❯ pytest 114_pytest.py                                                                                                                                                                        Py test
# ======================================================================================================= test session starts =======================================================================================================
# platform darwin -- Python 3.12.0, pytest-7.4.4, pluggy-1.3.0
# rootdir: /Users/endousou/Desktop/PythonLecture/test
# plugins: cov-4.1.0
# collected 2 items
#
# 114_pytest.py FF                                                                                                                                                                                                            [100%]
#
# ============================================================================================================ FAILURES =============================================================================================================
# ___________________________________________________________________________________________________________ test_power ____________________________________________________________________________________________________________
#
#     def test_power():
#         base = 2
#         exp = 3
#         # 標準のassertを使ってテスト可能
# >       assert power(base, exp) == 8
# E       assert 6 == 8
# E        +  where 6 = power(2, 3)
#
# 114_pytest.py:20: AssertionError
# ___________________________________________________________________________________________________________ test_times ____________________________________________________________________________________________________________
#
#     def test_times():
#         num1 = 2
#         num2 = 3
# >       assert times(num1, num2) == 6
# E       assert 5 == 6
# E        +  where 5 = times(2, 3)
#
# 114_pytest.py:29: AssertionError
# ===================================================================================================== short test summary info =====================================================================================================
# FAILED 114_pytest.py::test_power - assert 6 == 8
# FAILED 114_pytest.py::test_times - assert 5 == 6
# ======================================================================================================== 2 failed in 0.05s ========================================================================================================