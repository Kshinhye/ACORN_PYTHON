# 내가 그린 손글씨 이미지 분류 결과 호가인
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image #이미지 확대/축소 기능을 가지고 있음
import tensorflow as tf

# model을 만들 때 정규화했기 때문에 새로운 데이터도 정규화 해야한다.

im=Image.open('cs.png')
img=np.array(im.resize((28,28), Image.ANTIALIAS).convert('L')) #Image.ANTIALIAS 고해상도 -> 저해상도 할 때 부드럽게 만들어줌
print(img.shape)

plt.imshow(img, cmap='Greys')
plt.show()

data=img.reshape([1, 784])
print(data)
data= data/255.0 # 정규화(∵ 모델 학습 시 정규화를 했으므로)
# print(data)

# 학습이 끝난 모델로 내 이미지를 판별
mymodel=tf.keras.models.load_model('cla07model.hdf5')
pred=mymodel.predict(data)
print('pred: ', np.argmax(pred, 1))
