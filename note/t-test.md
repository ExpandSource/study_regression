# t-test (t-검정)

t-test는 [표본](./표본%20(Sample).md)의 [표본평균](./표본평균%20(Sample%20Mean).md)이 가정된 [모수](./모수%20(Parameter).md) 값(또는 두 집단의 평균)과 유의하게 다른지를 검정하는 방법이다. 단일표본 t-test, 독립표본 t-test, 대응표본 t-test 등 여러 종류가 있으며, [모집단](./모집단%20(Population).md) [표준편차](../개념노트/표준편차.md)를 모를 때 주로 사용한다.

t-test의 [검정통계량](./검정통계량.md)은 $t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$로 계산되며, 이 값이 [표집분포](./표집분포%20(Sampling%20Distribution).md)의 t-분포와 비교된다. t-분포는 [표본](./표본%20(Sample).md) 크기에 따라 모양이 달라지므로, 자유도(Degrees of Freedom)를 반드시 명시해야 한다. 표본이 클수록 t-분포는 정규분포에 가까워진다.

$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}$$

## 관련 개념
- [[가설검정]]
- [[표본평균]]
- [[검정통계량]]
- [[p-value]]

## 참고
- [t-test - Wikipedia](https://en.wikipedia.org/wiki/T-test)
- [t-검정 쉽게 이해하기 - 통계 학습](https://blog.naver.com/PostView.nhn?blogId=statstudy&logNo=220912345678)

## 시각 자료
![t-분포](https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/T_distribution_pdf.svg/400px-T_distribution_pdf.svg.png)
