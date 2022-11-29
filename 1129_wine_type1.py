import numpy as np
import pandas as pd

from sklearn.datasets import load_wine

x = pd.DataFrame(load_wine().data, columns=load_wine().feature_names)
y = pd.Series(load_wine().target, name='class')

x.head()

# 스키마 정의
# malic_acid: 말산
# ash: 회분
# total_phenols: 폴리페놀 총량
# flavanoids: 플라보노이드 폴리페놀
# nonflavonoid_phenols: 비 플라보노이드 폴리페놀
# color_intensity: 색상의 강도
# hue: 색상
# od280... : 희석 와인의 DD280/OD315 비율
# class: 와인 종류
# class 분류 문제

x.describe()

x.info()

# total_pheonols 결측치를 제거하고 alcaliniry_of_ash 변수의 결측치는 중앙값으로 대체한 후, alcalinirty_of_ash의 평균값을 계산, 최종 계산 값의 소수점 이하는 버린다.

# 근데 일단 사이킷런에서 가져온 데이터셋은 결측치가 없으므로.. 코드만 작성

#아래 두 줄은 na가 없어서 에러가 남
# x.dropna(subset = x.total_phenols) 
# x.alcalinity_of_ash.fillna(x.alcalinity_of_ash.median(), inplace=True)
import math

print('alcalinity of ash 의 평균값(소수점 이하 절삭):', math.trunc(x.alcalinity_of_ash.mean()))

df = pd.concat([x,y], axis=1)

# Q2: wind dataset에서 alcohol 평균값 이상이고, color_indensity 값이 color_intensity 평균값 이상인 데이터만 남겼을 때, 가장 많은 class 값을 구하시오

print('평균값 이상인 것 중 가장 많은 클래스: class', df[['alcohol', 'class']][(df.alcohol.mean() < df.alcohol)&(df.color_intensity.mean() < df.color_intensity)].value_counts('class').index[0])

# class 1에 해당하는 데이터의 ash 평균값과 wine 데이터셋의 모든 결측치를 제거한 후의 ash 평균값 차이의 절대값을 구하시오...
# 문제풀이 불가...

# Q4. alcohol 변수의 상위 20번째 값 (alcohol을 오름차순 정렬했을 때 상위 20번째 위치한 값) 으로 상위 20개 값을 변환한 후, proanthocyanions가 2 이하인 데이터를 추출하여 alcohol의 평균 값을 계산하시오 (소수점 세번째 자리에서 반올림)

df = df.sort_values(by='alcohol').reset_index(drop=True)

df.alcohol.iloc[1:21] = df.alcohol[20]

print('proanthocyanins 2 이하의  alcohol 평균:', round(df.alcohol[df.proanthocyanins <= 2].mean(), 2))

#Q5. class 1의 데이터 proline 변수의 제 3 사분위 수와 제1 사분위 수의 차이를 구하고, class2도 똑같은걸 구해서 두 값 차이의 절댓값 계산
answer = (df['proline'][df['class'] == 1].quantile(.75) - df['proline'][df['class'] == 1].quantile(.25)) - (df['proline'][df['class'] == 2].quantile(.75) - df['proline'][df['class'] == 2].quantile(.25))

print('절대값 차이:', np.abs(answer))