"""
オーバーライド（overriding）
・親クラスのメソッドを、サブクラス用にメソッドを書き換える・追加する
・オーバーロードとは別物なので注意する（Pythonにはオーバーロードはない）
"""

from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loadings):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loadings = max_loadings
        self._loadings = 0

    """親クラスのgasメソッドのオーバーライド"""
    def gas(self):
        if self._loadings > self._max_loadings:
            print("重量オーバーなので走れません")
            print(f"最低でも{self._loadings - self._max_loadings}tの荷物をおろしてください。")
        else:
            """elseの時に親クラスのgasメソッドを呼ぶ"""
            super().gas()

    def load(self, weight):
        if weight > 0:
            print(f"{weight}tの荷物を積みました")
            self._loadings += weight
        else:
            if self._loadings <= -weight:
                print(f"{self._loadings}t全ての荷物を降ろしました")
                self._loadings = 0
            else:
                print(f"{-weight}tの荷物を降ろしました")
                self._loadings += weight
        print(f"現在の積載量は{self._loadings}tです")
        if self._loadings > self._max_loadings:
            print(f"最大積積載量は{self._max_loadings}tです.重量オーバーです．！！")

    def gas(self):
        if self._loadings > self._max_loadings:
            print("重量オーバーなので走れません")
            print(f"最低でも{self._loadings-self._max_loadings}tの荷物をおろしてください")
        else:
            super().gas()


if __name__ == "__main__":
    isuzu_truck = Truck("トラックA", 6, "いすゞ", 10)
    isuzu_truck.gas()
    isuzu_truck.breaks()
    isuzu_truck.load(5)
    isuzu_truck.load(6)
    isuzu_truck.gas()
    isuzu_truck.load(100)
    isuzu_truck.gas()