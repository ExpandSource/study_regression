# 산점도 (Scatter Plot)

산점도 (Scatter Plot)는 두 연속형 [변수](../개념노트/변수%20(통계학).md) 간의 [관계](../개념노트/관계%20(통계).md)를 시각화하는 [기술통계](../개념노트/기술통계.md) 그래프이다. x축과 y축에 각각 변수를 배치하고, 각 관측치를 점으로 표시하여 전체적인 패턴을 파악할 수 있다.

두 변수 간의 선형 관계, 비선형 관계, 이상치(outlier), 군집(cluster) 등을 시각적으로 확인할 수 있다. [상관계수](../개념노트/상관계수.md)나 [Pearson](../개념노트/Pearson%20(통계).md), [Spearman](../개념노트/Spearman.md) 계수를 계산하기 전에 산점도를 먼저 확인하는 것이 권장된다.

회귀분석(Regression Analysis)에서 독립변수와 종속변수의 관계를 탐색하는 첫 단계로 자주 사용된다. 추세선(trend line)을 추가하여 관계의 방향성을 더 명확히 할 수 있다.

[Python](../개념노트/파이썬.md)의 [Matplotlib](../개념노트/Matplotlib.md)나 [Pandas](../개념노트/Pandas.md)를 사용하여 쉽게 작성할 수 있으며, `plt.scatter()` 또는 `df.plot.scatter()` 함수를 활용한다.

산점도 행렬(scatter plot matrix)을 사용하면 여러 변수 쌍의 관계를 한 번에 확인할 수 있다.

## 참조
- [Scatter plot - Wikipedia](https://en.wikipedia.org/wiki/Scatter_plot)
- [산점도 - 위키백과](https://ko.wikipedia.org/wiki/산점도)

![Scatter Plot Example](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Scatter_diagram_for_quality_characteristic_XXX.svg/800px-Scatter_diagram_for_quality_characteristic_XXX.svg.png)
