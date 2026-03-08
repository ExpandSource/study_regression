# SciPy

SciPy(Scientific Python)는 [파이썬](./파이썬.md) 기반의 과학 계산 라이브러리이다. [NumPy](./NumPy.md)를 기반으로 구축되어 고급 수학 함수, 통계, 최적화, 신호 처리 등의 기능을 제공한다.

## 주요 모듈

| 모듈                  | 기능                                                 |
| ------------------- | -------------------------------------------------- |
| `scipy.stats`       | 확률 [분포](./분포%20(통계학).md), 통계 검정, [기술통계](./기술통계.md) |
| `scipy.optimize`    | 최적화, 곡선 적합(curve fitting)                          |
| `scipy.linalg`      | 선형대수 연산                                            |
| `scipy.interpolate` | 보간법(interpolation)                                 |
| `scipy.integrate`   | 수치 적분                                              |

## 통계 분석 예시

```python
from scipy import stats
import numpy as np

# 정규성 검정 (Shapiro-Wilk)
data = np.random.normal(0, 1, 100)
stat, p_value = stats.shapiro(data)
print(f"통계량: {stat:.4f}, p-value: {p_value:.4f}")

# 정규분포 객체 생성
norm_dist = stats.norm(loc=0, scale=1)  # 평균=0, 표준편차=1
print(f"P(X < 1.96): {norm_dist.cdf(1.96):.4f}")

# t-검정 (두 집단 평균 비교)
group1 = np.random.normal(10, 2, 50)
group2 = np.random.normal(11, 2, 50)
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t-statistic: {t_stat:.4f}, p-value: {p_value:.4f}")

# 상관계수 계산
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])
r, p = stats.pearsonr(x, y)  # Pearson 상관계수
rho, p = stats.spearmanr(x, y)  # Spearman 순위 상관계수
```

## 확률분포 활용

```python
from scipy import stats

# 다양한 분포 객체
normal = stats.norm(loc=0, scale=1)      # 정규분포
t_dist = stats.t(df=10)                   # t-분포 (자유도=10)
chi2 = stats.chi2(df=5)                   # 카이제곱분포

# 분포 메서드
normal.pdf(0)      # 확률밀도함수 (Probability Density Function)
normal.cdf(1.96)   # 누적분포함수 (Cumulative Distribution Function)
normal.ppf(0.975)  # 분위수 함수 (Percent Point Function, CDF의 역함수)
normal.rvs(100)    # 난수 생성 (Random Variates)
```

## NumPy vs SciPy

[NumPy](./NumPy.md)는 배열 연산과 기본 수학 함수를 제공하고, SciPy는 이를 확장하여 과학 계산에 필요한 고급 알고리즘을 제공한다. [추론통계](./추론통계.md)의 가설 검정, [Shapiro-Wilk 검정](./Shapiro-Wilk%20검정.md) 등은 SciPy의 `stats` 모듈에서 수행한다.

## 참조
- [SciPy 공식 문서](https://docs.scipy.org/doc/scipy/)
- [SciPy 한국어 튜토리얼 - 데이터 사이언스 스쿨](https://datascienceschool.net/01%20python/03.00%20Scipy를%20이용한%20과학%20계산.html)
