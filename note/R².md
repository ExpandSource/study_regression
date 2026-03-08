# R² (결정계수, Coefficient of Determination)

R²는 [회귀분석](회귀분석.md) 모델이 [종속변수](종속변수.md)의 전체 분산 중 얼마나 설명하는지를 나타내는 적합도 지표이다. 0에서 1 사이의 값을 가지며, 1에 가까울수록 모델이 데이터를 잘 설명한다.

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}} = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

여기서 $SS_{res}$는 [잔차](잔차.md) 제곱합, $SS_{tot}$는 총 제곱합이다. 단순선형회귀에서 R²는 [상관계수](상관계수.md) $r$의 제곱과 같다.

[다중회귀](다중회귀.md)에서는 독립변수를 추가할수록 R²가 무조건 증가하므로, 변수 수를 페널티로 반영한 수정 R²(Adjusted R²)를 함께 확인한다. R²가 높아도 [잔차](잔차.md) 패턴이 있으면 모델이 부적절할 수 있다.

---

## 참조
- [Coefficient of determination - Wikipedia](https://en.wikipedia.org/wiki/Coefficient_of_determination)
- [R² 결정계수 이해하기 - 공돌이의 수학정리노트](https://angeloyeo.github.io/2020/08/24/linear_regression.html)

![R² 시각화](https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Coefficient_of_Determination.svg/400px-Coefficient_of_Determination.svg.png)
