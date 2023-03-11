# Deriving The EM Algorithm for PLSA

## Question 1.1:

$$
\begin{align}
L &= log\displaystyle\prod_{i = 1}^{n}P(X_i;\theta)\\\\
&=\sum_{i=1}^{n}logP(X_i;\theta)\\\\
&=\sum_{i=1}^{n}log[\lambda p(X_i|\theta_H)+(1-\lambda) p(X_i|\theta_T)]
\end{align}
$$

## Question 1.2:

### Step 1

$$
\begin{align}
L_c(\theta) &= log\ P(X,Z|\theta)\\\\
&=\sum_{i = 1}^{n}log\ P(X_i|Z_i,\theta)P(Z_i|\theta)\\\\
&=\sum_{i = 1}^{n}\sum_{k=1}^{K}I(Z_i=k)\ log\ P(X_i|Z_i=k,\theta)P(Z_i=k|\theta)\\\\
&=\sum_{i = 1}^{n}[I(Z=0)log\ \lambda P(X_i|\theta_H)+ I(Z =1)log\ (1-\lambda)P(X_i|\theta_T)]\\\\
\end{align}
$$

### Step2

$$
\begin{align}
Q(\theta,\theta^{t}) &= E_{p(Z|X,\theta^{t})}[L_c(\theta)]\\\\
&=\sum_{Z}L_c(\theta)P(Z|X,\theta^{t})\\\\
&=\sum_{i=1}^{n}[P(Z=0|X,\theta_H)log\lambda P(X_i|\theta_H) + P(Z=1|X,\theta_H)log(1-\lambda)P(X_i|\theta_T)]
\end{align}
$$

### Step3

$$
\begin{align}
\frac{\partial Q(\theta,\theta^{t})}{\partial \lambda}&=\sum_{i=1}^{n}[\frac{P(Z=0|X,\theta_H)}{\lambda}-\frac{P(Z=1|X,\theta_H)}{1-\lambda}]\\\\
&=n[\frac{P(Z=0|X,\theta_H)}{\lambda}-\frac{P(Z=1|X,\theta_H)}{1-\lambda}]\\\\
\frac{P(Z=0|X,\theta_H)}{\lambda}&-\frac{P(Z=1|X,\theta_H)}{1-\lambda} = 0\\\\
\frac{\lambda}{1-\lambda}&=\frac{P(Z=0|X,\theta_H)}{P(Z=1|X,\theta_H)}\\\\
\frac{\lambda}{1-\lambda}&=\frac{P(Z=0|X,\theta_H)}{1-P(Z=0|X,\theta_H)}\\\\
Thus,\  \lambda&=P(Z=0|X,\theta_H)
\end{align}
$$

### Step4

$$
\begin{align}
g(\theta_H)&= Q(\theta,\theta^{t})+\mu(1-\sum_{w\in V}P(w|\theta_H))\\\\
\frac{\partial g(\theta_H)}{\partial P(w|\theta_H)} &= \frac{P(Z=0|X,\theta_H^{(t)})}{P(w|\theta_H)} - \mu = 0\\\\
P(w|\theta_H) &= \frac{P(Z=0|X,\theta_H^{(t)})}{\mu}\\\\
& = \frac{P(Z=0|X,\theta_H^{(t)})}{\sum_{w \in V}P(Z=0|X,\theta_H^{(t)})}\\\\
& = \frac{P(Z = 0|X,\theta_H^{(t)})c(w, D)}{\sum_{w \in V}P(Z=0|X,\theta_H^{(t)})c(w,D)}\\\\
Thus,\ M-step:\\\\
P(w|\theta_H^{(t+1)}) &= \frac{P(Z = 0|X,\theta_H^{(t)})c(w, D)}{\sum_{w \in V}P(Z=0|X,\theta_H^{(t)})c(w,D)}\\\\
\end{align}
$$

### Step5

$$
\begin{align}
E-step:\\\\
P(Z=0|X,\theta_H^{(t)})&=\frac{\lambda P(w|\theta_H^{(t)})}{\lambda P(w|\theta_H^{(t)})+(1-\lambda)P(w|\theta_T)}\\\\
\end{align}
$$

## Question 2:

$$
\begin{align}
L_c(\theta) &= log\ P(X,Z|\theta)\\\\
&=\sum_{i = 1}^{n}log\ P(X_i|Z_i,\theta)P(Z_i|\theta)\\\\
&=\sum_{i = 1}^{n}\sum_{k=1}^{K}I(Z_i=k)\ log\ P(X_i|Z_i=k,\theta)P(Z_i=k|\theta)\\\\
&=\sum_{i = 1}^{n}[I(Z=0)log\ 0.9 P(X_i|\theta_H)+ I(Z =1)log\ 0.1 P(X_i|\theta_T)]\\\\
&=\sum_{i = 1}^{n}[I(Z=0)log\ 0.9 P(X_i|\theta_H)+ I(Z =1)log\ 0.1 P(X_i|\theta_T)]\\\\
Q(\theta,\theta^{t}) &= E_{p(Z|X,\theta^{t})}[L_c(\theta)]\\\\
&=\sum_{Z}L_c(\theta)P(Z|X,\theta^{t})\\\\
&=\sum_{i=1}^{n}[P(Z=0|X,\theta_H)log0.9 P(X_i|\theta_H) + P(Z=1|X,\theta_H)log0.1P(X_i|\theta_T)]\\\\
g(\theta_H)&= Q(\theta,\theta^{t})+\mu(1-\sum_{w\in V}P(w|\theta_H))\\\\
\frac{\partial g(\theta_H)}{\partial P(w|\theta_H)} &= \frac{P(Z=0|X,\theta_H^{(t)})}{P(w|\theta_H)} - \mu = 0\\\\
P(w|\theta_H) &= \frac{P(Z=0|X,\theta_H^{(t)})}{\mu}\\\\
& = \frac{P(Z=0|X,\theta_H^{(t)})}{\sum_{w \in V}P(Z=0|X,\theta_H^{(t)})}\\\\
& = \frac{P(Z = 0|X,\theta_H^{(t)})c(w, D)}{\sum_{w \in V}P(Z=0|X,\theta_H^{(t)})c(w,D)}\\\\
Thus,\ M-step:\\\\
P(w|\theta_H^{(t+1)}) &= \frac{P(Z = 0|X,\theta_H^{(t)})c(w, D)}{\sum_{w \in V}P(Z=0|X,\theta_H^{(t)})c(w,D)}\\\\
E-step:\\\\
P(Z=0|X,\theta_H^{(t)})&=\frac{0.9 P(w|\theta_H^{(t)})}{0.9 P(w|\theta_H^{(t)})+0.1P(w|\theta_T)}\\\\
\end{align}
$$

