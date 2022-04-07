# Bayes theorem

but let's stop and understand what this means

<font color="red">animation inverse to substitute $rain$ and $sun$ by $A$ and $B$.</font>

- $P(sun|rain)P(rain)$: it is obviously the probability of both rain and sun according to the formulas above. 
- Another way to look at it: we are in the world where $rain$ has been confirmed and we are expressing our belief about $sun$ ($P(sun|rain)$) $\rightarrow$ how do we transform this belief into a world where $rain$ has **NOT** been confirmed? 
- This is, If I start with $P(sun|rain)$, What can I say about $sun$ and $rain$ in a world where $rain$ has **NOT** been confirmed? [<font color="red">show diagram with only $rain$ and $sun|rain$</font>] ... I cannot state anything about $¬rain$ because I have no information about it. Somewhat, $P(sun\text{ and }rain)$ is the best I can do

observe the game we are playing: What happens if I gain some information (observed that rains)? What happens if I loose information (move to a world where rain has **NOT** been confirmed). 

- the equation $P(sun|rain)=P(sun\text{ and }rain) / P(rain)$ represents the case when we **GAIN** information (observed $rain$)
- the equation $P(sun\text{ and }rain)=P(sun|rain)P(rain)$ represents the case when we want to **INTEGRATE** the information gained into a larger context where $rain$ has not been confirmed.
- observe that this is just a very simple algebraic manipulation ... but its interpretation is **VERY** profound.

## This is bayesian thinking!!!!



