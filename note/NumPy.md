# NumPy

## 핵심 개념
NumPy(Numerical Python)는 [파이썬](./파이썬.md)의 과학 계산용 핵심 라이브러리이다. 다차원 배열([ndarray](./ndarray.md)) 객체와 이를 효율적으로 처리하는 도구를 제공하며, [통계학](./통계학.md) 및 데이터 분석의 기반이 된다.

## 주요 특징
- **[ndarray](./ndarray.md)**: 동일 타입의 다차원 배열로 빠른 연산 지원
- **브로드캐스팅(Broadcasting)**: 크기가 다른 배열 간 연산 자동 처리
- **벡터화 연산(Vectorization)**: 반복문 없이 배열 전체에 연산 적용
- **메모리 효율성**: C 언어 기반으로 파이썬 리스트보다 빠르고 효율적

## 기본 사용법

```python
import numpy as np

# 배열 생성
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# 배열 생성 함수
zeros = np.zeros((3, 3))      # 0으로 채운 3x3 배열
ones = np.ones((2, 4))        # 1로 채운 2x4 배열
arange = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)  # 0~1 사이 5개 균등 분할

# 배열 속성
print(arr.shape)   # 배열 형태
print(arr.dtype)   # 데이터 타입
print(arr.ndim)    # 차원 수
```

## 통계 함수

```python
data = np.array([1, 2, 3, 4, 5])

# 기술통계
np.mean(data)    # 평균
np.std(data)     # 표준편차
np.var(data)     # 분산
np.median(data)  # 중앙값
np.min(data)     # 최솟값
np.max(data)     # 최댓값
np.sum(data)     # 합계
```

## 배열 연산

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 요소별 연산
print(a + b)      # [5, 7, 9]
print(a * b)      # [4, 10, 18]
print(a ** 2)     # [1, 4, 9]

# 행렬 연산
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(np.dot(A, B))  # 행렬 곱
print(A @ B)         # 행렬 곱 (Python 3.5+)
```

## 인덱싱과 슬라이싱

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr[0, 1])      # 2 (0행 1열)
print(arr[:, 0])      # [1, 4, 7] (모든 행의 0열)
print(arr[1:, :2])    # [[4, 5], [7, 8]] (1행 이후, 2열 이전)

# 조건 인덱싱
print(arr[arr > 5])   # [6, 7, 8, 9]
```

## 참고 자료
- [NumPy 공식 문서](https://numpy.org/doc/stable/)
- [점프 투 파이썬 - NumPy](https://wikidocs.net/14569)
