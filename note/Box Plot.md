# Box Plot

## 핵심 개념
Box Plot(상자 그림)은 [기술통계](./기술통계.md)에서 데이터의 분포를 시각화하는 그래프이다. [사분위수](./사분위수.md)를 기반으로 중심 경향성, 산포도, 이상치(Outlier)를 한눈에 파악할 수 있다.

## 구성 요소
- **상자(Box)**: Q1(25%)에서 Q3(75%)까지의 범위 (IQR)
- **중앙선**: 중앙값(Median, Q2)
- **수염(Whisker)**: Q1 - 1.5×IQR ~ Q3 + 1.5×IQR 범위
- **이상치(Outlier)**: 수염 밖의 점들

## IQR (Interquartile Range)
$$IQR = Q3 - Q1$$

## 활용
- 데이터 분포의 비대칭성 확인
- 그룹 간 분포 비교
- 이상치 탐지

## 참고 자료
- [Wikipedia - Box Plot](https://en.wikipedia.org/wiki/Box_plot)
- [네이버 지식백과 - 상자그림](https://terms.naver.com/entry.naver?docId=3405064&cid=47324&categoryId=47324)

![Box Plot Anatomy](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Boxplot_vs_PDF.svg/400px-Boxplot_vs_PDF.svg.png)
