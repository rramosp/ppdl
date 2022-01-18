# ML models from a bayesian perspective

As a primer to what this means in machine learning. 

- What do you have right before you train a model? You have your data $D$(there might be some uncertainty due to the variability of the sampling or data acquisition process), and you know nothing about your parameters $\theta$ .

What is the meaning of $P(D|\theta)$ ?

- We fix some certain parameter values (for instance, a linear regression model with bias -0.3 = $\theta_0$ and slope 1.3 = $\theta_1$) and we are asking about the probability of the data that we have given those parameters.
- If you could choose between different $\theta$ which one would you choose? The ones with higher or lower $P(D|\theta)$? Why?  Probably the ones with high values, because you are saying I want the model that assigns to what I have just seen the highes probability of being seen. Which seems a reasonable assumption. $\rightarrow$ this is maximum likelihood estimation.

What is the meaning of $P(\theta|D)$ ?

- You fix the data $D$, and you are asking, what is the probability distribution (uncertainty in a bayes setting) of different model parameters?

Observe that:

- $P(\theta|D)$ is a distribution of model parameters, not a particular value of parameters (like when we train a model traditionally). It should represent our uncertainty about model parameters. A spreadout distribution would mean that, seeing the data (as a fact), we have a lot on uncertainty about what model parameters (values) are better and, thus, more difficult to make a choice.
- $P(D|\theta)$ is a distribution over the data.
- $P(D|\theta)$ is relatively easy to calculate (have your model output a probability distribution, like after softmax).
- $P(\theta|D)$ is very hard to calculate, since we **MUST** be able to assign a probability to each set of values for the parameters.

As we can use Bayes theorem in this setting as well, and help us with $P(\theta|D)$:

$P(\theta|D) = \frac{P(D|\theta)P(\theta)}{P(D)}$




