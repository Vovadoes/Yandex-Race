import os

from Button import Button
from Car import classes_car, Car
from Image import Image


# print(os.listdir(r'Cars\car1\images'))

print(classes_car)

a = list(filter(lambda x: x.name == 'Первый', classes_car))
print(a[-1])

name = 'first_car_r'

car = Car(class_car=a[-1])
car.basic_image = Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\first_car_r.png'))
car.mask = Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\m_econom_2 (1).png'))
car.images = [Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\m_econom_2.png'))]
car.save(name)

print('save.. success')

car.load(name)

print('load.. success')
