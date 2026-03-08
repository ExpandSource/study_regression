# Seaborn 기본 사용법

[Seaborn](seaborn.md)은 [Matplotlib](Matplotlib.md)을 기반으로 한 통계적 데이터 시각화 라이브러리이다. [DataFrame](DataFrame.md)을 직접 사용할 수 있어 [Pandas](Pandas.md)와 궁합이 좋다.

## 기본 설정

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 기본 스타일 설정
sns.set_theme(style="whitegrid")  # 'darkgrid', 'white', 'dark', 'ticks'
```

## 산점도 (Scatter Plot)

```python
# 내장 데이터셋 로드
tips = sns.load_dataset("tips")

# 기본 산점도 - hue로 범주별 색상 구분
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("총 금액 vs 팁")
plt.show()
```

## 회귀선이 포함된 산점도 (regplot)

```python
# [상관계수](상관계수.md) 분석에 유용한 회귀선 포함 산점도
sns.regplot(data=tips, x="total_bill", y="tip", ci=95)  # ci: 신뢰구간
plt.title("회귀선이 포함된 산점도")
plt.show()
```

## 히스토그램 & 분포도 (histplot, kdeplot)

```python
# [히스토그램](히스토그램.md)과 커널 밀도 추정
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(data=tips, x="total_bill", kde=True, ax=axes[0])  # kde: 밀도곡선
axes[0].set_title("히스토그램 + KDE")

sns.kdeplot(data=tips, x="total_bill", hue="sex", ax=axes[1])  # 그룹별 분포
axes[1].set_title("그룹별 밀도 곡선")
plt.show()
```

## 박스플롯 (Box Plot)

```python
# [Box Plot](Box%20Plot.md) - [사분위수](사분위수.md) 및 이상치 확인
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
plt.title("요일별 총 금액 분포")
plt.show()
```

## 히트맵 (Heatmap)

```python
# [상관계수](상관계수.md) 행렬 시각화
numeric_cols = tips.select_dtypes(include='number')
correlation = numeric_cols.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", center=0)
plt.title("상관계수 히트맵")
plt.show()
```

## FacetGrid를 이용한 다차원 시각화

```python
# col, row로 그래프 분할
g = sns.FacetGrid(tips, col="time", row="sex", height=4)
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()
plt.show()
```

## 참조
- [Seaborn Official Documentation](https://seaborn.pydata.org/)
- [Seaborn 기초 - 테디노트](https://teddylee777.github.io/visualization/seaborn/)
