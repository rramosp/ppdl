# distributions

Recall that in probabilistic progamming we are swiching from dealing with numbers (or individuals) to dealing with distributions (populations of individuals).

Here we use the term **individual** in a very generic way, it could be row in a table of data representing a person, or a house, it could be a set of values at the output of some layer in a neural network, it could be the weights of that layer, etc.

Distributions are more complex objects that numbers. A number is just that, a number. A distribution cn be best described with a PDF (probability density function for a continutous distribution), or a PMF (probability mass function, for a discrete distribution)

Therefore, everything we do with distributions is harder. But of course, we can do so many more things with distributions than with numbers.

Let's see some examples, as we have been seing during the course:

- We could have a model whose output when after being fed an input is a distributions. For instance, instead of predicting a house price after seeing a set of featurs of the house, we can have a model predicting a distribution, from that input. This will be a predictive distribution. With this we could: measure the uncertainty the model places in the prediction and in, general, have more posibilities when using the prediction in real life **example with a multimodal predictive distribution on the house price** (select mean, etc.)  This model would output a **different** distribution for each input data item (each house).

- We could have a model whose output **after seeing the full dataset** is a distribution. We would not be able to make individual predictions, but we would have a notion of the probability of each input data (i.e. density estimation, anomaly detection)

- We could have a model whose input are samples of a known distribution (a simple one, such as a normal 0,1) and, for each input sample, it produces a single output


---
what is a latent variable?
- sometimes this refers to the parameters of a model that we want to find out. This is more frequent in statistics texts.
- sometimes this referes to intermediate representations of the data (for instance, the output of intermediate layers). This is more frequent in ML texts.