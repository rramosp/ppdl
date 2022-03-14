# Bayes theorem

**[00:00]** Bayes theorem is at the root of Bayesian inference. 


**[00:11]**
  $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

**[00:30]** Its formulation simplicity might be misleading (engañosa) and what is hard is not to derive the formula, but to properly own its interpretation and apply it in different contents.

**[00:35]** [<font color="red"> highlight **A** if i know **B** </font>]

**[00:45]** [<font color="red"> Change scene and split screen in half with the two key elements </font>] Let's get down to it. Two key things to remember on Bayesian inference:

- **[01:36]** Probability is interpreted as belief, **not as an actual truth**. It represents our knowledge and uncertainty about something. It is very important to slow down and allow this to sink in well in our understanding. If **I KNOW** that it is going or has rain, then $P(rain)=1$. If, by whatever reason I am only 50% sure of that, then $P(rain)=0.5$.
-  **[02:45]** Probability is updated as our uncertainty changes. When does our uncertainty change? When we have new observations, evidence, facts. <font color="red"> [list examples] </font>

**[04:09]** <font color="red"> [Change scene for example sun and rain] </font>

**[04:15]** [<font color="red">_making pickture_</font>] Our working example $P(rain)=0.6$, $P(sun)=0.4$, $P(rain\text{ and }sun)=0.3$ ... observe $P(¬rain\text{ and }¬sun)=0.1$ 
 
 <font color="red">{Graphs fading in and out when he talks about other posibilities (fog, hail (granizo ) within the universe)} </font>  
 **[05:43]** <font color="red"> [animate fog diagram intercepted with sun and rain] </font>  
 **[05:50]** <font color="red">[animate hail (granizo) diagram intercepted with rain] </font>  
 

**[06:18]** <font color="red"> animate next line. Fade in and out text with value and meaning of the expression </font>

**QUESTION**. what is the value and meaning of expression $P(sun|rain)$ ? 

<font color="red">{Graphs to explain what happens if rain is observed} </font>  
**[06:37]** <font color="red">Highlight the right side of the expression</font>  
**[06:47]** <font color="red"> Fade in and out an eye to examplify an observation</font>   

- **[07:18]** $rain$ becomes a **FACT** $\rightarrow$ we have to act **AS IF** $P(rain)$ becomes 1 so (1) everything outside dissapears and (2) everying inside must be scaled accordingly. [<font color="red">anim transforming circle 0.6 into 1.0</font>]
- **[07:56]** How much should be scale $P(sun|rain)$?? 0.2 is half 0.4, so if 0.4 becomes 1, 0.2 becomes 0.5 so that proportions are kept.
- **[08:22]** $P(sun|rain)=P(sun\text{ and }rain) / P(rain)$
- **[08:49]** $\frac{0.3}{0.6} = 0.5$
- **[09:01]** $P(rain|sun)=\frac{P(sun\text{ and }rain)}{P(sun)}=\frac{0.3}{0.4}=0.75$
- **[09:30]** 

<font color="red">animation to convert the formulas into bayes theorem</font>

likewise with $P(rain|sun) = P(sun\text{ and }rain) / P(sun)$

if we arrange both calculations we obtain Bayes theorem:

$P(sun|rain)P(rain) = P(sun\text{ and }rain) = P(rain|sun)P(sun)$

<font color="red">animation to substitute $rain$ and $sun$ by $A$ and $B$.</font>
