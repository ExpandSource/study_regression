# DataFrame

## 핵심 개념
DataFrame은 [Pandas](./Pandas.md)의 핵심 자료구조로, 행(Row)과 열(Column)로 구성된 2차원 테이블 형태의 데이터 구조이다. 각 열은 서로 다른 [데이터 타입](./파이썬%20데이터타입.md)을 가질 수 있으며, [통계학](./통계학.md)적 분석의 기본 단위로 활용된다.

## 주요 구성 요소
- **index**: 행 레이블 (기본값: 0, 1, 2, ...)
- **columns**: 열 이름
- **values**: [ndarray](./ndarray.md) 형태의 실제 데이터

## 특징
- **이질성(Heterogeneous)**: 열마다 다른 데이터 타입 허용
- **레이블 기반 접근**: `loc` (이름), `iloc` (위치)로 데이터 선택
- **SQL 유사 연산**: 조인, 그룹화, 필터링 지원
- **결측치 처리**: NaN 값 탐지 및 처리 기능 내장

## 참고 자료
- [Pandas DataFrame 공식 문서](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
- [데이터 사이언스 스쿨 - DataFrame](https://datascienceschool.net/01%20python/04.02%20%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84.html)

![DataFrame Structure](https://pandas.pydata.org/docs/_images/01_table_dataframe.svg)
