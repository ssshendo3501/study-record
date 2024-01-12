# 今回はcar.pyにCarクラスを書いているが必ずしもそういう必要はない
# ただファイル名とクラス名は合わせた方がわかりやすい
# また。一つのファイルに複数のクラスを書くこともよくある

class Car():
    def __init__(self, model_name, mileage, manufacture):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        print(f'{self.manufacture}の{self.model_name}(燃費：{self.mileage})のアクセルを踏みます')

    def breaks(self):
        print('{0.manufacture}の{0.model_name}(燃費：{0.mileage})のブレーキを踏みます'.format(self))



# Carクラスを別ファイルから呼び出したいときに出力されないように、
# if __name == "__main__" を記載する
if __name__ == "__main__":
    # インスタンス生成
    prius = Car("Prius", 20, "TOYOTA")

    print(prius.mileage)
    prius.gas()
    prius.breaks()

# 20
# TOYOTAのPrius(燃費：20)のアクセルを踏みます
# TOYOTAのPrius(燃費：20)のブレーキを踏みます