# **Chapter3. 시계열 분석** 
[1. 날짜 및 시간 데이터 조작](#)
    [1.1 시간대 변환](#)
    [1.2 날짜 및 타임스태프 형식 변환](#)
    [1.3 날짜 계산](#)
    [1.4 시간 계산](#)
    [1.5 서로 다른 출처의 날짜 합치기](#)

[2. 데이터셋: 소매업 매출](#)
[3. 데이터 트렌드 분석](#)
    [3.1 간단한 트렌드](#)
    [3.2 요소 비교](#)
    [3.3 전체 대비 비율 계산](#)
    [3.4 인덱싱으로 시계열 데이터 변화 이해하기](#)

<br>

## 시계열 데이터의 분석
> 시계열 데이터: 시간 순으로 재정렬된 데이터의 배열, 데이터는 주로 일정한 시간 간격을 두고 저장돼있다.

예측은 시계열 분석의 주요 목표 중 하나이다. 과거의 값으로 미래의 값을 예측하며, 시장 상황과 대중 트렌드, 제품 도입 시기 등 다양한 형태로 분석하고 있다. 

<br>

## **3.1 날짜 및 시간 데이터 조작**
DATE, DATETIME 형식을 다루는 방법, interval 개념을 사용한 날짜 계산과 시간 조작, JOIN을 수행할 때나 출처가 다른 여러 데이터들을 조합할 때 고려해야할 주의사항 등

<br>

### **3.1.1. 시간대 변환**
데이터베이스의 타임스탬프는 대체로 UTC(협정 세계시)를 사용하지만 아주 간혹 그리니치 평균시(GMT) 등을 사용하는 경우가 있다...  

- 데이터베이스에서 타임스탬프는 `YYYY-MM-DD hh:mi:ss` 형태로 저장

**주요 데이터베이스의 시간대 정보 시스템 테이블**
데이터베이스 | 시스템테이블
--- | ---
Postgres | pg.timezone_names
MySQL | mysql.time_zone_names
SQL Server | sys.time_zone_info
Redshift | pg_timezone_names

### **3.1.2. 날짜 및 타임스탬프 형식 변환**
- current date: 현재 날짜 반환
``` SQL
SELECT current_date;
```
외에도 여러 가지 함수 지원  
- current_timestamp
- localtimestamp
- get_date()
- now() ...

**시간 단위 절삭**
- date_trunc
```SQL
SELECT date_trunc('month', '2020-10-04 12:33:35' ::timestamp);

date_trunc
-------------------
2020-10-01 00:00:00
```
- date_trunc 미지원시 date_format에서도 비슷한 작업 수행 가능
```SQL
SELECT date_format('2020-10-04 12:33:35', '%Y-%m-01') as date_trunc

date_trunc
-------------------
2020-10-01 00:00:00
```

**날짜 또는 타임스탬프 값 추출**
- 시간 값 반환이 필요한 경우를 제외하고 `DATE`타입과 `TIMESTAMP`타입은 서로 변환 가능
- date_part, extract 함수를 통해 시간 단위 값을 반환할 수 있음 (반환 타입:FLOAT)
```SQL
-- date_part 사용
SELECT date_part('day', current_timestamp),
SELECT date_part('month', current_timestamp),
SELECT date_part('hour', current_timestamp) 

-- extract 사용
SELECT extract('day' from current_timestamp);
extract
-------
27.0

SELECT extract('month' from current_timestamp);
extract
-------
5.0

-- interval과 함께 사용
-- interval 이후 단위의 값을 실수로 반환
-- 단위는 반드시 맞춰줘야 함! 일 별은 일별로, 월 별은 월별로
SELECT date_part('day', interval '30 days');
date_part
---------
30.0
```

- to_char: 첫 번째 인자에서 두 번째 인자에 해당하는 부분의 이름을 가져옴
```SQL
SELECT to_char(current_timestamp, 'Day');
to_char
--------
Monday
```
- 날짜 및 시간 이어붙이기
``` SQL
SELECT date '2020-09-01' _ time '03:00:00' as timestamp;
timestamp
-------------------
2020-09-01 03:00:00
```
