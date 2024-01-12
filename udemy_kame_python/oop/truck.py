"""
• Challenge: Carクラスを継承するTruckクラスを作ってみよう
• Carクラスの属性に加えて，最大積載量と，現在の積載量の情報をもつようにする
• load()メソッドで，指定した重荷の重さを積んだり降ろせたりできるようにする.
  (積載量がマイナスにならないように注意する)
• 積載量をオーバーしたらその旨をprint()する.が，積むことは可能にする
"""
# 自分の回答
from car import Car

class Truck(Car):
    def __init__(self, model_name, mileage, manufacture, max_load_capacity, current_load_capacity=0):
        super().__init__(model_name=model_name, mileage=mileage, manufacture=manufacture)
        self._max_load_capacity = max_load_capacity
        self._current_load_capacity = current_load_capacity
        print("Truck init is called")

    def load_luggage(self, load):
        self._current_load_capacity += load
        if self._max_load_capacity < self._current_load_capacity:
            print(f"最大積載量{self._max_load_capacity}[ton]をオーバーしています")
            print(f"現在の積載量は{self._current_load_capacity}[ton]です")
        else:
            print(f"現在の積載量は{self._current_load_capacity}[ton]です")

    def unload_luggage(self, load):
        self._current_load_capacity -= load
        if self._current_load_capacity < 0:
            print(f"現在の積載量は0[ton]です")
        else:
            print(f"現在の積載量は{self._current_load_capacity}[ton]です")


if __name__ == "__main__":
    isuzu = Truck(model_name="Isuzu", mileage=20, manufacture="Isuzu", max_load_capacity=500, current_load_capacity=0)
    print(isuzu.model_name)
    print(isuzu.mileage)

    isuzu.gas()

    isuzu.load_luggage(200)
    isuzu.load_luggage(400)
    isuzu.load_luggage(100000)
    isuzu.unload_luggage(100000)
    isuzu.unload_luggage(400)
    isuzu.unload_luggage(210)
    isuzu.unload_luggage(100)



# 正しい回答
from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loadings):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loadings = max_loadings
        self._loadings = 0

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
    isuzu_truck.brakes()
    isuzu_truck.load(5)
    isuzu_truck.load(6)
    isuzu_truck.gas()
    isuzu_truck.load(-1)
    isuzu_truck.gas()