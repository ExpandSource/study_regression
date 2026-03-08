# ADF 검정 (Augmented Dickey-Fuller Test)

[시계열](시계열.md) 데이터의 [정상성](정상성.md)을 검증하는 단위근 검정(unit root test). 단순 Dickey-Fuller 검정을 확장하여 [자기상관](자기상관.md)을 보정한 형태이다.

[귀무가설](귀무가설.md)과 [대립가설](대립가설.md):
- $H_0$: 단위근이 존재한다 → 비정상 시계열
- $H_1$: 단위근이 없다 → 정상 시계열

[p-value](p-value.md)가 [유의수준](유의수준.md)(보통 0.05)보다 작으면 $H_0$를 기각하여 정상 시계열로 판단한다. p-value가 크면 비정상 시계열이므로 [차분](차분.md)이 필요하다.

Python에서는 `statsmodels`의 `adfuller()` 함수로 수행한다:
```python
from statsmodels.tsa.stattools import adfuller
result = adfuller(series)
print(f'ADF Statistic: {result[0]:.4f}, p-value: {result[1]:.4f}')
```

## 참조
- [Wikipedia - Augmented Dickey–Fuller Test](https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test)
- [statsmodels - adfuller 공식 문서](https://www.statsmodels.org/stable/generated/statsmodels.tsa.stattools.adfuller.html)
