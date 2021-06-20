- [Sample space and Events](#sample-space-and-events)
- [Probability](#probability)
  - [Independent Events](#independent-events)
  - [Conditional Probability](#conditional-probability)
  - [Bayes' Theorem](#bayes-theorem)
- [Random Variable](#random-variable)
  - [Probability with RVs](#probability-with-rvs)
- [Probability and Distribution](#probability-and-distribution)
  - [Cumulative Distribution Function(CDF)](#cumulative-distribution-functioncdf)
  - [Probability Mass Function(PMF)](#probability-mass-functionpmf)
  - [Probability Density Function(PDF)](#probability-density-functionpdf)
  - [Others](#others)
- [Expectations](#expectations)
  - [Expectation](#expectation)
  - [Variance](#variance)
  - [Covariance](#covariance)
  - [Conditional Expectation](#conditional-expectation)
  - [Conditional Variance](#conditional-variance)
- [Famous Distributions](#famous-distributions)
  - [Bernoulli Distribution](#bernoulli-distribution)
  - [Binomial Distribution](#binomial-distribution)
  - [Geometric Distribution](#geometric-distribution)
  - [Poisson Distribution](#poisson-distribution)
  - [Normal Distribution](#normal-distribution)
  - [Chi-Squeare Distribution](#chi-squeare-distribution)

# Sample space and Events
- Sample space $\Omega$: Set of possible outcomes of an events
- Points $w$ in $\Omega$: sample outcome = realization = elements
- Subset $A$ of $\Omega$: event
- Given an event $A$
    - $A^c = \{ w \in \Omega: w \notin A\}$: complement of $A$
    - $\Omega^c$ is the empty set $\empty$
    - $A \bigcup B - \{ w \in \Omega: w \in A \text{ or } w \in B \text{ or } w\in \text{both} \}$
    - 합집합: $\bigcup_{i=1}^{\infty} A_i = \{ w \in \Omega: w \in A_i \text{ for at least one }i \}$
    - 교집합: $\bigcap_{i=1}^{\infty} A_i = \{ w \in \Omega: w \in A_i \text{ for all }i \}$
- Given sequence of $A_1, A_2, \cdots$
    - Disjoint / manually exclusive: when $A_i \bigcap A_j = \empty$ whenever $i \neq j$
    - a partition of $\Omega$ & $A_1, A_2, \cdots$ are disjoint sets: $\bigcup_{i=1}^{\infty} A_i = \Omega$
    - Indicator of $A$: $I_A (w) = I(w \in A) = \begin{cases} 1 & \text{if } w \in A \\ 0 & \text{if } w \notin A \end{cases}$
    - Monotone increasing: $A_1 \subset A_2 \subset \cdots \rightarrow \lim_{n \rightarrow \infty} A_n = \bigcup_{i=1}^{\infty} A_i$
    - Monotone decreasing: $A_1 \supset A_2 \supset \cdots \rightarrow \lim_{n \rightarrow \infty} A_n = \bigcap_{i=1}^{\infty} A_i$

---

# Probability

확률은 실수(real number) $P(A)$를 event $A$에 부여하는 것
- $P$는 probability distribution 혹은 probability measure 이라고함
    - Axiom 1: $P(A) \geq 0$ for every $A$
    - Axiom 2: $P(\Omega) = 1$
    - Axiom 3: If $A_1, A_2, \cdots$ 가 disjoint 일 경우, $P(\bigcup_{i=1}^{\infty} A_i) = \sum_{i=1}^{\infty} P(A_i)$
- Properties
    - $P(\empty) = 0$
    - $A \subset B \Rightarrow P(A) \leq P(B)$
    - $0 \leq P(A) \leq 1$
    - $P(A^c) = 1 - P(A)$
    - $P(A \bigcup B) = P(A) + P(B) - P(A \bigcap B)$
    - $A \bigcap B = \empty \Rightarrow P(A \bigcup B) = P(A) + P(B)$


두 가지 확률에 대한 관점, Axiom과 interpretation는 서로 아주 다르다
- Frequentist: Relative frequency of many trials, $P(A)$ is the long run proportion of times that A is true in repetition
    - 확률을 많은 시도 후의 사건의 상대적 빈도의 극한으로 해석
- Bayesian (Subjective): Degree of belief, $P(A)$ measures the observers strength's of belief that $A$ is true.
    - 믿음의 정도로 확률을 해석, 이는 이전 실험에 대한 결과, 또는 그 사건에 대한 개인적 믿음 등, 그 사건에 대한 사전 지식에 기반할 수 있음

## Independent Events

- If $A$ and $B$ are independent $\rightarrow P(A \bigcap B) = P(A)P(B)$ 
- $A$ set of event $\{A_i: i \in I \}$ is independent if $P( \bigcap_{i \in J} A_i) = \prod_{i \in J} P(A_i)$ for every finite subset J of I
- Disjoint event is not independent event $P(A \bigcap B) = 0 \neq P(A)P(B)$

## Conditional Probability

- If $P(B) > 0$ then the conditional probability of $A$ given $B$ is $P(A \vert B) = \dfrac{P(AB)}{P(B)}$
- Sample space changes to $B$
- $P(A \vert B) \neq P(B \vert A)$
- $A$ and $B$ are independent if and only if $P(A \vert B) = \dfrac{P(AB)}{P(B)} = \dfrac{P(A)P(B)}{P(B)} = P(A)$

## Bayes' Theorem

- $P(A_i \vert B) = \dfrac{P(B \vert A_i) P(A_i)}{P(B)} = \dfrac{P(B \vert A_i) P(A_i)}{\sum_j P(B\vert A_j) P(A_j)}$
- $P(A)$: prior, $B$: observed data, $P(A \vert B)$ posterior 
- update the belief $P(A)$ given observed data $B$, $P(A \vert B)$
- $P(B \vert A)$: Given prior, observed data probability

---

# Random Variable

- A random variable is a mapping $X: \Omega \rightarrow \Bbb{R}$ that assigns a real number $X(w)$ to each outcome $w$

## Probability with RVs

Calculate the probability by inverting RVs. Given a random variable $X$ and a subset $A$ of the real line, define $X^{-1}(A) = \{w \in \Omega: X(w) \in A \}$ and let 

$$\begin{aligned} P(X \in A) &= P(X^{-1}(A)) = P(\{w \in \Omega; X(w) \in A \}) \\ P(X = x) &= P(X^{-1}(x)) = P(\{w \in \Omega; X(w) = x \}) \end{aligned}$$

- Example: Coin Toss, Let $X$ be the number of heads.

| $w$ | $P(\{w\})$ | $X(w)$ |
|---|---|---|
| TT | 1/4 | 0 |
| HT | 1/4 | 1 |
| TH | 1/4 | 1 |
| HH | 1/4 | 2 |

to 

| $x$ | $P(\{X=x\})$ |
|---|---|
| 0 | 1/4 |
| 1 | 1/2 |
| 2 | 1/4 |

---

# Probability and Distribution

## Cumulative Distribution Function(CDF)

A function $F_X: \Bbb{R} \rightarrow [0, 1]$ defined by $F_X(x) = P(X \leq x)$

- 모든 RVs.의 정보를 가지고 있음. Non-decreasing, right continuous function.
- Example: Coin Toss, Let $X$ be the number of heads.

    $$F_X(x) \begin{cases} 0 & x < 0 \\ 1/4 & 0 \leq x < 1 \\ 3/4 & 1 \leq x < 2 \\ 1 & x \geq 2\end{cases}$$

## Probability Mass Function(PMF)

$f_X(x) = P(X=x)$ when $X$ is discrete if it takes countably many values $\{x_1, x_2, \cdots \}$

- CDF: $F_X(x) = P(X \leq x) = \sum_{x_i \leq x} f_X(x_i) = \sum_{x_i \leq x} P(X=x_i) = \sum_{x_i \leq x} f_X(x_i)$
- Example: Coin Toss, Let $X$ be the number of heads.

    $$F_X(x) \begin{cases} 1/4 & x = 0 \\ 1/2 & x=1 \\ 1/4 & x=2 \\ 0 & \text{otherwise}\end{cases}$$

## Probability Density Function(PDF)

$f_X(x)$ is PDF. When random variable $X$ is continuous if there exists a function $f_X$ such that $f_X(x) \geq 0$ for all $x$, $\int_{-\infty}^{\infty} f_X(x) dx =1$ and for every $a \leq b$, 

$$P(a < X < b) = \int_a^b f_X(x)dx$$

- CDF: $F_X(x) = \int_{-\infty}^{x} f_X(t)dt$ and $f_X(x) = F_{X}^{'}(x)$ at all points $x$ at which $F_X$ is differentiable

## Others 

- Quantile function

    $F^{-1}(q) = \inf \{ x: F(x) > q\}$ for $q \in [0, 1]$, If $F$ is strictly increasing and continuous then $F^{-1}(q)$ is the unique real number $x$ such that $F(x)=q$.

- Equal distribution: $F_X(x) = F_Y(x)$

---

# Expectations

## Expectation

Expected value, mean, first moment: one number summary of the distribution

$E(X) = \int x dF(x) = \mu_X = \begin{cases} \sum_x x f(x) & \text{if } X = \text{discrete} \\ \int x f(x) & \text{if } X = \text{continuous} \\  \end{cases}$

- The Rule of the Lazy Statistician: Let $Y = r(X)$, then $E(Y) = E(r(x)) = \int r(x) dF_X(x)$
- Property:
    - $E(aX + b) = aE(X) + b$
    - $E(XY) = E(X)E(Y)$ if $X, Y$ are independent

## Variance

Variance, second moment: the spread of distribution

$V(X) = \sigma^2 = E[(X-\mu)^2] = \int (x - \mu)^2 dF(x)$

- Standard deviation: $sd(X) = \sqrt{V(X)}$
- Property:
    - $V(X) = E(X^2) - \mu^2$
    - $V(aX + b) = a^2 V(X)$
    - $V(aX+bY) = a^2V(X) + b^2V(Y)$ if $X, Y$ are independent

## Covariance

Covariance: the strength of linear relationship between two RVs X and Y

$Cov(X, Y) = E((X - \mu_X)(Y - \mu_Y))$

- Correlation: $\rho = \rho_{X, Y} = \dfrac{Cov(X, Y)}{\sigma_X \sigma_Y}$
- Property:
    - $Cov(X, Y) = E(XY) - E(X)E(Y)$
    - $-1 \leq \rho(X, Y) \leq 1$
    - V(X \pm Y) = V(X) + V(Y) \pm Cov(X, Y)

## Conditional Expectation

Given $Y=y$, conditional expectation of $X$ is 

$$E(X \vert Y) = \begin{cases} \sum x f_{X\vert Y} (x \vert y) dx & \text{discrete} \\ \int x f_{X\vert Y} (x \vert y) dx & \text{continuous} \end{cases}$$

$$E(r(X, Y) \vert Y) = \begin{cases} \sum r(X, Y) f_{X\vert Y} (x \vert y) dx & \text{discrete} \\ \int r(X, Y) f_{X\vert Y} (x \vert y) dx & \text{continuous} \end{cases}$$

- $E(X \vert Y)$ is function of $Y$
- Property: $E[E(Y \vert X)] = E(Y)$

## Conditional Variance

$V(Y \vert X=x) = \int (y - \mu(x))^2 f(y\vert x)dy$ where $\mu(x) = E(Y\vert X=x)$

- Property: $V(Y) = E[V(Y \vert X)] + V[E(Y\vert X)]$

---

# Famous Distributions

## Bernoulli Distribution

- $X \sim \text{Bernoulli}(p)$
- $X$ is binary RVs. 
- $P(X=1) = p$ and $P(X=0)=1-p$ for some $p \in [0, 1]$
- $f(x) = p^x(1-p)^{1-x}$ for $x \in \{0, 1\}$
- Example: Coin Toss $p$ = probability to have head
- $E(X) = p$
- $V(X) = p(1-p)$

## Binomial Distribution

- $X \sim \text{Binomial}(n, p)$, sum of $n$ independent $\text{Bernoulli}(p)$ random variables
- $X = \{x_1, x_2, \cdots, x_n\}$ are independent
- $f(x) = \begin{cases} \begin{pmatrix} n \\ x \end{pmatrix} p^x (1-p)^{n-x} & \text{for } x=0, \cdots, n \\ 0 & \text{otherwise} \end{cases}$
- Example: Coin Toss $x$ = the number of head, $p$ = probability to have head
- $E(X) = np$
- $V(X) = np(1-p)$

## Geometric Distribution

- $X \sim \text{Geom}(p), p \in (0, 1)$
- $P(X=k) = p(1-p)^{k-1}, \quad k \geq 1$
- Example: Coin Toss, Number of trials needed until the first head
- $E(X) = 1/p$
- $V(X) = (1-p)/p^2$

## Poisson Distribution

- $X \sim \text{Poisson}(\lambda)$
- $f(x) = e^{-\lambda} \dfrac{\lambda^x}{x!} \quad x \geq 0$
- $\sum_{x=0}^{\infty} f(x) = e^{-\lambda} \sum_{x=0}^{\infty} \dfrac{\lambda^x}{x!} = e^{-\lambda}e^{\lambda} = 1$
- Derived to model the number of rare event, wrongful conviction(잘못된 유죄 결정)
- $\lambda$: mean & variance of dist.
- Sum of two Possion RVs follows Poissons.
- Example: event incidence(차 사고 등), $x$: number of the incidence in each day, $\lambda$: average number
- $E(X) = V(X) = \lambda$

##  Normal Distribution

- $X \sim \text{Normal}(\mu, \sigma^2)$
- $f(x) = \dfrac{1}{\sigma\sqrt{2\pi}} \exp \{ -\dfrac{(x-\mu)^2}{2\sigma^2}\}, \quad x\in\Bbb{R}$
- $Z \sim \text{Standard Normal}(0, 1)$ where $Z = \dfrac{X-\mu}{\sigma}$
- Example: widly used for model continuous measure, noise(error) in the observation
- $E(X) = \mu$
- $V(X) = \sigma^2$

## Chi-Squeare Distribution

- $X \sim \chi^2(p)$
- $f(x) = \dfrac{1}{\Gamma(p/2)2^{p/2}} x^{(p/2)-1} e^{-e/2}, \quad x > 0$
- If $Z_1, \cdots, Z_p$ are independent standard Normal RVs then $\sum_{i=1}^p Z_i^2 \sim \chi_p^2$
- $E(X) = p$
- $V(X) = 2p$