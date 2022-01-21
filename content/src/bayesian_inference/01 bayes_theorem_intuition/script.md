# Bayes theorem

Bayes theorem is at the root of Bayesian inference. 

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
Its formulation simplicity might be misleading (engañosa) and what is hard is not to derive the formula, but to properly own its interpretation and apply it in different contents.

Let's get down to it. Two key things to remember on Bayesian inference:

- Probability is interpreted as belief, **not as an actual truth**. It represents our knowledge and uncertainty about something. It is very important to slow down and allow this to sink in well in our understanding. If **I KNOW** that it is going or has rain, then $P(rain)=1$. If, by whatever reason I am only 50% sure of that, then $P(rain)=0.5$.
- Probability is updated as our uncertainty changes. When does our uncertainty change? When we have new observations, evidence, facts. 

[<font color="red">_making pickture_</font>] Our working example $P(rain)=0.4$, $P(sun)=0.5$, $P(rain\text{ and }sun)=0.2$ ... observe $P(¬rain\text{ and }¬sun)=0.1$


**QUESTION**. what is the value and meaning of expression $P(sun|rain)$ ? 

- $rain$ becomes a **FACT** $\rightarrow$ we have to act **AS IF** $P(rain)$ becomes 1 so (1) everything outside dissapears and (2) everying inside must be scaled accordingly. [<font color="red">anim transforming circle 0.4 into 1.0</font>]
-  How much should be scale $P(sun|rain)$?? 0.2 is half 0.4, so if 0.4 becomes 1, 0.2 becomes 0.5 so that proportions are kept.
-  $P(sun|rain)=P(sun\text{ and }rain) / P(rain)$

<font color="red">animation to convert the formulas into bayes theorem</font>

likewise with $P(rain|sun) = P(sun\text{ and }rain) / P(sun)$

if we arrange both calculations we obtain Bayes theorem:

$P(sun|rain)P(rain) = P(sun\text{ and }rain) = P(rain|sun)P(sun)$

<font color="red">animation to substitute $rain$ and $sun$ by $A$ and $B$.</font>

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



