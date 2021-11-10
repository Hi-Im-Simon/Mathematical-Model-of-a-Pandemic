init_values = {
    'mask_rate': 0.1,
    'mask_fall_rate': 0.5,
}

# initial values
N = 13680470 # current population, int

Rh = 5
Bt_s = 0.67
Bt_a = 0.74
Ps = 0.1 # % wearing masks, float
Xi = 0.5 # % infected fall because of masks, float
La_s = 0.1 # % for symptomatic people to get healthy, float
La_a = 0.1 # % for asymptomatic people to get healthy, float
La_q = 0.05 # % for people in quarantine people to get healthy, float
Al_s = 0.2 # % of symptomatic people isolating, float
Al_a = 0.2 # % of asymptomatic people isolating, float
De_s = 0.015 # fatafatality rate for symptomatic people, float
De_q = 0.015 # fatality rate for people in quarantine, float
Mu = 0.000036529 # ovrall fatality rate, float

I_s = int(0.04 * N) # current amount of infected people with symptoms, int
I_a = int(0.01 * N) # current amount of infected people without symptoms, int
S = N - I_s - I_a # amount of not infected people, int
Q = 0 # amount of people in quarantine, int
R = 0 # amount of prople with immunity, int
D = 0 # amount of deaths, int
