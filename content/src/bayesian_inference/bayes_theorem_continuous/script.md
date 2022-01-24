# Bayes theorem Continuous distributions


As we see, the great discovery of ways was that we can relate different observations (information gain) with existing knowledge in a very precise way.

We are in the middle of our journey to effectively use bayes inference in ML

Let's now move to a more complex example. We want to estimate our position from consecutive measurements from a noise position sensor. To make thins simple, the sensor gives us our position in 1D.

We **know** the sensor is noisy, it gives us the position in meters with respect to a certain origin and the manufacturer tells us that the sensor has a standard deviation 1.

We will call:

- $z$ our actual position
- $s_i$ with $i \ge 0$ the consecutive measurements we do.

with this $P(z)$ represents **our knowledge** (or uncertainty) of where we are ($z$), and $P(z|s_i)$ would be our knowledge **after** seeing measurement $s_i$

Let's start with the first measurement: $s_0$ and let's imagine the sensor reading is $s_0=22.3m$

We want to estimate $P(z|s_0=22.3m)$, so let's use Bayes:

$$P(z|s_0=22.3m) = \frac{P(s_0=22.3m|z) P(z)}{P(s_0=22.3m)}$$

The key thing here is to understand that we are **dealing with distributions**. This means:

- $P(z|s_0=22.3m)$ is a distribution (**not a number as before**), and in fact, we can see it as a function of $z$ (a probability distribution), because we have a precise measurement, a value for $s_0$. We could also write it as $P(z|s_0)$ for short, but we **must remember** that it is a **function** of $z$
- $P(s_0=22.3m|z)$ is a distribution (**not a number as before**), also a function of $z$, because $s_0$ is fixed.
- $P(z)$ is a distribution also a function of $x$
- $P(s_0=22.3m)$ is **a number**, we are asking about the probability of observing $s_0=22.3m$. This **does not** depend on $z$.

What do we use for the different terms:

- $P(z)$ is the **prior**, our initial guess of the position. We could use a very uninformative prior, such as $\mathcal{N}(0,100)$, which a large std. Or if we somehow have some prior information, that $x$ position is about 20m we could use $\mathcal{N}(20,5)$

- $P(s_0|z)$ es el **likelihood**, es decir, qué probable sería ver lo que he visto en función de $x$, o sea, si yo estuviera ubicado en distintos lugares. 
- Intuitively, if my real position $z$ is far from 22.3, the likelihood of my observation ($s_0=22.3m$) would be lower than if I was closer. Como el fabricante nos dice el fabricante que el sensor tiene una std=1m, por tanto lo modelamos como $\mathcal{N}(z,1)$, es decir, una normal centrada en $z$.
- $P(s_0)$ is the normalization constant. **This is hard** and we do not know it beforehand, so we use the trick of summing over all possible values of $z$

$$P(s_0=22.3m) = \int_{-\infty}^\infty P(s_0=22.3m|z)P(z)dz$$

observe that the numeration is **always** just one item of the infinite sum that is the normalization constant. So this is really a normalization constant.

Now, since we are **dealing with distributions**, let's use the PDFs of the different distributions that we have. Remember that if $x\sim \mathcal{N}(\mu, \sigma)$, then

$$P(x)= \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(x-\mu)^2/\sigma^2}$$

so let's substitute in our case for bayes theorem, we will use $\mathcal{N}(20,5)$ s our prior.


$$P(z|s_0=22.3m) = \frac{\frac{1}{1 \cdot \sqrt{2\pi}}e^{-\frac{1}{2}(s_0-z)^2/1^2} \frac{1}{3\cdot \sqrt{2\pi}}e^{-\frac{1}{2}(z-20)^2/3^2} }{P(s_0=22.3m)}$$

**small detail**, observe how we use $(s_0-z)^2$ in the likelihood, and $(z-20)^2$ in the prior. Since we are squaring the order of $z$ does not matter, but observe that in the likelihood $z$ is acting as the parameter $\mu$ of normal distribution (i.e. the normal is **centered** at $z$), and in the prior it is acting as the pdf argument (the normal is **centered** at 20). If our distribution PDF was not symmetric in $\mu$ and $x$, we would have to be very careful on this.

and finally

$$P(z|s_0=22.3m) = \frac{\frac{1}{1 \cdot \sqrt{2\pi}}e^{-\frac{1}{2}(22.3-z)^2/1^2} \frac{1}{3\cdot \sqrt{2\pi}}e^{-\frac{1}{2}(z-20)^2/3^2} }{\int \Big[ \frac{1}{1 \cdot \sqrt{2\pi}}e^{-\frac{1}{2}(22.3-z)^2/1^2} \frac{1}{3\cdot \sqrt{2\pi}}e^{-\frac{1}{2}(z-20)^2/3^2} \Big]dz}$$

observe:

- the numerator (likelihood*prior) is a function of $z$.
- the normalization factor is a **number** since it is an integral over $z$ of a function of $z$
- $P(z|s_0=22.3m)$ is therefore a function of $z$ which is a probability distribution itself.


and finally, we can of course handle **new observations**, using the newly computed posterior as the prior of the next observation.

$$P(z|s_i) = \frac{P(s_i|z)P(s_{i-1})}{P(s)}$$


We are going to see this now in a notebook

LAB: Estimate the position with velocity and position estimates (i.e. do kalman filter by hand)



