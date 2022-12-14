# 이원카이제곱 - 교차분할표 이용
# : 두 개 이상의 변인(집단 또는 범주)을 대상으로 검정을 수행한다.
# 분석대상의 집단 수에 의해서 독립성 검정과 동질성 검정으로 나뉜다.

# 독립성(관련성) 검정
# - 동일 집단의 두 변인(학력수준과 대학진학 여부)을 대상으로 관련성이 있는가 없는가?
# - 독립성 검정은 두 변수 사이의 연관성을 검정한다.

#===============================================================================
# 실습 : 교육수준과 흡연율 간의 관련성(독립성) 분석 : smoke.csv'
# 귀무 : 교육수준과 흡연율간의 관련성이 없다. (서로 독립이다)
# 대립 : 교육수준과 흡겨율간의 관련성이 있다. (서로 독립이 아니다.)
#===============================================================================

import pandas as pd
import scipy.stats as stats

datas=pd.read_csv("../testdata/smoke.csv")
print(datas.head(2))
print(datas['education'].unique()) #unique() 범주확인 # [1 2 3] 세가지
print(datas['smoking'].unique()) #unique() 범주확인 # [1 2 3] 세가지

#교차표
ctab=pd.crosstab(index=datas['education'], columns=datas['smoking'])
print(ctab)
ctab.index=['대학원졸','대졸','고졸']
ctab.columns=['자드','다정','현성']
print(ctab)

chi_result=[ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]

#chi2,p,ddof,_=stats.chi2_contingency(chi_result)
chi2,p,ddof,_=stats.chi2_contingency(ctab) #교차표의 결과를 직접 적용해도 됨

print('chi2: {}, p-value: {}, ddof: {}'.format(chi2,p,ddof))
#chi2: 18.910915739853955, p-value: 0.0008182572832162924, ddof: 4
#해석: 유의확률 p-value는  0.0008182572832162924 < 0.05 이므로 귀무가설 기각한다. (연구자의 목적 성취)
#이런 결과에 상응하는 어떤 조치를 보고서에 담아주면 됨.

#야트 보정
#분할표의 자유도가 1인 경우는 x^2값이 약간 높게 계산된다. 
#절대값 |O-E|에서 0.5를 뺀 다음 제곱하며, 이 방법을 야트보정이라 한다.
#우리는 식을 쓸거라서 기억안해도 괜찮지만 알아는 둬야한다. (자유도가 1인경우에는 카이제곱값이 크게 나온다.)
#검정도구는 이를 자동으로 해 줌