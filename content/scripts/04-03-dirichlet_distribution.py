# %% [markdown]
# # Dirichlet Distribution
#
# This notebook presents an introduction to the Dirichlet distribution, and some applications for it.
#
# First, let us import the required libraries:

# %%
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_probability as tfp
from ipywidgets import interact, FloatLogSlider
from ppdl.samplers import AnimalsFrequenciesSampler

tfd = tfp.distributions

# %% [markdown]
# ## Properties
#
# The Dirichlet distribution is mainly used in Bayesian statistics, specially, it's the conjugate of the multinomial and the categorical distributions. In the following list you can find some relevant concepts from this distribution:
#
# * It's a multivariate distribution over a random vector $\mathbf{x} \in \mathbb{R}^K$ such that each component takes values in:
#
# > $x_i \in [0, 1]$.
#
# * The support for this distribution is constrained to be a simplex, i.e.:
#
# > $\sum_i{x_i} = 1$.
#
# * The probability density function is given by:
#
# > $\text{P}(\mathbf{x}) = \frac{1}{\beta(\mathbf{\alpha})} \prod_{i = 1} ^ K x_i ^ {\alpha - 1}$
#
# * It's a multivariate generalization of the Beta distribution.
#
# * It has a vector of parameters $\alpha \in \mathbb{R} ^ K$ which controls the `sparsity` of the distribution.
#
# Let us show an emample of samples generated from the Dirichlet distribution for different $\alpha$ values:

# %%
def plot_dirichlet_samples(alpha, n_samples=10000):
    """
    3D plot for samples from the Dirichlet distribution.

    Parameters
    ----------
    alpha : array_like
        Parameters of the Dirichlet distribution.
    n_samples : int
        Number of samples to generate.
    """
    dim = 3
    dist = tfd.Dirichlet(
        concentration=np.ones((dim, )) * alpha
        )
    sample = dist.sample(n_samples).numpy()
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.scatter3D(*(sample[:, i] for i in range(dim)), alpha=0.5)
    ax.view_init(45, 10)
    ax.set_title(f"$\\alpha = {alpha:.3f}$") 

# %%
interact(plot_dirichlet_samples, alpha=FloatLogSlider(min=-2, max=2));

# %% [markdown]
# ## Example
#
# Similar to the Beta distribution, the Dirichlet distribution is used to model rates, multivariate proportions or variables in $[0, 1]$.
#
# Let us consider the following example:
#
# > In a survey, we measured the relative frequencies of pets per house, the experiment considered the following animals:
#
# * Dog
# * Cat
# * Bird
# * Fish
#
# Let us generate a sample for this problem

# %%
sampler = AnimalsFrequenciesSampler()

# %%
sample = sampler(n_samples=1000, seed=42)
sample

# %% [markdown]
# We can verify that this sample contains relative frequencies as follows:

# %%
print(
        sample
        .drop(columns=["house"])
        .sum(axis=1)
        )

# %% [markdown]
# Let us solve this problem using MLE over the Dirichlet distribution:

# %%
@tf.function
def neg_log_lik(dist, data):
    logs = dist.log_prob(data)
    return -tf.reduce_sum(logs)

# %% [markdown]
# The distribution using `tfp`:

# %%
parameters = tf.Variable(
        np.ones((4, )) * 0.1,
        )
dist = tfd.Dirichlet(
        concentration=parameters
        )
sample_numpy = (
        sample
        .drop(columns=["house"])
        .to_numpy()
        )

# %% [markdown]
# We can now solve the problem using automatic differentiation:

# %%
# Add note about numerical issues
iters = 1000
optimizer = tf.optimizers.Adam(learning_rate=0.01)

for iter in range(iters):
    with tf.GradientTape() as t:
        neg_log_lik_value = neg_log_lik(dist, sample_numpy)
        t.watch(dist.trainable_variables)
    print(f"Iteration {iter + 1}/{iters}, loss = {neg_log_lik_value.numpy():.3f}")
    gradients = t.gradient(neg_log_lik_value, dist.trainable_variables)
    optimizer.apply_gradients(zip(gradients, dist.trainable_variables))

# %% [markdown]
# We can now verify that the parameters of the Dirichlet distribution:

# %%
print(dist.concentration)

# %% [markdown]
# We can generate a sample, and verify that the relative frequencies are as expected:

# %%
sample_dirichlet = (
        dist
        .sample(1000)
        .numpy()
        )

# %%
print(sample_numpy.mean(axis=0))
print(sample_dirichlet.mean(axis=0))

# %%
print(sample_numpy.std(axis=0))
print(sample_dirichlet.std(axis=0))


# %%
