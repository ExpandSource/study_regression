# 시차 선택 기준 (AIC, BIC)

AIC(Akaike Information Criterion)와 BIC(Bayesian Information Criterion)는 [VAR (벡터자기회귀모형)](VAR%20(벡터자기회귀모형).md)에서 최적 [시차 (Lag)](시차%20(Lag).md) $p$를 선택하기 위한 정보 기준(Information Criterion)이다.

$$\text{AIC} = -2\ln(\hat{L}) + 2k \qquad \text{BIC} = -2\ln(\hat{L}) + k\ln(n)$$

여기서 $\hat{L}$은 최대 우도(likelihood), $k$는 추정 모수 수, $n$은 표본 크기이다. 두 기준 모두 **값이 작을수록** 좋은 모형이며, BIC는 AIC보다 모수 수에 더 강하게 페널티를 부과하여 더 간결한 모형을 선호한다.

모든 후보 시차 $p = 1, 2, \ldots, p_{max}$에 대해 VAR을 추정하고, AIC/BIC가 최소인 $p$를 선택한다. AIC는 예측력, BIC는 모형 간결성 측면에서 주로 참조한다. [가설검정](가설검정.md)과 달리 모형 비교의 상대적 기준으로만 사용된다.

---

## 참조
- [Akaike information criterion - Wikipedia](https://en.wikipedia.org/wiki/Akaike_information_criterion)
- [AIC와 BIC 비교 - 공돌이의 수학정리노트](https://angeloyeo.github.io/2020/07/17/MLE.html)
