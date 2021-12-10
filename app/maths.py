def do_math(d):
    Tp = 1  # sampling interval in days, assume default = 1 day


    S = 1368048  # susceptible compartment
    I = 50  # infected compartment
    R = 0  # recovered compartment
    D = 0  # deceased compartment
    V = 0  # vaccinated compartment

    N_0 = S + I + R + D + V  # max initial population size
    N = S + I + R + V  # total population size
    
    
    infection_rate = float(d['infection_rate'])
    recovery_rate = float(d['recovery_rate'])
    mortality_rate = float(d['mortality_rate'])
    immunity_loss_rate = float(d['immunity_loss_rate'])
    mask_rate = float(d['mask_rate'])
    social_distancing_rate = float(d['social_distancing_rate'])
    mask_effectiveness = float(d['mask_effectiveness'])
    social_distancing_effectiveness = float(d['social_distancing_effectiveness'])
    vaccination_rate = float(d['vaccination_rate'])
    vaccine_efficacy = float(d['vaccine_efficacy'])
    
    t = int(d['_time'])

    S_out = [S]
    I_out = [I]
    R_out = [R]
    D_out = [D]
    V_out = [V]
    N_out = [N]

    for _ in range(t-1):
        dS = (-1 * infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate) * (I*S)/N_0+immunity_loss_rate*R - vaccination_rate*S) * Tp
        dI = (infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate) * (I*S)/N_0 + (1-vaccine_efficacy)*infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*(V/N_0) - (recovery_rate+mortality_rate)*I) * Tp
        dR = (recovery_rate*I-immunity_loss_rate*R) * Tp
        dD = (mortality_rate*I) * Tp
        dV = (vaccination_rate*S - (1-vaccine_efficacy)*infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*(V/N_0)) * Tp
        dN = (dS + dI + dR + dV) * Tp

        S += int(dS)
        I += int(dI)
        R += int(dR)
        D += int(dD)
        V += int(dV)
        N += int(dN)

        S_out.append(S)
        I_out.append(I)
        R_out.append(R)
        D_out.append(D)
        V_out.append(V)
        N_out.append(N)


    return([S_out, I_out, R_out, D_out, V_out, N_out])
