# <b>CHAPTER 2. 데이터 준비 </b>
### <b>index</b>

[1. 데이터 타입](#21-데이터-타입)<br>
    [1.1 데이터 베이스 데이터 타입](#211-데이터-베이스-데이터-타입) <br>
    [1.2 정형 데이터와 반정형 데이터](#212-정형-데이터와-반정형-데이터)<br>
    [1.3 정량 데이터와 정성 데이터](#213-정량-데이터와-정성-데이터) <br>
    [1.4 퍼스트, 세컨드, 서드 파티 데이터](#214-퍼스트-세컨드-서드-파티-데이터)<br>
    [1.5 희소 데이터](#215-희소-데이터)<br>
    
[2. SQL 쿼리 구조](#22-sql-쿼리-구조)<br>
[3. 프로파일링: 데이터 분포](#23-프로파일링-데이터-분포)<br>
    [2.3.1 히스토그램과 빈도](#231-히스토그램과-빈도)<br>
[4. 프로파일링: 데이터 품질](#24-프로파일링-데이터-품질)<br>
[5. 준비: 데이터 정제](#25-준비-데이터-정제)<br>
6. 준비: 데이터 셰이핑
7. 결론


데이터 랭글링: 원본 데이터를 보다 분석하기 쉬운 형태로 가공하는 과정

 ## <b> 2.1 데이터 타입
###  2.1.1. 데이터 베이스 데이터 타입 </b> <br><br>

주요 데이터 타입: 문자열, 숫자, 논리, 날짜/시간

| 타입 | 이름 | 설명 |
| --- | --- | --- | 
| 문자열 |  CHAR / VARCHAR | 문자열 데이터를 저장,<br>CHAR: 고정 길이 값을 저장 <br> VARCHAR: 지정된 범위 내에서 가변 길이 값을 저장 
|    | TEXT, BLOB | VARCHAR의 범위를 넘어서는 긴 문자열 데이터 저장 <br> 설문 응답 등의 텍스트를 저장
| 숫자 | INT / SMALLINT / BIGINT | 정수 데이터 저장, 데이터 베이스에 따라 SMALLINT 또는 BIGINT를 저장하기도 한다
| | FLOAT / DOUBLE / DECIMAL | 실수 데이터 저장
| 논리 | BOOLEAN | True 또는 False 값을 저장
| 날짜/시간 | DATETIME / TIMESTAMP | 날짜 및 시간 데이터를 저장 <br> 기본 형식: <b>YYYY-MM-DD hh:mi:ss <b>
| | TIME | 시간 데이터를 저장

- DECIMAL은 소수점 위치를 표시
- INT 타입은 DECIMAL보다 메로리를 적게 사용
- 이외에도 JSON이나 지리 타입 등의 데이터 타입이 존재

<br>
<br>

### <b>2.1.2 정형 데이터와 반정형 데이터 </b> 
<br>
<li> 정형 데이터: 각 속성이 열에 저장되고 개체가 행에 저장되는 행렬 형태의 데이터
- 각 필드는 지정된 데이터 타입에 맞는 데이터만 저장할 수 있다.
<br>
<Li> 비정형 데이터: 미리 지정된 구조, 데이터 모델, 데이터 타입이 없음. <br>
e.g. 사진, 이미지, 비디오 오디오 등 <br>
관계형 데이터베이스에 효율적으로 저장하기 어려우며 SQL로 쿼리를 수행하기도 알맞지 않음
<br>
<li> 반정형 데이터: 나름의 구조를 갖춘 비정형 데이터

<br>
<br>

### <b>2.1.3 정량 데이터와 정성 데이터 </b>
<br>
<li> 정량 데이터: 사람, 물건, 이벤트 등을 특정 수치로 정량화한 데이터 -> 숫자 타입의 정보를 저장할 수 있다. <br>
<li> 정성 데이터: 주로 텍스트 형태로 적힌 느낌, 의견, 서술과 같이 명확한 수치로 측정할 수 없는 데이터 
</li>
<br>
<br>

### <b>2.1.4  퍼스트, 세컨드, 서드 파티 데이터 </b>

| 구분 | 설명 | 예시 |
| -- | -- | -- |
| 퍼스트 파티 데이터 | 기관에서 직접 수집한 데이터 | 서버로그, 고객 정보, 거래 데이터 등|
| 세컨드 파티 데이터  | 특정 기관에 서비스를 제공하는 업체에서 수집하는 데이터 | 주로 CRM, 이메일, 자동화 도구 등에 사용되는 SaaS 형태로 제공되는 상품 등 | 
| 서드 파티 데이터 | 어디선가 무료로 얻는 데이터 | 금액을 지불하고 구매하는 데이터, 정부에서 무료로 공개한 데이터 등|
- 서드 파티 데이터는 조직 내부에서 수집하는 데이터가 아니므로 데이터 팀이 데이터 생성 및 수집 과정에 참여해 데이터 형식 수집 주기, 품질 등을 조정할 수 없음


<br>
<br>

### <b>2.1.5 희소 데이터</b>
- 희소 데이터 saparse data: 빈 값이나 중요하지 않은 정보가 많이 포함돼 크기에 비해 의미 있는 정보가 적은 데이터 셋
- 가공 방법: 
    1. 자주 발생하지 않는 이벤트를 더 자주 발생하는 이벤트의 하위로 묶거나
    2. 희소 데이터를 삭제하거나
    3. 희소 데이터가 많이 발생하는 시간대 등을 분석하여 분석에서 제외하는 방법 등이 있다.

## <b> 2.2 SQL 쿼리 구조 </b>
- SELECT : 쿼리를 통해 어느 절을 가져올 것인지 결정
- FROM : SELECT 절에서 언급한 컬럼을 어떤 테이블에서 가져올 것인지 결정, 여러 테이블을 참조하기 위한 JOIN 을 수행
    - INNER JOIN: 두 테이블에서 상응하는 모든 레코드를 가져옴
    - LEFT JOIN: 첫 번째 테이블의 레코드를 모두 가져오고, 두 번째 테이블에서는 첫 번째 테이블과 상응하는 레코드만 가져옴
    - FULL OUTER JOIN:  두 테이블에서 조건에 맞는 레코드를 모두 가져옴
    - 카티션 JOIN: 명시된 조건으로 첫 번째 테이블의 각 레코드가 두 번째 테이블의 여러 레코드와 일치하는 경우에 발생 -> 의도적으로 시계열 분석에서 날짜 데이터를 채워 넣는 등 <b>특수한 목적이 있을 때가 아니면 사용하지 않는다.</b>
- WHERE: SELECT 절을 통해 가져올 컬럼의 조건을 설정
- GROUP BY: 주로 SELECT 절에서 특정 필드를 그룹화하고 그룹별 집계를 수행하기 위해 사용
    - 집계를 수행할 필드와 집계에 사용되지 않는 필드가 최소한 하나씩 있어야 합니다.

<br>
<b> 데이터 베이스를 죽이지 않는 방법: LIMIT와 샘플링 </b> 

``` SQL
데이터 베이스에서 불러올 정보가 너무 많은 경우, 오류가 나거나 DB가 죽어버릴 수 있다. 이를 방지하기 위해서는 프로파일링, LIMIT 또는 샘플링을 이용해 반환할 쿼리의 수를 제한하는 방법을 사용하는 것이 좋다.


1. LIMIT
LIMIT 절은 쿼리의 맨 마지막에서 제한할 레코드의 개수를 제한할 수 있다.
SELECT col1, col2
FROM table
LIMIT 100 -- 100개 행으로 출력 레코드 수 제한

2. 샘플링
- 나눗셈의 나머지 (MOD) 함수를 이용한 샘플링
- WHERE절의 조건을 이용한 (e.g. 필드의 마지막 글자를 활용 등)
```


## <b>2.3 프로파일링: 데이터 분포</b>
스키마와 테이블을 통해 데이터가 어떻게 저장되어있는 지 파악

### <b> 2.3.1 히스토그램과 빈도 </b>
- 프로파일링 하기 위한 필드를 GROUP BY 절로 지정하고, count(*)를 통해 필드 내에서 각 값의 개수를 알아냄

``` SQL
SELECT fruit, count(*) as qty
FROM fruit_inventory
GROUP BY 1 -- 과일별로 grouping
;
```
💡 count함수를 사용할 때에는 데이터셋에 중복되는 레코드가 있는지 잘 알아봐야 한다. 전체 레코드, 수를 알고싶다면 count(*)를 사용해도 좋지만, 중복되지 않는 고유한 필드의 수를 세고 싶다면 count distinct를 사용해야 함

- 빈도 그림: 데이터셋에 존재하는 값의 빈도를 시각화하는 방법

- 주문 개수 별 고객 분포
    - 서브쿼리에서 count를 사용한 customer_id 에 대한 주문 수 파악
    - 이 서브쿼리에서 나온 주문 수 orders를 카테고리로 삼고 count를 사용해 주문 개술 별 고객의 수를 집계
```SQL
SELECT orders, count(*) as num_customers
FROM(
    SELECT customer_id, count(order_id) as orders
    FROM orders
    GROUP BY 1
) a
GROUP BY 1
;
```

### <b>2.3.2 구간화</b>
- 연속값을 프로파일링 할 때 유용
- 값의 범위를 기준으로 먼저 그룹핑
- CASE문, 반올림, 로그 등을 사용하여 간단히 수행 <br>

<b> CASE문 syntax </b>

```SQL
CASE WHEN condition1 THEN return_value_1
    WHEN condition2 THEN return_value_2
    ...
    ELSE return_value_default
    END
```
💡 하나의 CASE 문에서 THEN의 모든 반환값은 데이터 타입이 같아야 하며, 그렇지 않으면 오류가 발생. 만약 이 문제로 오류가 발생하면 반환값의 데이터 타입을 문자열 등의 일반 데이터 타입으로 캐스팅하여 해결 <br>

** 데이터에서 매우 작거나 매우 큰 값으로 인해 그래프의 꼬리 한쪽이 길게 늘어진 모양이 나올 때, 모든 값의 개수를 확인하기보다 구간화를 활용하는 편이 좋음.

<br>
 e.g. 기업의 주문량에 따라 운송비 할인율을 다르게 적용하는 상황을 가정하여 주문량을 기준으로 기업을 나누고 주문량 구간별 기업 수를 파악

 ```SQL
 SELECT 
    CASE WHEN order_amount <= 100 THEN 'up to 100'
        WHEN order_amount <= 500, THEN '100 - 500'
        ELSE 500 + END as amount_bin
    , CASE WHEN order_amount <= 100 THEN 'small'
        WHEN order_amount <= 500 THEN 'medium'
        ELSE 'large' END as amount_category
    , COUNT(customer_id) as customers
    FROM orders
    GROUP BY 1,2

 ```

- 구간 범위 설정에 로그를 사용하기도 합니다. => 데이터셋에서 가장 작은 값과 큰 값들의 차이가 매우 큰 경우에 유용 (e.g. 가계 자산 분포, 인터넷 속성에 따른 웹사이트 방문자 분포 등)

| 형식 | 결과 |
| -- | -- |
|log(1) | 0 |
| log(10) | 1 |
| log(100) | 2 |
| log(1000) | 3 |

LOG 함수는 인자의 로그 값을 반환하며, 인자에는 상숫값이나 필드를 지정
```SQL
SELECT log(sales) as bin,
    count(customer_id) as customers
FROM table
GROUP BY 1
;
```

- log함수의 인자로 10의 배수가 아닌 다른 숫자를 사용할 수도 있지만, 0 이하의 값을 사용하면 데이터베이스에 따라 null을 반환하거나 오류가 날 수 있으므로 주의


### <b> 2.3.3 N분위수</b>

### 1. 윈도우 함수
윈도우 함수: 여러 행에 걸친 계산을 수행<br>
함수 이름 + OVER 절로 구성 <br>
OVER 절은 연산을 수행하고 정렬할 필드를 선택
```SQL
function(필드명) OVER(PARTITON BY 필드명 ORDER BY 필드명)
```
- 함수로는 일반 집계 함수 뿐만 아니라 rank, first_value, ntile 등도 상용 가능
- PARTITION BY 절은 필요하지 않다면 생략 가능: 명시하지 않을 경우 전체 테이블에 대해 연산 수행
- ORDER BY 절에 명시된 필드를 기준으로 정렬

```SQL
ntile(num_bins) OVER (PARTITION BY ... ORDER BY...)
```
나누고 싶은 구간의 개수를 인자로 받아 데이터를 나눔

```SQL
SELECT ntile
, min(order_amount) as lower_bound
, max(order_amount) as upper_bound
, count(order_id) as orders
FROM
    (SELECT customer_id, order_id, order_amount
    , ntile(10) OVER (ORDER BY order_amount) as ntile
    FROM orders
    ) a
GROUP BY 1
;
```
- 각 행의 N분위 수 값을 계산하고 min, max 함수를 통해 구간별 범위를 확인할 수 있다.

- 유사한 기능을 할 수 있는 함수: percent_rank
- 다만, ntile과 percent_rank 모두 계산을 위해 행 정렬이 들어가느라 연산이 많으므로, 대용량 데이터 처리에서는 적합하지 않음


<br> <br>

## <b>2.4  프로파일링: 데이터 품질 </b>
가능하다면 데이터를 실제 검증 자료와 비교해 보는 것이 가장 좋음
<br>
프로파일링을 통해 null, 검토해야 할 카테고리 분류, 처리가 필요한 값이 여러 개인 개인 필드, 일반적이지 않은 날짜/시간 형식을 탐색

### <b> 2.4.1 중복 탐지 </b>

중복이 발생하는 대표적인 이유
- 휴먼 에러
- 데이터 삽입 코드를 두 번 실행
- 데이터 처리 단계에서 코드를 여러 번 실행(다대다 JOIN 등)

<br> 중복을 찾아내는 여러 가지 방법
1. cartition Join 으로 가능한 경우의 수를 모두 본다 -> 모든 행을 봐야하므로 일이 좀 커짐
2. SELECT와 count 함수를 사용한 개수 체크 <br>
기본적인 컨셉은 확인하고자 하는 컬럼을 그룹핑하여 그 개수를 카운트, 1개 초과인 중복 데이터를 탐색 <br>

* Query 1 (subquery)
```SQL
SELECT records, count(*)
FROM (
    SELECT col_a, col_b, col_c, .. , count(*) as records
    FROM table
    GROUP BY 1,2,3 ...
) a
WHERE records > 1
GROUP BY 1
```
- Query 2 (grouping + having)

```SQL
SELECT col_a, col_b, col_c, ... , count(*) as records
FROM table
GROUP BY 1,2,3, ... 
HAVING records > 1
```

### <b> 2.4.2 중복 제거 </b>
- 거래 이력이 있는 고객 모두에게 다음 주문 시 사용 가능한 쿠폰을 보낸다고 가정해보자. 우선, customer 테이블과 transaction 테이블에 JOIN을 수행해 거래 내역이 있는 고객 리스트를 추출
```SQL
SELECT c.customer_id, c.customer_name, c.customer_email
FROM customer as c
JOIN transaction as t ON c.customer_id = t.customer_id
;
```
<b> 여러 번의 거래 기록이 있는 경우 중복 데이터가 나타나게 됨, 세 가지 방법을 이용해 중복 제거 가능</b>
- DISTINCT 사용
- GROUP BY 를 사용한 unique 값 조회
- 집계함수 (min, max)를 사용

<br> <br>
## <b> 2.5 준비: 데이터 정제</b>
<br>
CASE 변환, null처리, 데이터 타입 변환 등
<br> <br>

### **2.5.1 CASE 문** <br>
데이터의 표준화, 구간화 등에 사용 <br>
e.g. NPS (순수 추천 고객 지수) 구하기
```SQL
SELECT reposnse_id , likelihood
, CASE WHEN likelihood <= 6 THEN 'Detractor'
    WHEN likelihood <= 8 THEN 'Passive'
    ELSE 'Promoter'
    END as reponse_type
FROM nps_reponses
```
또는 <b>IN</b> 연산자를 이용해 카테고리 값을 직접 지정해 줄 수 있다.
```SQL
CASE WHEN likelihood in (0,1,2,3,4,5,6) THEN 'Detractor'
    WHEN likelihood in (7,8) THEN 'Passive'
    WHEN likelihood in (9,10) THEN 'Promoter'
    END as reponse_type
```

<br>
동시에 여러 절에 조건을 걸 때에는 AND 또는 OR 연산자로 연결해 줄 수 있다.

```SQL
CASE WHEN likelihood <= 6
        AND country = 'US'
        AND high_value = true
        THEN 'US high value detractor'
    WHEN likelihood >= 9
        AND (country in ('CA', 'JP) 
            or high_value = true)
        THEN 'some other label'
    ...
    END
```

**룩업 테이블을 활용한 데이터 정제**
> 해당 필드에 어떤 데이터가 있는지 알 때, 데이터의 분산이 크지 않으며 값이 변경될 일이 없다고 확신한다면 데이터 정제나 보강에 CASE 문을 사용할 수 있지만, 필드에 저장된 데이터의 분산이 크고 값이 자주 바뀔 수 있는 경우에는 룩업 테이블을 사용하는 편이 낫다.
- 룩업 테이블: 키-값 쌍으로 정의<br>
별도의 코드를 주기적으로 실행해 키-값 쌍에 새로운 값을 추가할 수 있으며, 쿼리를 수행할 때 룩업 테이블에 별도의 JOIN을 수행하여 정제된 데이터를 가져올 수도 있음

**플래그의 표시** <Br>

``` SQL
SELECT customer_id,
    CASE WHEN gender = 'F' THEN 1 ELSE 0 END as is_female,
    CASE WHEN likelihood in (9,10) THEN 1 ELSE 0 END as is_promoter
 FROM ... 
```
> 이외에도... 
- 특정 속성에 대해서 레이블링 할 때
- 임계값 또는 양을 설정하여 레이블링 할 때

<br><br>

### **2.5.2 타입 변환과 캐스팅**
**데이터타입 변경의 두 가지 방법**

1) CAST(데이터 타입) <br>
```SQL
e.g. CAST(1234 as varchar),
    CAST(CONCAT(year, '-', month, '-', day) as date) =>문자열로 반환,
    DATE(CONCAT(year, '-', month, '-', day)) => DATE 타입으로 바로 변환
```
2) 더블 콜론(::)의 사용: input :: 데이터 타입 <br>
```
e.g. 1234::varchar
```

**to_데이터 타입 함수**
| 함수 | 사용 목적 |
| -- | -- |
| to_char | 데이터 타입을 문자열 타입으로 변환 | 
| to_number | 데이터 타입을 숫자 타입으로 변환 | 
| to_date | 데이터 타입을 date 타입으로 변환(날짜 부분 명시) |
| to_timestamp | 데이터 타입을 TIMESTAMP 타입으로 변환(날짜 부분 명시) |

<br><br>
### **2.5.3 null값 다루기**
**null?** 해당 필드에 아무 데이터도 수집되지 않았거나 해당 필드에서 필요 없는 값을 의미
<br> <br>
### **null 처리법**
1) CASE문의 사용
``` SQL
e.g. CASE WHEN num_orders IS NULL THEN 0 ELSE num_orders END
    CASE WHEN address IS NULL THEN 'Unknown' ELSE address END
```

2) COALESCE : 인자를 두 개 이상 받아서 그 중 null이 아닌 첫 번째 값을 반환
```SQL
e.g. COALESCE(num_orders, 0)
```
cf:  일부 데이터 베이스는 coalesce 함수와 비슷한 기능을 하지만 인자를 두 개만 받는 nvl 함수를 지원

3) nullif : 두 숫자를 비교해서 서로 같지 않으면 첫 번재 숫자를 반환하고, 같으면 null을 반환 <br>
특정 필드의 기본값이 무엇인지 알고 있으며, 이것을 null로 바꾸고 싶을 때 유용
```SQL
nullif(6,7) -> 두 숫자가 같지 않으므로 6을 반환
nullif(6,6) -> 두 숫자가 같으므로 null을 반환
```
CASE문으로도 표현 가능
``` SQL
CASE WHEN 6 = 7 THEN 6
    WHEN 6 = 6 THEN null
    END
```

> **WHERE절에서 데이터를 필터링할 때 null이 문제가 될 수 있음** <br>
case) 어떤 필드가 과일이름과 null을 동시에 저장하고 있을 때 'apple'이 아닌 값을 반화받고 싶다면 아래의 쿼리를 수행하게 될 것이다. <br>
**WHERE my_field <> 'apple'** <br>
그러나 일부 데이터 베이스는 위 문장을 실행하게 되면, null도 함께 반환할 수 있다. 따라서 둘 다 필터링 하기 위해서는 **or** 조건을 사용하여 'apple'과 'null' 명시적으로 조건 설정해야한다.
**WHERE my_field <> 'apple' or my_field is null**


<br> <br>
### **2.5.4 결측데이터**
<br>

**결측치가 발생하는 이유**
- 사용자가 정보를 입력하지 않음
- 코드의 버그
- 옮기는 과정에서의 human error
- 데이터 수집 방법의 변경 등에 따른 결측
- 중간에 새로운 필드를 추가했을 때 이전의 정보는 null로 채워짐
- 테이블이 다른 테이블의 값을 참조하는 상황에서 다른 테이블이 DW에 로드 되지 않아 연결된 데이터를 찾을 수 없는 케이스 

**결측치를 찾아내는 법**
- 히스토그램, 빈도 분석 등을 통한 데이터 프로파일링
- 두 테이블 값을 비교
```SQL
거래 내역이 저장된 transaction 테이블에 고객 ID가 있다면, 해당 고객의 정보는 customer 테이블에 저장되어 있을 것으로 예상한다. 두 테이블에 LEFT JOIN과 WHERE절을 사용해 customer 테이블에 정보가 저장되지 않은 고객의 ID를 찾는다.

SELECT distinct t.customer_id
FROM transactions t
LEFT JOIN customers c on t.customer_id = c.customer_id
WHERE c.customer_id is null
;
```

**결측치는 모두 오류?** <br>
결측 데이터는 그 자체로 의미를 지닐 수 있으므로, 무조건 결측 데이터가 없도록 만들거나 다른 값으로 채워서는 안 된다. 결측 데이터를 통해 근복적인 시스템 설계 문제 또는 데이터 수집 과정 내의 문제를 찾아내기도 한다.
<br>
<br>
**결측치 대체** <br>
평균, 중앙값 또는 바로 이전에 저장된 값 등으로 대체할 수 있다.<br>
결측값을 다른 값으로 대체하면 앞으로 수행할 데이터 분석의 결과도 계속 달라질 수 있으므로, 결측값이 무엇이며, 어떤 값으로 대체했는지를 문서화 해야함.
<br><br>
1) 상수값으로 채우기 <br>
'xyz' 상품의 값이 20달러라는 것을 안다면 20을 채워넣으면 된다. (CASE문 사용)
``` SQL
CASE WHEN price is null and item_name = 'xyz' THEN 20 ELSE price END
```
2) 수리 함수나 CASE문을 사용해 생성한 값으로 결측값 채우기
