# Shapiro-Wilk 검정

Shapiro-Wilk 검정(Shapiro-Wilk Test)은 데이터가 [정규분포](./정규분포.md)를 따르는지 검정하는 통계적 방법이다. 정규성 검정(Normality Test) 중 가장 강력한(powerful) 검정으로 알려져 있다.

$$W = \frac{(\sum_{i=1}^{n} a_i x_{(i)})^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$

귀무가설(H₀)은 "데이터가 정규분포를 따른다"이다. p-value가 유의수준(보통 0.05)보다 작으면 귀무가설을 기각하고, 데이터가 정규분포를 따르지 않는다고 판단한다.

표본 크기가 3~5000 사이일 때 적합하며, 소표본에서 특히 효과적이다. [Q-Q plot](./Q-Q%20plot.md)과 함께 사용하여 정규성을 시각적으로도 확인하는 것이 권장된다.

[추론통계](./추론통계.md)에서 t-검정, ANOVA 등 모수적 검정의 전제조건인 정규성 가정을 확인할 때 필수적으로 사용된다.

## 참조
- [Shapiro-Wilk Test - Wikipedia](https://en.wikipedia.org/wiki/Shapiro–Wilk_test)
- [정규성 검정 설명 - 공돌이의 수학정리노트](https://angeloyeo.github.io/2020/11/25/shapiro_wilk_test.html)
