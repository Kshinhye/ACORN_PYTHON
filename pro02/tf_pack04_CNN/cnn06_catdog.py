# cnn을 통한 댕댕이와 냥이 분류 모델

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import matplotlib.pyplot as plt

data_url='https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
# 압축풀기
path_to_zip=tf.keras.utils.get_file('cats_and_dogs.zip', origin=data_url,extract=True)
PATH=os.path.join(os.path.dirname(path_to_zip), 'cats_and_dogs_filtered')

# 상수정의
batch_size=128
epochs=15
IMG_HEIFHT=150
IMG_WIDTH=150

# 데이터준비
train_dir=os.path.join(PATH, 'train')
validation_dir=os.path.join(PATH, 'validation')

train_cats_dir=os.path.join(train_dir, 'cats')
train_dogs_dir=os.path.join(train_dir, 'dogs')
validation_dogs_dir=os.path.join(validation_dir, 'dogs')
validation_cats_dir=os.path.join(validation_dir, 'cats')
