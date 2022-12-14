#공분산 / 상관계수

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

df=pd.read_csv("../testdata/drinking_water.csv")
print(df.head(3))

print('df친밀도 std',np.std(df['친밀도'])) #0.968505126935272
print('df친밀도 std',np.std(df['적절성'])) #0.8580277077642035
print('df친밀도 std',np.std(df['만족도'])) #0.8271724742228969

print('---공분산(numpy)---------')
print(np.cov(df['친밀도'],df['적절성'])[0,1])
print(np.cov(df['친밀도'],df['만족도'])[0,1])
print(np.cov(df['적절성'],df['만족도'])[0,1])
print('---공분산(pandas)---------')
print(df.cov())

print('---상관계수(numpy)---------')
print(np.corrcoef(df['친밀도'],df['적절성'])[0,1]) #0.49920860859323496
print(np.corrcoef(df['친밀도'],df['만족도'])[0,1]) #0.467144983600896
print(np.corrcoef(df['적절성'],df['만족도'])[0,1]) #0.7668526996408389
print('---상관계수(pandas)---------')
print(df.corr())
print(df.corr(method='pearson')) #정규성을 따른다 / 등간, 비율척도
print(df.corr(method='spearman'))#정규성을 따르지 않는다. / 서열 척도
print(df.corr(method='kendall')) #정규성을 따르지 않는다. / 서열 척도(spearman과유사)
print()
print('---만족도에 따른 특성 사이의 상관관계 출력---------')
co_re=df.corr()
print(co_re['만족도'].sort_values(ascending=False))
print()
#그냥 시각화
df.plot(kind='scatter',x='만족도',y='적절성')
plt.show()
#판다스의 이미지 출력기능
from pandas.plotting import scatter_matrix
attr=['친밀도','적절성','만족도']
scatter_matrix(df[attr], figsize=(10,6))
plt.show()

print('---상관관계 시각화 heatmap---------')
import seaborn as sns
sns.heatmap(df.corr())
plt.show()

# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = df.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()