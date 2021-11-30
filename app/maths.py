def do_math(d):
    # total initial population size
    N = 13680480 # current population, int
    Tp = 1 # sampling interval in days, assume default = 1


    S = N - int(0.0005*N) - int(0.06*N) # susceptible class
    E = 0 # exposed class
    I = int(0.0005*N) # infected class
    Q = int(0.06*N) # quarantined class
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
    N_out = [N]

    for _ in range(t-1):
        dS = (Tht - (Alph_c*(1-Psi)*(1-Nu)*(E+I)*S)/N - Mu*S + Sgm*R)*Tp
        dE = ((Alph_c*(1-Psi)*(1-Nu)*(E+I)*S)/N - (Mu + Omg)*E)*Tp
        dI = (Omg*E - (Mu + Dlt + Rho + Tau)*I)*Tp
        dQ = (Rho*I - (Mu + Dlt + Phi)*Q)*Tp
        dR = (Phi*Q + Tau*I - (Sgm + Mu)*R)*Tp
        dN = (Tht - Mu*N - Dlt*(I+Q))*Tp

        S += int(dS)
        E += int(dE)
        I += int(dI)
        Q += int(dQ)
        R += int(dR)
        N += int(dN)

        S_out.append(S)
        E_out.append(E)
        I_out.append(I)
        Q_out.append(Q)
        R_out.append(R)
        N_out.append(N)


    return([S_out, E_out, I_out, Q_out, R_out, N_out])
