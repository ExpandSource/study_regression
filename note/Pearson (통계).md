# Pearson (통계)

피어슨 [상관계수](../개념노트/상관계수.md) (Pearson Correlation Coefficient)는 두 [변수](../개념노트/변수%20(통계학).md) 간의 선형 관계 강도와 방향을 측정하는 [기술통계](../개념노트/기술통계.md) 지표이다. -1에서 1 사이의 값을 가지며, 1에 가까우면 양의 선형 관계, -1에 가까우면 음의 선형 관계, 0에 가까우면 선형 관계가 없음을 의미한다.

카를 피어슨(Karl Pearson)이 개발한 이 계수는 두 변수의 공분산을 각 변수의 [표준편차](../개념노트/표준편차%20(통계학).md)의 곱으로 나눈 값이다. 수식은 다음과 같다:

$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

선형 관계만 측정하므로 비선형 관계는 감지하지 못한다는 한계가 있다. 이상치(outlier)에 민감하며, 두 변수 모두 정규분포를 따라야 정확한 해석이 가능하다. 비모수적 대안으로는 [Spearman](../개념노트/Spearman.md) 순위 상관계수가 있다.

[산점도](../개념노트/산점도%20scatter%20plot.md)와 함께 사용하여 시각적으로 관계를 확인하는 것이 권장된다.

## 참조
- [Pearson correlation coefficient - Wikipedia](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)
- [피어슨 상관계수 - 공돌이의 수학정리노트](https://angeloyeo.github.io/2020/08/04/pearson_correlation.html)

![Pearson Correlation Examples](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Correlation_examples2.svg/800px-Correlation_examples2.svg.png)
