# 독버섯(poisonous)인지 식용버섯(edible)인지 분류
# https://www.kaggle.com/datasets/uciml/mushroom-classification
# feature는 중요변수를 찾아 선택, label:class
#
# 데이터 변수 설명 : 총 23개 변수가 사용됨.
#
# 여기서 종속변수(반응변수)는 class 이고 나머지 22개는 모두 입력변수(설명변수, 예측변수, 독립변수).
# 변수명 변수 설명
# class      edible = e, poisonous = p
# cap-shape    bell = b, conical = c, convex = x, flat = f, knobbed = k, sunken = s
# cap-surface  fibrous = f, grooves = g, scaly = y, smooth = s
# cap-color     brown = n, buff = b, cinnamon = c, gray = g, green = r, pink = p, purple = u, red = e, white = w, yellow = y
# bruises        bruises = t, no = f
# odor            almond = a, anise = l, creosote = c, fishy = y, foul = f, musty = m, none = n, pungent = p, spicy = s
# gill-attachment attached = a, descending = d, free = f, notched = n
# gill-spacing close = c, crowded = w, distant = d
# gill-size       broad = b, narrow = n
# gill-color      black = k, brown = n, buff = b, chocolate = h, gray = g, green = r, orange = o, pink = p, purple = u, red = e, white = w, yellow = y
# stalk-shape  enlarging = e, tapering = t
# stalk-root    bulbous = b, club = c, cup = u, equal = e, rhizomorphs = z, rooted = r, missing = ?
# stalk-surface-above-ring fibrous = f, scaly = y, silky = k, smooth = s
# stalk-surface-below-ring fibrous = f, scaly = y, silky = k, smooth = s
# stalk-color-above-ring brown = n, buff = b, cinnamon = c, gray = g, orange = o, pink = p, red = e, white = w, yellow = y
# stalk-color-below-ring brown = n, buff = b, cinnamon = c, gray = g, orange = o,pink = p, red = e, white = w, yellow = y
# veil-type      partial = p, universal = u
# veil-color     brown = n, orange = o, white = w, yellow = y
# ring-number none = n, one = o, two = t
# ring-type     cobwebby = c, evanescent = e, flaring = f, large = l, none = n, pendant = p, sheathing = s, zone = z
# spore-print-color black = k, brown = n, buff = b, chocolate = h, green = r, orange =o, purple = u, white = w, yellow = y
# population abundant = a, clustered = c, numerous = n, scattered = s, several = v, solitary = y
# habitat       grasses = g, leaves = l, meadows = m, paths = p, urban = u, waste = w, woods = d

import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from xgboost import plot_importance
import xgboost as xgb

data = pd.read_csv('../testdata/mushrooms.csv')
print(data.head(3), data.shape)  # (8124, 23)
print(data.info())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
for col in data.columns:
    data[col] = le.fit_transform(data[col])
print(data.head(3))
print(data.isnull().sum()) # 널값없음

features = data.iloc[:, 1:23] # 독립
print(features.head(3))
labels = data['class'] # 종속
print(labels.head(3))

# XGBClassifier로 중요 변수 뽑아내기
model = xgb.XGBClassifier(booster = 'gbtree', max_depth = 6, n_estimators=500 ).fit(features, labels)
fig, ax = plt.subplots(figsize = (10, 12))
plot_importance(model, ax = ax) 
plt.show() # spore-print-color : 315, odor : 125, gill-size : 80, cap-color : 61  # 상위4개만 뽑음

i_features = data[['spore-print-color', 'odor', 'gill-size', 'cap-color']] # 중요변수 따로 뽑아서 담아줌
x_train, x_test, y_train, y_test = train_test_split(i_features, labels, test_size = 0.3, random_state=1)

# model
model = GaussianNB().fit(x_train, y_train)
pred = model.predict(x_test)
print('예상값 :', pred[:3])
print('실제값 :', y_test[:3].values)
print('총갯수 :%d, 오류수:%d'%(len(y_test), (y_test != pred).sum()))
print('분류정확도 :', metrics.accuracy_score(y_test, pred))
