class ClassCar:
    def __init__(self, name, k_money=1):
        self.name = name
        self.k_money = k_money


classes_car = []
classes_car.append(ClassCar("Обычный"))
classes_car.append(ClassCar("Премиум", 2))


class Car:
    def __init__(self):
        self.image_left = None
        self.image_right = None
        self.class_car = None

    def load(self):
        return self

    def save(self):
        pass
