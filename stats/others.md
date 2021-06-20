

# Convergence of RV 

- Law of large number: 샘플의 크키가 커질 수록 샘플 평균은 점점 전체 모집단의 평균과 가까울 가능성이 높다. 혹은 샘플 평균의 분산이 점점 작아진다(한 점으로 모이게 된다)
- Central Limit Theorem: 동일한 확률분포를 가진 독립 확률 변수 n개의 평균의 분포는 n이 적당히 크다면 정규분포에 가까워진다
- Taylor Expansion: $f(x) = f(a) + f^{'}(a)(x-a) + \dfrac{f^{(2)(a)}}{2!}(x-a)^2 + \cdots$
- Parametric and Non-parametric Model
    - Statistical model: set of distributions
    - Parametric model: can be parameterized by a finite number of parameters


# Mean Square Error

$MSE = E_{\theta}[(\hat{\theta}_n - \theta)^2]$

- bias-bariance decomposition: $MSE = bias^2(\hat{\theta}_n) + V_{\theta}(\hat{\theta}_n)$
- 유도: 
    
    $$\begin{aligned} E_{\theta}(\hat{\theta}_n - \theta)^2 &=
    E_{\theta}(\hat{\theta}_n -E(\hat{\theta}_n) + E(\hat{\theta}_n) - \theta)^2 \\
    &= E_{\theta}( (\hat{\theta}_n - E(\hat{\theta}_n))^2 ) + E_{\theta}( E(\hat{\theta}_n) - \theta)^2 ) + 2 E_{\theta}( \hat{\theta}_n - E(\hat{\theta}_n) )( E(\hat{\theta}_n) - \theta ) \\
    &= V_{\theta}(\hat{\theta}_n) + bias^2(\hat{\theta}_n) + 0
    \end{aligned}$$

- bias-Variance Tradeoff
    - low variance $\rightarrow$ high bias -> underfitting
    - high variance $\rightarrow$ low bias -> overfitting
- Complex 한 모델일 수록 bias는 줄어들겠지만 variance가 높아질 가능성이 있음