# 중심극한정리 (Central Limit Theorem, CLT)

[표본 (Sample)](표본%20(Sample).md) 크기가 충분히 클 때, [표본평균 (Sample Mean)](표본평균%20(Sample%20Mean).md)의 [표집분포 (Sampling Distribution)](표집분포%20(Sampling%20Distribution).md)가 근사적으로 [정규분포](정규분포.md)를 따른다는 정리. 원래 [모집단 (Population)](모집단%20(Population).md)의 분포와 무관하게 성립하는 강력한 결과이다.

수식으로 표현하면, 평균이 $\mu$이고 분산이 $\sigma^2$인 모집단에서 크기 $n$인 표본을 추출할 때:

$$\frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \xrightarrow{d} N(0, 1) \quad \text{as } n \to \infty$$

일반적으로 $n \geq 30$이면 정규분포 근사가 충분히 좋다고 간주한다. 다만 원래 분포가 매우 치우쳐 있거나 극단값이 많은 경우 더 큰 표본이 필요할 수 있다.

중심극한정리는 [신뢰구간 (Confidence Interval, CI)](신뢰구간%20(Confidence%20Interval,%20CI).md) 구성과 가설검정의 이론적 근거가 되며, [표준오차 (Standard Error, SE)](표준오차%20(Standard%20Error,%20SE).md)를 이용한 추론을 가능하게 한다. 이는 통계학에서 가장 중요한 정리 중 하나로 평가된다.

![Central Limit Theorem](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/IllustrationCentralTheorem.png/500px-IllustrationCentralTheorem.png)

## 참조
- [Wikipedia - Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
- [다크 프로그래머 - 중심극한정리](https://darkpgmr.tistory.com/147)
