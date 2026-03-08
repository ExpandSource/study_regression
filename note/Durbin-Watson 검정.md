# Durbin-Watson 검정 (Durbin-Watson Test)

회귀분석의 [잔차](잔차.md)에 [자기상관](자기상관.md)(autocorrelation)이 존재하는지 검정하는 방법. 특히 1차 자기상관(lag-1 autocorrelation)을 탐지하는 데 사용된다.

검정통계량 $d$는 다음과 같이 계산된다:

$$d = \frac{\sum_{t=2}^{n}(e_t - e_{t-1})^2}{\sum_{t=1}^{n}e_t^2}$$

$d$ 값의 범위는 0~4이며 해석은 다음과 같다:
- $d \approx 2$: 자기상관 없음 (이상적)
- $d < 1.5$: 양(+)의 자기상관 존재
- $d > 2.5$: 음(-)의 자기상관 존재

자기상관이 감지되면 [OLS](OLS.md) 추정의 효율성이 저하되므로 [차분](차분.md), GLS(일반화최소제곱법), 또는 ARIMA 모형을 적용한다. Python에서는 `statsmodels`의 `durbin_watson()` 함수로 계산할 수 있다.

## 참조
- [Wikipedia - Durbin–Watson Statistic](https://en.wikipedia.org/wiki/Durbin%E2%80%93Watson_statistic)
- [statsmodels - durbin_watson 공식 문서](https://www.statsmodels.org/stable/generated/statsmodels.stats.stattools.durbin_watson.html)
