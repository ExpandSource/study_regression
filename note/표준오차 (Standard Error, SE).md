# 표준오차 (Standard Error, SE)

[통계량 (Statistic)](통계량%20(Statistic).md)의 [표집분포 (Sampling Distribution)](표집분포%20(Sampling%20Distribution).md) 표준편차. 통계량이 얼마나 변동하는지를 나타내며, 추정의 정확도를 측정하는 지표이다.

[표본평균 (Sample Mean)](표본평균%20(Sample%20Mean).md)의 표준오차는 다음과 같이 계산된다:

$$SE(\bar{x}) = \frac{\sigma}{\sqrt{n}}$$

실무에서는 모표준편차 $\sigma$를 알 수 없으므로, 표본표준편차 $s$로 대체하여 $SE = \frac{s}{\sqrt{n}}$를 사용한다. 표본 크기 $n$이 커질수록 표준오차는 작아지며, 이는 더 큰 표본이 더 정확한 추정을 제공함을 의미한다.

표준오차는 [신뢰구간 (Confidence Interval, CI)](신뢰구간%20(Confidence%20Interval,%20CI).md) 계산에 핵심적으로 사용된다. 예를 들어, 95% 신뢰구간은 대략 $\bar{x} \pm 1.96 \times SE$로 구성된다. 회귀분석에서는 회귀계수의 표준오차를 통해 계수 추정치의 신뢰성을 평가한다.

표준오차는 표준편차와 다른 개념으로, 표준편차는 개별 관측값의 산포를 나타내지만 표준오차는 통계량의 산포를 나타낸다.


![](https://freshrimpsushi.github.io/ko/posts/541/20180425_205309.png#center)
## 참조
- [Wikipedia - Standard Error](https://en.wikipedia.org/wiki/Standard_error)
- [네이버 지식백과 - 표준오차](https://terms.naver.com/entry.naver?docId=3338360&cid=47324&categoryId=47324)
