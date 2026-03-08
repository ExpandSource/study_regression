# ndarray

## 핵심 개념
ndarray(N-dimensional Array)는 [NumPy](./NumPy.md)의 핵심 자료구조로, 동일 타입의 요소를 가진 다차원 배열이다. [벡터](./벡터.md)(1차원)와 행렬(2차원) 연산을 효율적으로 처리하며, [Pandas](./Pandas.md)의 [DataFrame](./DataFrame.md) 기반이 된다.

## 주요 속성
- **shape**: 배열의 형태 (예: `(3, 4)` = 3행 4열)
- **dtype**: 요소의 데이터 타입 (int64, float64 등)
- **ndim**: 차원 수
- **size**: 전체 요소 개수

## 특징
- **동질성(Homogeneous)**: 모든 요소가 동일한 데이터 타입
- **벡터화 연산**: 반복문 없이 배열 전체에 연산 적용
- **브로드캐스팅**: 크기가 다른 배열 간 자동 연산 확장
- **메모리 효율성**: C 기반으로 [파이썬](./파이썬.md) 리스트보다 빠름

## 참고 자료
- [NumPy ndarray 공식 문서](https://numpy.org/doc/stable/reference/arrays.ndarray.html)
- [점프 투 파이썬 - ndarray](https://wikidocs.net/14569)

![ndarray Structure](https://numpy.org/doc/stable/_images/np_array.png)
