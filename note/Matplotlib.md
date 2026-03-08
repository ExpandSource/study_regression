# Matplotlib

## 핵심 개념
Matplotlib은 [파이썬](./파이썬.md)의 대표적인 데이터 시각화 라이브러리이다. [NumPy](./NumPy.md) 배열을 기반으로 다양한 그래프를 생성하며, [기술통계](./기술통계.md) 분석 결과를 시각적으로 표현하는 데 필수적이다.

## 주요 구성 요소
- **Figure**: 그래프 전체 영역 (캔버스)
- **Axes**: 실제 그래프가 그려지는 영역
- **pyplot**: MATLAB 스타일의 간편한 인터페이스

## 기본 사용법

```python
import matplotlib.pyplot as plt
import numpy as np

# 기본 선 그래프
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('사인 함수')
plt.xlabel('x축')
plt.ylabel('y축')
plt.show()
```

## 주요 그래프 유형

```python
# 선 그래프 (Line Plot)
plt.plot(x, y, color='blue', linestyle='--', label='sin(x)')

# 산점도 (Scatter Plot)
plt.scatter(x, y, c='red', s=10, alpha=0.5)

# 막대 그래프 (Bar Chart)
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]
plt.bar(categories, values)

# 히스토그램 (Histogram)
data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')

# 박스 플롯 (Box Plot)
plt.boxplot([data1, data2, data3])

# 파이 차트 (Pie Chart)
plt.pie(values, labels=categories, autopct='%1.1f%%')
```

## 그래프 꾸미기

```python
# Figure와 Axes 생성
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y)
ax.set_title('그래프 제목', fontsize=14)
ax.set_xlabel('X축 레이블')
ax.set_ylabel('Y축 레이블')
ax.legend()           # 범례 표시
ax.grid(True)         # 그리드 표시

plt.tight_layout()    # 레이아웃 자동 조정
plt.savefig('graph.png', dpi=300)  # 이미지 저장
plt.show()
```

## 다중 그래프 (Subplots)

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('sin(x)')

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('cos(x)')

axes[1, 0].bar(['A', 'B', 'C'], [10, 20, 15])
axes[1, 1].hist(np.random.randn(500), bins=20)

plt.tight_layout()
plt.show()
```

## 한글 폰트 설정

```python
import matplotlib.pyplot as plt

# Windows
plt.rcParams['font.family'] = 'Malgun Gothic'
# macOS
# plt.rcParams['font.family'] = 'AppleGothic'

plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
```

## 참고 자료
- [Matplotlib 공식 문서](https://matplotlib.org/stable/contents.html)
- [데이터 사이언스 스쿨 - Matplotlib](https://datascienceschool.net/01%20python/05.01%20%EB%A7%B7%ED%94%8C%EB%A1%AF%EB%A6%AC%EB%B8%8C%20%ED%8C%A8%ED%82%A4%EC%A7%80%EC%9D%98%20%EC%86%8C%EA%B0%9C.html)
