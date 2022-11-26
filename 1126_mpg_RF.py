# Motor Trend Car Road Test
# - target이 미국 생산 차량인지를 구분하는 분류 문제

import numpy as np
import pandas as pd

import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = sns.load_dataset('mpg')

df

df.info()

## 스키마 정의
# -  mpg: 기름 1 갤런당 몇 마일을 주행하는지 연비 정보

# - cylinder: 실린더의 개수

# - deplacement: 배기량

# - horsepower: 마력

# - weight: 무게

# - acceleration: 가속력

# - model_year: 모델의 연식

# - name: 차량명

# - isUSA:미국 생산 여부

# - origin: 생산지?

df.origin.unique()

# isUSA 컬럼이 없으므로 생성해줘야함
df['isUSA'] = 0

df['isUSA'][df.loc[:,'origin'] == 'usa'] = 1

df

df.describe()

sns.displot(df, x=df.horsepower)

sns.boxplot(df.horsepower)

# horsepower의 결측치 대치
# 이상치가 조금 있는 편이므로 중앙값으로 대치

df.horsepower.fillna(df.horsepower.median(), inplace=True)

df.info()

# object(명목형 변수) 제거
df.pop('origin')
df.pop('name')

df

df.iloc[:,:-1]

# target: 미국 생산 차량인가?
y = df['isUSA']
x = df.iloc[:, :-1]

# train - test split, 7:3 으로
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(x).transform(x)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(random_state=42)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

from sklearn.metrics import accuracy_score

print(f'''랜덤포레스트 정확도: , {accuracy_score(y_test, rf_pred)},
''')