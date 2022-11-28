# 교재 260p 1~5번 문항 (작업형 1유형)

from sklearn.datasets import load_iris

import numpy as np
import pandas as pd
import seaborn as sns

import warnings

warnings.filterwarnings('ignore')

load_iris()

x = pd.DataFrame(load_iris().data, columns=load_iris().feature_names)
y = pd.Series(load_iris().target)

y
# 0: setosa
# 1: versicolor
# 2: virginica

x.info()

x.describe()

# Q1. iris dataset에서 species 변수 값별로 petal_width 상워 25% 값을 구한 후, 가장 큰 값과 가장 작은 값 사이의 차이를 계산하시오.

iris = pd.concat([x,y], axis=1)

iris.rename(columns={0:'species'}, inplace=True)

# 0: setosa
# 1: versicolor
# 2: virginica
iris['species'][iris.species == 0] = 'setosa'
iris['species'][iris.species == 1] = 'versicolor'
iris['species'][iris.species == 2] = 'virginica'

iris

print('petal_width 최대값과 최소값의 차이: ', iris.groupby('species').quantile(.25)['petal width (cm)'].max() - iris.groupby('species').quantile(.25)['petal width (cm)'].min())

# Q2. iris dataset에서 sepal_length 변수의 전체 값들을 중복 없이 리스트로 만든 후, 오름차순으로 정렬했을 때 리스트의 10번째에 오는 숫자를 계산하시오.
lst = iris['sepal length (cm)'].to_list()
lst.sort()

list(set(lst))[10]

print('리스트에서 10번째 오는 숫자:', list(set(lst))[10])

# Q3. iris dataset sepal_width 변수 값으로 내림차순 한 후, 위에서부터 100개 행을 학습데이터로 분리하고, 학습데이터에서 sepal_width의 표준편차 값을 구한 후 50을 곱한 값을 계산, 최종 계산 값의 소수점 이하는 버림

train_x = iris.sort_values(by='sepal width (cm)').iloc[:100].reset_index()

import math
print(math.trunc(train_x['sepal width (cm)'].std() * 50))

# Q4. iris dataset, species 변수값별로 petal_length 상위 10개 행의 평균값을 구한 후, 평균값의 합을 구하시오 (소수점 이하 반올림)

round(iris.groupby('species').mean()['petal length (cm)'].sum())

# Q5. iris dataset sepal_length의 변수가 이상치를 가지는 데이터 행수를 계산하시오

col = iris['sepal length (cm)']

print('이상치의 개수: ', len(iris[(col.mean() + 2 * col.std() < col) | (col.mean() - 2 * col.std() > col)]))

# iris['sepal length (cm)'].mean() + 2 * iris['sepal length (cm)'].std() > 

# (iris['sepal length (cm)'].quantile(0.75) < iris['sepal length (cm)']).sum()