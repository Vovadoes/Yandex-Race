import os

from Button import Button
from Car import classes_car, Car
from Image import Image


# print(os.listdir(r'Cars\car1\images'))

car = Car(class_car=classes_car[0])
car.basic_image = Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\baby_taxi-r.png'))
car.mask = Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\m_baby (1).png'))
car.images = [Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\m_baby.png'))]
car.save('baby taxi')

print('save.. success')

car.load('baby taxi')

print('load.. success')
