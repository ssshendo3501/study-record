# return を明示しない関数はreturn noneと同義
def print_dict(input_dict):
    for k, v in input_dict.items():
        print(f'key:{k}, value:{v}')
    return None


a = {1 : 'one', 2 : 'two'}
print(a)
return_value = print_dict(a)
print(return_value)  # None


def get_first_last_value(text):
    text = text.replace(',', '')
    words = text.split()
    return words[0], words[-1]


text = 'Hello, my name is Mike'
first, last = get_first_last_value(text)
print(f'first word is {first}, last word is {last}')
# first word is Hello, last word is Mike