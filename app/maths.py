# total initial population size
N = 13680480 # current population, int

S = 0.75*N # susceptible class
I = int(0.005*N) # infected class
E = N-S-I # exposed class
Q = 0 # quarantined class
R = 0 # recovered class

Tht = 1.418243e-1 # recruitment rate into susceptible population
Mu = 5.389301e-2 # natural mortality rate
Dlt = 6.839696e-1 # infection death rate
Omg = 2.421307e-2 # progression rate from exposed to infectious class
Sgm = 2.104874e-1 # rate of loss of immunity
Tau = 8.270934e-1 # treatment rate for infectious individuals
Phi = 4.584931e-3 # treatment rate for quarantined individuals
Psi = 2.999373e-1 # proportion of individuals that maintain social distancing
Nu = 2.808803e-1 # usage of a face mask and a hand sanitiser by a portion of the population
Rho = 1.786530e-1 # rate of recovery from infection
Alph_c = 2.814715e-1 # effective transmission rate

S_out = [S]
E_out = [E]
I_out = [I]
Q_out = [Q]
R_out = [R]

for i in range(10):
    dS = Tht - (Alph_c*(1-Psi)*(1-Nu)*(E+I)*S)/N - Mu*S + Sgm*R
    dE = (Alph_c*(1-Psi)*(1-Nu)*(E+I)*S)/N - (Mu + Omg)*E
    dI = Omg*E - (Mu + Dlt + Rho + Tau)*I
    dQ = Rho*I - (Mu + Dlt + Phi)*Q
    dR = Phi*Q + Tau*I - (Sgm + Mu)*R

    S += int(dS)
    E += int(dE)
    I += int(dI)
    Q += int(dQ)
    R += int(dR)

    S_out.append(S)
    E_out.append(E)
    I_out.append(I)
    Q_out.append(Q)
    R_out.append(R)


print(S_out)
print(E_out)
print(I_out)
print(Q_out)
print(R_out)
