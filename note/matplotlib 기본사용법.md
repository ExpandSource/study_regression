# Matplotlib 기본사용법

[Matplotlib](../개념노트/Matplotlib.md)는 [Python](../개념노트/파이썬.md)에서 데이터 시각화를 위한 기본 라이브러리이다. [산점도](../개념노트/산점도%20scatter%20plot.md), [히스토그램](../개념노트/히스토그램.md), [Box Plot](../개념노트/Box%20Plot.md) 등 다양한 그래프를 생성할 수 있다.

## 기본 설정

```python
import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (한글 깨짐 방지)
plt.rcParams['font.family'] = 'AppleGothic'  # Mac
# plt.rcParams['font.family'] = 'Malgun Gothic'  # Windows
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지
```

## 선 그래프 (Line Plot)

```python
# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.title('사인 함수 그래프')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()  # 범례 표시
plt.grid(True)  # 격자 표시
plt.show()
```

## 산점도 (Scatter Plot)

```python
# [상관계수](../개념노트/상관계수.md) 분석을 위한 산점도
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

plt.figure(figsize=(8, 6))
plt.scatter(x, y, alpha=0.6, s=50)  # alpha: 투명도, s: 점 크기
plt.title('산점도 예시')
plt.xlabel('변수 X')
plt.ylabel('변수 Y')
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)  # 수평선
plt.axvline(x=0, color='gray', linestyle='--', linewidth=0.5)  # 수직선
plt.show()
```

## 히스토그램 (Histogram)

```python
# [기술통계](../개념노트/기술통계.md)의 [분산](../개념노트/분산%20(통계학).md) 시각화
data = np.random.normal(100, 15, 1000)  # 평균 100, 표준편차 15

plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
plt.title('정규분포 히스토그램')
plt.xlabel('값')
plt.ylabel('빈도')
plt.axvline(data.mean(), color='red', linestyle='--', label=f'평균: {data.mean():.2f}')
plt.legend()
plt.show()
```

## 서브플롯 (Subplots)

```python
# 여러 그래프를 한 화면에 배치
fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2x2 그리드

# 각 서브플롯에 그래프 그리기
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Sin')

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title('Cos')

axes[1, 0].scatter(x, y)
axes[1, 0].set_title('Scatter')

axes[1, 1].hist(data, bins=20)
axes[1, 1].set_title('Histogram')

plt.tight_layout()  # 레이아웃 자동 조정
plt.show()
```

## 스타일 적용

```python
# 미리 정의된 스타일 사용
plt.style.use('seaborn-v0_8')  # 또는 'ggplot', 'fivethirtyeight' 등
plt.plot(x, y)
plt.show()
```

## 참조
- [Matplotlib Official Documentation](https://matplotlib.org/stable/index.html)
- [Matplotlib 튜토리얼 - 데이터 사이언스 스쿨](https://datascienceschool.net/01%20python/05.02%20%EB%A7%B7%ED%94%8C%EB%A1%AF%EB%A6%AC%EB%B8%8C%20%EC%82%AC%EC%9A%A9%EB%B2%95.html)
