# 신뢰구간 (Confidence Interval, CI)

[모수 (Parameter)](모수%20(Parameter).md)의 참값이 포함될 것으로 기대되는 구간 추정치. [표본 (Sample)](표본%20(Sample).md) 데이터를 이용하여 계산되며, [신뢰수준 (Confidence Level)](신뢰수준%20(Confidence%20Level).md)과 함께 제시된다.

모평균 $\mu$의 95% 신뢰구간은 다음과 같이 계산된다:

$$\bar{x} \pm t_{\alpha/2, n-1} \times SE$$

여기서 $\bar{x}$는 [표본평균 (Sample Mean)](표본평균%20(Sample%20Mean).md), $SE$는 [표준오차 (Standard Error, SE)](표준오차%20(Standard%20Error,%20SE).md), $t_{\alpha/2, n-1}$은 t-분포의 임계값이다. 표본 크기가 크면 ($n \geq 30$) [중심극한정리 (Central Limit Theorem, CLT)](중심극한정리%20(Central%20Limit%20Theorem,%20CLT).md)에 의해 z-분포(정규분포)를 사용할 수 있다.

신뢰구간의 폭은 표본 크기, 신뢰수준, 데이터의 변동성에 따라 달라진다. 표본 크기가 클수록, 신뢰수준이 낮을수록, 데이터 변동성이 작을수록 신뢰구간이 좁아진다. 회귀분석에서는 회귀계수의 신뢰구간을 통해 계수의 통계적 유의성을 평가한다.

점추정(point estimate)과 달리 구간추정은 추정의 [불확실성](판단의%20불확실성.md)을 정량적으로 표현한다는 장점이 있다.

![Confidence Interval](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Confidenceinterval.svg/500px-Confidenceinterval.svg.png)

## 참조
- [Wikipedia - Confidence Interval](https://en.wikipedia.org/wiki/Confidence_interval)
- [네이버 지식백과 - 신뢰구간](https://terms.naver.com/entry.naver?docId=3338213&cid=47324&categoryId=47324)
