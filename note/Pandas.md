# Pandas

## 핵심 개념
Pandas는 [파이썬](./파이썬.md)의 데이터 분석 및 조작 라이브러리이다. [NumPy](./NumPy.md) 기반으로 구축되었으며, 테이블 형태의 데이터를 효율적으로 처리한다. [통계학](./통계학.md)적 분석과 데이터 전처리의 핵심 도구이다.

## 주요 자료구조
- **Series**: 1차원 레이블 배열 (인덱스 + 값)
- **[DataFrame](./DataFrame.md)**: 2차원 테이블 구조 (행과 열로 구성)

## 기본 사용법

```python
import pandas as pd
import numpy as np

# Series 생성
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# DataFrame 생성
df = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '나이': [25, 30, 35],
    '점수': [85, 92, 78]
})

# 파일에서 읽기
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
```

## 데이터 탐색

```python
df.head()        # 상위 5행
df.tail()        # 하위 5행
df.shape         # (행 수, 열 수)
df.info()        # 데이터 타입 및 결측치 정보
df.describe()    # 기술통계 요약
df.columns       # 열 이름 목록
df.dtypes        # 각 열의 데이터 타입
```

## 데이터 선택 및 필터링

```python
# 열 선택
df['이름']              # 단일 열 (Series)
df[['이름', '나이']]    # 복수 열 (DataFrame)

# 행 선택
df.loc[0]               # 레이블 기반 인덱싱
df.iloc[0]              # 정수 위치 기반 인덱싱
df.loc[0:2, '이름':'점수']  # 범위 선택

# 조건 필터링
df[df['나이'] > 25]
df[(df['나이'] > 25) & (df['점수'] >= 80)]
```

## 데이터 조작

```python
# 열 추가/수정
df['합격'] = df['점수'] >= 80

# 결측치 처리
df.dropna()              # 결측치 행 제거
df.fillna(0)             # 결측치를 0으로 대체

# 정렬
df.sort_values('나이', ascending=False)

# 그룹화 및 집계
df.groupby('합격')['점수'].mean()
```

## 통계 함수

```python
df['점수'].mean()      # 평균
df['점수'].std()       # 표준편차
df['점수'].var()       # 분산
df['점수'].median()    # 중앙값
df['점수'].value_counts()  # 빈도수
df.corr()              # 상관계수 행렬
```

## 참고 자료
- [Pandas 공식 문서](https://pandas.pydata.org/docs/)
- [데이터 사이언스 스쿨 - Pandas](https://datascienceschool.net/01%20python/04.01%20%ED%8C%90%EB%8B%A4%EC%8A%A4%20%ED%8C%A8%ED%82%A4%EC%A7%80%EC%9D%98%20%EC%86%8C%EA%B0%9C.html)
