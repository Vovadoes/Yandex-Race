from Car import classes_car, Car
from Image import Image

car = Car(class_car=classes_car[0])
car.info['path_mask'] = 'mask.png'
car.save('car1')
car.basic_image = Image('./Cars/car1/basic_image.png')
car.mask = Image('./Cars/car1/mask.png')
