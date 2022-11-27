import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

import warnings
warnings.filterwarnings('ignore')

df = sns.load_dataset('penguins')

df.head()

df.info()

# 스키마 정의
# - species: 종

# - island: 섬(서식지)

# - sex: 성별

# - bill_length_mm: 부리의 길이 (mm)

# - bill_depth_mm: 부리의 높이 (mm)

# - flipper_length_mm: 팔 길이

# - body_mass_g:  체중(g) [종속변수, 수치형 변수]

df.describe()
# scale 달라서 scaling 필요

df.columns

df[(df.bill_length_mm.isna()) | (df.bill_depth_mm.isna()) | (df.flipper_length_mm.isna()) | (df.sex.isna()) | (df.body_mass_g.isna())]

# 성별을 몰라서 그냥 dropna!!!
df.dropna(inplace=True)

y = df['body_mass_g']
x = df[['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'sex']]

x.head()

x.info()

x = pd.get_dummies(x, prefix={'species': ' species', 'island':'island', 'sex':'sex'})

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

# train data 스케일링

scaler = StandardScaler()

scaler.fit(X_train[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']])
X_train_scaled = scaler.transform(X_train[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']])
X_test_scaled = scaler.transform(X_test[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']])

X_train_scaled

# 모델
lr = LinearRegression()

lr.fit(X_train_scaled, y_train)

print(lr.intercept_, lr.coef_)

lr_y_pred = lr.predict(X_test_scaled)

len(X_test_scaled)

from sklearn.metrics import r2_score, mean_squared_error
print(f'R2 score : {r2_score(y_test, lr_y_pred)}')
print(f'RMSE : {np.sqrt(mean_squared_error(y_test, lr_y_pred))}')

# 약 82% 설명력을 가진 모델, 평균적으로 378g 차이난다.