def do_math(d):
    # total initial population size
    N = 13680480 # current population, int

    S = 0.75*N # susceptible class
    I = int(0.005*N) # infected class
    E = N-S-I # exposed class
    Q = 0 # quarantined class
    R = 0 # recovered class
    
    Tht = float(d['infection_rate'])
    Mu = float(d['natural_mortality_rate'])
    Dlt = float(d['infection_death_rate'])
    Omg = float(d['exposed_to_infected_rate'])
    Sgm = float(d['immunity_loss_rate'])
    Tau = float(d['infected_treatment_rate'])
    Phi = float(d['quarantined_treatment_rate'])
    Psi = float(d['social_distancing_rate'])
    Nu = float(d['protection_usage_rate'])
    Rho = float(d['infected_recovery_rate'])
    Alph_c = float(d['transmission_rate'])
    
    
    t = int(d['_time'])

    S_out = [S]
    E_out = [E]
    I_out = [I]
    Q_out = [Q]
    R_out = [R]

    for _ in range(t-1):
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


    return([S_out, E_out, I_out, Q_out, R_out])
