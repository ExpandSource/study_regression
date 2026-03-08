# Spearman

스피어만 순위 [상관계수](../개념노트/상관계수.md) (Spearman's Rank Correlation Coefficient)는 두 [변수](../개념노트/변수%20(통계학).md) 간의 단조 [관계](../개념노트/관계%20(통계).md) (monotonic relationship)를 측정하는 비모수 통계 지표이다. 원본 데이터 값 대신 순위(rank)를 사용하여 계산한다.

[Pearson](../개념노트/Pearson%20(통계).md) 상관계수와 달리 선형성과 정규분포 가정이 필요 없으며, 이상치에 덜 민감하다. -1에서 1 사이의 값을 가지며, 순위가 일치할수록 1에 가깝고, 반대일수록 -1에 가깝다.

수식은 다음과 같다 (순위 차이 $d_i$를 사용):

$$\rho = 1 - \frac{6\sum d_i^2}{n(n^2-1)}$$

서열척도(ordinal scale) 데이터나 비선형이지만 단조 증가/감소하는 관계를 분석할 때 적합하다. 예를 들어, 학생들의 성적 순위와 공부 시간 순위 간의 관계를 분석하는 데 사용할 수 있다.

[산점도](../개념노트/산점도%20scatter%20plot.md)와 함께 사용하면 관계의 형태를 시각적으로 파악할 수 있다.

## 참조
- [Spearman's rank correlation coefficient - Wikipedia](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)
- [스피어만 상관계수 - 공돌이의 수학정리노트](https://angeloyeo.github.io/2020/08/05/spearman_correlation.html)
