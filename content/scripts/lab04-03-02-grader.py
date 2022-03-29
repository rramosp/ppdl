# %% [markdown]
# # Lab 04.03.2: Topic Modeling using Neural Networks and Variational Inference

# %%
## Ignore this cell
!pip install ppdl==0.1.5 rlxmoocapi==0.1.0 --quiet

# %%
import inspect
from rlxmoocapi import submit, session

# %% [markdown]
# ## Task 1:
#
# Preprocessing for the text data:
# * Convert strings to lowercase
# * Remove special characters, numbers, and punctuation.
# * Remove stopwords.

# %% [markdown]
# ## Task 2:
#
# Implement an encoder model that generates topics (last layer must be a Dirichlet distrubution) from word counts.

# %% [markdown]
# ## Task 3:
#
# Implement a decoder model that generates words from topics.

# %% [markdown]
# ## Task 4:
#
# Implement a function that generates the prior distribution over topics.

# %% [markdown]
# ## Task 5:
#
# Implement the ELBO function that must be optimized

# %% [markdown]
# ## Task 6:
#
# Train the model.

# %% [markdown]
# ## Task 7:
#
# Extract the topics from the trained model and a subsample of the data.

# %% [markdown]
# ## Task 8:
#
# Extract the most meaningful words from each topic
