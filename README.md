# Bachelors_Thesis



This is the code for my Bachelor's thesis.
Here, I used maximum likelihooed estimation to estimate an indiviuals learning rate after a subset of learning.

It is split in several parts parts:

## Simulation:

To produce a hypothesis, I simulated sigmoid learning curves according to a point-process model of learning.

First, I varied parameters associated with complexity of the learning material and individual leanring rate.
In a second step, I used maximum likelihood estimation to retrieve the learning rate based on the material complexity alone.

![simulation](Plots/Simulation_Fig1.png)

## Preprocessing:

This is the code that I used to clean the data.

## Analysis

This is code I used to estimate learning rates in a real learning curves from a vocabulary leanring task.

**analysis_by_parameter.py** replicates the analysis from the simulation.

![hist](Plots/Hist_param_Fig2.png)

**analysis_over_trials.py** analysis how accuracy of leanring rate estimates changes over trials/ time.

![red](Plots/Red_Fig3.png)


### Discussion

Entails code to illustrate explanations in the work.

Why there is a linear trend in the simulation.
![tail](Plots/tail_Fig4.png)

The effects of discrete recall measures on the accuracy of leanring rate estimates.
![discrete](Plots/discrete_Fig5.png)
