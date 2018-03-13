# Markov Chain
## Definition
### An Example:
<p align="center">
<img   src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Finance_Markov_chain_example_state_space.svg/400px-Finance_Markov_chain_example_state_space.svg.png"    title="wiki/Markov_chain"  > 
</p>

The above picture : arrows mean the probabilities of the next week's market state.   
Picture can translate into a matrix:  

/|bull | bear | stagnant
---|---|---|---
**bull**|0.9|0.075|0.025
**bear**|0.15|0.8|0.05
**stagnant**|0.25|0.25|0.5

### let's say this week is bear week, so what's the probability of bull market on the fourth week.  

### Answer: 

**1st week:**  bear week 
 
**2nd week:** lest week is bear week ,so this week   
    
/|bull | bear | stagnant
---|---|---|---  
**bear**|0.15|0.8|0.05

bull week : P=**0.15**  
bear week:P=**0.8**  
stagnant week:P=**0.05**  
 
**3rd week:** this week is depend on last week(bull=0.15,bear=0.8,stagnant=0.05)
bull week: (bull,bear,stagnant) to bull :P = **0.15\*0.9 + 0.8\*0.15 + 0.05\*0.25 = 0.2675**  
bear week: P = **0.15\*0.075 + 0.8\*0.8 + 0.05\*0.25 = 0.66375**  
stagnant week: P = **0.15\*0.025 + 0.8\*0.05 + 0.05\*0.5 = 0.06875** 
 
**4th week:** bull week  
(bull,bear,stagnant) to bull: P = **0.2675\*0.9 + 0.66375\*0.15 + 0.06875\*0.25 = 0.3575**  

So we can see the current week is only depend on last week ,has nothing to do with the week before last week.