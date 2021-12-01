# A Mathematical Model of a Pandemic
This project's aim is to model the progression of a pandemic in a population given certain initial parameters. In order to accomplish this, a basic SIR model[^1] has been used to design a new model that is able to predict the progression of a pandemic within defined accuracy. The system is modelled after the COVID-19 pandemic, although its modularity allows it to be used in other circumstances.

## Variables
The SIRD model (_Susceptible-Infected-Recovered-Deceased_) divides the total population $N$ into following compartments:
* Susceptible compartment $S(t)$,
* Infected compartment $I(t)$,
* Recovered compartment $R(t)$,
* Deceased compartment $D(t)$.

The total population at a given time $t$ can be expressed by a simple summation:

$$ N(t) = S(t) + I(t) + R(t). $$

## Parameters
Parameters used in the model:
* $\beta$ – basic infection rate,
* $\gamma$ – recovery rate,
* $\mu$ – mortality rate,
* $\sigma$ – immunity loss rate,
* $\phi$ – percentage of population correctly using face coverings (e.g. masks); $0 \leq \phi \leq 1$,
* $\theta$ – mask effectiveness rate defined as a projected decrease in infection rate; $0 \leq \theta \leq 1$, assumed $\theta = 0.5$,
* $\delta$ – percentage of population isolating (e.g. lockdown measures, stay-at-home orders); $0 \leq \delta \leq 1$,
* $\eta$ – isolation effectiveness rate defined as a projected decrease in infection rate; $0 \leq \eta \leq 1$, assumed $\eta = 0.85$.

## Differential equations
The following set of differential equations are used in the model:

$$\frac{dS}{dt} = -(1-\phi\theta)(1-\delta\eta)\beta \frac{IS}{N} + \sigma R,$$
$$\frac{dI}{dt} = (1-\phi\theta)(1-\delta\eta)\beta \frac{IS}{N} - (\gamma + \mu)I,$$
$$\frac{dR}{dt} = \gamma I - \sigma R,$$
$$\frac{dD}{dt} = \mu I.$$

The change of total population $N$ at a time $t$ is defined as

$$ \frac{dN}{dt} = \frac{dS}{dt} + \frac{dI}{dt} + \frac{dR}{dt}$$

which simplifies to

$$ \frac{dN}{dt} = -\mu I.$$

## References
[^1]: I. Cooper, A. Mondal and C. G. Anthonopoulos, "A SIR model assumption for the spread of COVID-19 in different communities", _Chaos, Solitons & Fractals_, vol. 139, 2020.