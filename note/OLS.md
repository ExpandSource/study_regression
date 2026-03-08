# OLS (Ordinary Least Squares, 최소제곱법)

OLS는 [회귀분석](회귀분석.md)에서 [회귀계수](회귀계수.md)를 추정하는 가장 기본적인 방법으로, [잔차](잔차.md)(실제값 - 예측값)의 제곱합(RSS, Residual Sum of Squares)을 최소화하는 계수를 구한다.

$$\min_{\beta} \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 = \min_{\beta} \sum_{i=1}^{n}(y_i - \beta_0 - \beta_1 x_i)^2$$

OLS 추정량이 최선의 선형불편추정량(BLUE, Best Linear Unbiased Estimator)이 되기 위한 조건을 가우스-마코프 정리(Gauss-Markov Theorem)라 한다. 주요 가정은 잔차의 정규성, 등분산성(homoscedasticity), 독립성이다.

가정이 위반되면 추정값의 신뢰성이 낮아지므로, [잔차](잔차.md) 플롯을 통한 가정 검토가 필수적이다. Python에서는 `statsmodels` 라이브러리의 `OLS` 함수로 쉽게 적용할 수 있다.

---

## 참조
- [Ordinary least squares - Wikipedia](https://en.wikipedia.org/wiki/Ordinary_least_squares)
- [최소제곱법 이해 - 다크프로그래머](https://darkpgmr.tistory.com/56)

![OLS 시각화](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Linear_least_squares_example2.svg/400px-Linear_least_squares_example2.svg.png)
