# Django Website for Sampling from High Dimensional Space

This repository contains the integration of [sampling from high dimensional space with complex, non-linear constraints](https://github.com/karthikncsu/Sampling-from-high-dimensional-space) program into Django web framework to demo the sampler. The website provides options of selecting one of the methods from the following four methods

1) Sequential Monte Carlo (SMC)
2) Gibbs Sampler (Gibbs)
3) Adaptive Metropolis (AdaptiveMetropolis)
4) Metropolis Random Walk (Metropolis)

and one of the following examples can be selected

1) Mixture
2) Example
3) Formulation
4) Alloy

The required packages to run this program is available in Pipfile
### Demo

The program is hosted on the Heroku server and below is the link for the website to try out different options for sampling.

[Django Website](https://sheltered-eyrie-03969.herokuapp.com/)

Due to the limitation of the Heroku server, the cases with a computational time of more than 30 seconds give a time-out error.  The issue will be resolved in the future and the website can be used to solve any case. In the mean while, please try other cases.

Below is the link for the Git repository of the sampling from high-dimensional space.

[GitHub code for sampling from high dimensional space](https://github.com/karthikncsu/Sampling-from-high-dimensional-space)

