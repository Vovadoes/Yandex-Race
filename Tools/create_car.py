import os
import pickle

from Button import Button
from Car import classes_car, Car
from Image import Image

full_path = os.path.join('123')

if not os.path.exists(full_path):
    os.makedirs(full_path)

for i in classes_car:
    if not os.path.exists(os.path.join(full_path, i.name)):
        os.makedirs(os.path.join(full_path, i.name))
    pickle.dump(i, open(os.path.join(full_path, i.name, 'class_car.txt'), 'wb+'))


# print(os.listdir(r'Cars\car1\images'))
# ---
# print(classes_car)
#
# a = list(filter(lambda x: x.name == 'Первый', classes_car))
# print(a[-1])
#
# name = 'first_car_r'
#
# car = Car(class_car=a[-1])
# car.basic_image = Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\first_car_r.png'))
# car.mask = Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\car1\mask.png'))
# car.images = [Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\car1\images\real_car.png'))]
# car.images.append(Button(Image(r'E:\GitHub\picturs for vova\picturs for vova\car1\images\real_car2.png')))
# car.save(name)
#
# print('save.. success')
#
# car.load(name)
#
# print('load.. success')
