import os

from Car import classes_car, Car
from Image import Image


# print(os.listdir(r'Cars\car1\images'))

car = Car(class_car=classes_car[0])
car.info['path_mask'] = 'mask.png'
car.save('car1')
car.basic_image = Image('./Cars/car1/basic_image.png')
car.mask = Image('./Cars/car1/mask.png')
