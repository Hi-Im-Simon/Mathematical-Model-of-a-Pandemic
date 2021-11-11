# total initial population size
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
Mu = 3.6529 * 10**-5 # ovrall fatality rate, float

I_s = int(0.04 * N) # current amount of infected people with symptoms, int
I_a = int(0.01 * N) # current amount of infected people without symptoms, int
S = N - I_s - I_a # amount of not infected people, int
Q = 0 # amount of people in quarantine, int
R = 0 # amount of prople with immunity, int
D = 0 # amount of deaths, int
E = S

out = [S]

for i in range(10):
    dS = Rh - Bt_s * (1 - Ps * Xi) * S * I_s - Bt_a * (1 - Ps * Xi) * S * I_a - Mu * S
    #dE = Bt_s * (1 - Ps * Xi) * S * I_s + Bt_a * (1 - Ps * Xi) * S * I_a - ()
    S += int(dS)
    out.append(S)

#print(out)

