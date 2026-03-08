# 표본평균 (Sample Mean)

[표본 (Sample)](표본%20(Sample).md) 데이터의 산술평균. 모평균 $\mu$를 추정하는 대표적인 [통계량 (Statistic)](통계량%20(Statistic).md)이며, $\bar{x}$ 또는 $\bar{X}$로 표기한다.

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

표본평균은 불편추정량(unbiased estimator)으로, 기댓값이 모평균과 같다: $E[\bar{x}] = \mu$. 표본평균의 분산은 $\text{Var}(\bar{x}) = \frac{\sigma^2}{n}$이며, 표본 크기 $n$이 커질수록 분산이 작아진다.

[중심극한정리 (Central Limit Theorem, CLT)](중심극한정리%20(Central%20Limit%20Theorem,%20CLT).md)에 따라, 표본 크기가 충분히 크면 표본평균의 [표집분포 (Sampling Distribution)](표집분포%20(Sampling%20Distribution).md)는 근사적으로 정규분포 $N(\mu, \frac{\sigma^2}{n})$를 따른다. 이는 원래 모집단의 분포와 무관하게 성립한다.

표본평균의 [표준오차 (Standard Error, SE)](표준오차%20(Standard%20Error,%20SE).md)는 $SE = \frac{s}{\sqrt{n}}$로 계산되며, 이를 통해 모평균의 [신뢰구간 (Confidence Interval, CI)](신뢰구간%20(Confidence%20Interval,%20CI).md)을 구성할 수 있다.

![Sample Mean Distribution](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/500px-Standard_deviation_diagram.svg.png)

## 참조
- [Wikipedia - Sample Mean](https://en.wikipedia.org/wiki/Sample_mean_and_covariance)
- [네이버 지식백과 - 표본평균](https://terms.naver.com/entry.naver?docId=3338357&cid=47324&categoryId=47324)
