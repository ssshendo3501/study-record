#　docstring：関数の使い方を説明する

# docstringの書き方：reStructuredText
def multiply(num1, num2):
    """
    multiply num1 with num2 and return the result
    :param num1: first number that you want to multiply
    :param num2: second number that you want to multiply
    :return: num1 * num2
    """
    return num1 * num2


# .__doc__をするとdocが見れる
print(multiply.__doc__)
help(multiply)

# multiply(num1, num2)
#     multiply num1 with num2 and return the result
#     :param num1: first number that you want to multiply
#     :param num2: second number that you want to multiply
#     :return: num1 * num2


# docstringの書き方：GoogleStyle
def dividend(num1, num2):
    """
    num1 is divided by num2 and return the result
    Args:
        num1: number that you want to divide
        num2: number that num1 is divided by

    Returns:
        num1 / num2
    """
    return num1 / num2

