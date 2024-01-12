# Pythonでは関数が引き取った引数の型のチェックができる
# 手段1：isintance()を使う
# 手段2：関数の振る舞いをチェックする

class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")


# 手段1
# クラスがAnimalクラスであればwalkメソッドを実行するコード
# typeでクラスを判別しようとするとサブクラスを拾って判断できない
# そのため、クラスの型チェックはisuinstance()で行う
# isinstance()関数はサブクラスでもきちんとTrueで返ってくる
def walk_with_me(animal: Animal) -> None:
    # if type(animal) is Animal:
    if isinstance(animal, Animal):
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩(walk)できません")


if __name__ == "__main__":
    pochi = Animal("Pochi")
    walk_with_me(pochi)
    hachi = Dog("Hachi")
    walk_with_me(hachi)


# Pochi is walking
# Hachi is walking



# 手段2
# Pythonは動的型付け言語であるため、本当はその変数がクラスを判断するか
# （データの型で）判断するよりも、
# animalという変数にwalkがあるか？を考えれば良い
# getattr()というビルトインファンクションを使うことで、変数がメソッドのAttributeを持っているか判断できる
# callableはその変数が呼ぶことができるか（可能であればTrueを返す）
def walk_with_me(animal: Animal) -> None:
    # if type(animal) is Animal:
    # if isinstance(animal, Animal):
    method = getattr(animal, 'walk', None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f"{type(animal).__name__}は散歩(walk)できません")


if __name__ == "__main__":
    pochi = Animal("Pochi")
    walk_with_me(pochi)
    hachi = Dog("Hachi")
    walk_with_me(hachi)


# Pochi is walking
# Hachi is walking
