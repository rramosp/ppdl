# %% [markdown]
# # Variational Inference for Text Modeling
#
# In this notebook, we will implement the variational inference algorithm for topic modeling using a neural network and Latent Dirichlet Allocation (LDA). We'll review the bayesian concepts behind LDA, and its implementation using tensorflow probability.
#
# First, let us import the necessary libraries.

# %%
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_probability as tfp
from collections import Counter

tfd = tfp.distributions
tfb = tfp.bijectors
plt.style.use("ggplot")

# %% [markdown]
# ## Distributions in a Corpus of Documents
#
# Let us consider the following simple corpus of documents:

# %%
corpus = [
    "the cat sat on the mat the mat was on the cat the cat was on the mat",
    "the dog sat on the mat the mat was on the dog the dog was on the mat",
    "when the cat was on the roof the roof was on the cat the cat was on the roof",
    "the bird sang a song the song sang the bird the bird sang a song"
    ]

# %% [markdown]
#
# First, we'll compute the words distribution for a the first document in the corpus.
#
# Let us tokenize the document into words by splitting on the space characters:

# %%
words = corpus[0].split()
print(words)

# %% [markdown]
# Next, we'll compute words occurences in the document and the vocabulary:

# %%
counts = Counter(words)
vocab = np.array(list(counts.keys()))
print(vocab)
print(counts)

# %% [markdown]
# Finally, we'll estimate the parameters of the multinomial distribution for this document:

# %%
dist_params = tf.Variable(list(counts.values()))
dist_params = dist_params / tf.reduce_sum(dist_params)

document_dist = tfd.Multinomial(
        total_count=float(len(vocab)),
        probs=dist_params,
        )
print(document_dist)

# %% [markdown]
# Using this distribution, we can sample documents counts with the counts distribution of the first document:

# %%
sample = document_dist.sample(10)
print(sample)

# %% [markdown]
# We can convert the sample into a list of words, here, We repeat each word in the vocabulary the number of times it appears in the `sample` matrix:

# %%
sample_np = (
        sample
        .numpy()
        .astype("int")
        )

for sample_id, doc_counts in enumerate(sample_np):
    print(f"Sample {sample_id}: ", end="")
    for i, count in enumerate(doc_counts):
        if count > 0:
            print(" ".join([vocab[i]] * count), end=" ")
    print()

# %% [markdown]
# Now, We'll compute the parameters of the multinomial distribution for each document in the corpus. 
#
# First, we'll compute the vocabulary for the corpus:

# %%
vocab = np.unique(
        np.concatenate([
            np.array(doc.split())
            for doc in corpus
            ])
        )
print(vocab)

# %% [markdown]
# Also, we need a mapping from the vocabulary to the indices of the parameters.

# %%
word2idx = {w: i for i, w in enumerate(vocab)}

# %% [markdown]
# We can compute the counts for each document:

# %%
words = list(map(lambda doc: doc.split(), corpus))
print(words)

# %%
tokens = [[word2idx[w] for w in doc] for doc in words]
print(tokens)

# %%
counts = list(map(Counter, tokens))
print(counts)

# %% [markdown]
# We can now compute the parameters of the multinomial distribution for each document:

# %%
params = np.zeros((len(corpus), len(vocab)))
for i, doc in enumerate(counts):
    params[i, list(doc.keys())] = list(doc.values())
params = params / params.sum(axis=1, keepdims=True)
print(params)

# %% [markdown]
# The distribution for each document in the corpus:

# %%
document_dist = tfd.Multinomial(
        total_count=float(len(vocab)),
        probs=params
        )
print(document_dist)

# %% [markdown]
# Let us generate two sample corpuses from the distribution:

# %%
sample = document_dist.sample(2)
sample_np = (
        sample
        .numpy()
        .astype("int")
        )
print(sample_np)

# %%
for sample_id, sample in enumerate(sample_np):
    print(f"Sample {sample_id}: ")
    for document_id, doc_counts in enumerate(sample):
        print(f"\tDocument {document_id}: ", end="")
        for i, count in enumerate(doc_counts):
            if count > 0:
                print(" ".join([vocab[i]] * count), end=" ")
        print()

# %% [markdown]
# This approach always generates a corpus with 4 documents that have the same distribution of the original documents. However, there are some questions that enmark some limitations of this approach:
#
# * What would happen if we had a large corpus?
#
# > Under this approach, we would have to sample the distribution for each document in the corpus. This would be a very expensive operation.
#
# * What happens to documents with similar distributions, is it necessary to save equivalent vectors multiple times?
#
# > We would have to save the same vector multiple times. Which is memory inefficient.
#
# * Is there any way to generate a corpus with a different number of documents?
#
# > There is no way to generate a corpus with a different number of documents, since we have positional distributions for a fixed-length corpus.
#
# To address these problems, we can use a distribution for the parameters of the multinomial distribution (Bayesian modeling), which allows us to: save the parameters for the parameters' distribution only; summarize multiple distributions in one; and to generate corpuses with different number of documents.
#
# However, what kind of distribution is the parameters' distribution?
#
# > Let us recap about Bayesian conjugates. First, consider the Bernoulli distribution (special case of the Multinomial distribution), its conjugate is the Beta distribution. We need a multivariate distribution that generalizes the beta distribution and that can be used for the Multinomial's parameters distribution (Dirichlet).

# %% [markdown]
# ## Bayesian Modeling for the Corpus Distribution
#
# Let us implement the following two-level hierarchical model for the corpus distribution:
#
# $$
# p \sim Dirichlet(\alpha)\\
# x \sim Multinomial(p)
# $$

# %%
corpus_dist = tfd.JointDistributionNamed(
        {
            "p": tfd.Dirichlet(
                concentration=tf.Variable(tf.ones(len(vocab)))
                ),
            "x": lambda p: tfd.Multinomial(
                total_count=float(len(vocab)),
                probs=p
                )
            }
        )

# %% [markdown]
# We can generate some samples from this distribution, notice that the `JointDistributionNamed` object generates a sample for each of the levels:

# %%
sample = corpus_dist.sample(10)
print(sample)

# %% [markdown]
# Let's view the corpus for this case:

# %%
sample_np = corpus_dist.sample(10)["x"].numpy().astype("int")
for document_id, doc_counts in enumerate(sample_np):
    print(f"\tDocument {document_id}: ", end="")
    for i, count in enumerate(doc_counts):
        if count > 0:
            print(" ".join([vocab[i]] * count), end=" ")
    print()

# %% [markdown]
# We can solve this problem using variational inference, in this matter, We would need a surrogate posterior distribution, whose parameters can be easily estimated with tensorflow's automatic differentiation.

# %%
surrogate_posterior = tfd.JointDistributionNamedAutoBatched({
    "p": tfb.Sigmoid()(
        tfd.Normal(
            loc=tf.Variable(tf.ones(len(vocab))),
            scale=tf.ones(len(vocab))
            )
        )
    })

# %% [markdown]
# We need the bag-of-words representation of the corpus:

# %%
counts_mat = np.zeros((len(corpus), len(vocab)))
for i, doc in enumerate(counts):
    counts_mat[i, list(doc.keys())] = list(doc.values())
counts_mat = tf.constant(counts_mat, dtype=tf.float32)

# %% [markdown]
# We can now compute the log-likelihood of the corpus distribution:

# %%
def log_prob(p):
    return corpus_dist.log_prob({"p": p, "x": counts_mat})

# %% [markdown]
# Finally, we solve the problem using variational inference:

# %%
optimizer = tf.optimizers.Adam(learning_rate=1e-3)
loss = tfp.vi.fit_surrogate_posterior(
        target_log_prob_fn=log_prob,
        surrogate_posterior=surrogate_posterior,
        optimizer=optimizer,
        num_steps=int(1e3),
        )

# %% [markdown]
# Let's view a sample of documents:

# %%
params = surrogate_posterior.sample(10)["p"].numpy()
params = params / params.sum(axis=1, keepdims=True)
dist = tfd.Multinomial(
        total_count=float(len(vocab)),
        probs=params
        )

# %%
sample_np = dist.sample(4).numpy().astype("int")
for sample_id, sample in enumerate(sample_np):
    print(f"Sample {sample_id}: ")
    for document_id, doc_counts in enumerate(sample):
        print(f"\tDocument {document_id}: ", end="")
        for i, count in enumerate(doc_counts):
            if count > 0:
                print(" ".join([vocab[i]] * count), end=" ")
        print()
