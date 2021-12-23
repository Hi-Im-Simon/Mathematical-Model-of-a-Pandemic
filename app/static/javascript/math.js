function calc(data) {
    Tp = 1;  // sampling interval in days, assume default = 1 day

    S = 1368048;  // susceptible compartment
    I = 50;  // infected compartment
    R = 0;  // recovered compartment
    D = 0;  // deceased compartment
    V = 0;  // vaccinated compartment

    N_0 = S + I + R + D + V;  // max initial population size
    N = S + I + R + V;  // total alive population size
    
    infection_rate = data.get('infection_rate');
    recovery_rate = data.get('recovery_rate');
    mortality_rate = data.get('mortality_rate');
    immunity_loss_rate = data.get('immunity_loss_rate');
    mask_rate = data.get('mask_rate');
    social_distancing_rate = data.get('social_distancing_rate');
    mask_effectiveness = data.get('mask_effectiveness');
    social_distancing_effectiveness = data.get('social_distancing_effectiveness');
    vaccination_rate = data.get('vaccination_rate');
    vaccine_efficacy = data.get('vaccine_efficacy');

    time = data.get('_time');

    S_out = [S];
    I_out = [I];
    R_out = [R];
    D_out = [D];
    V_out = [V];
    N_out = [N];

    for (let _ = 0; _ < time - 1; _++) {
        dS = (-1 * infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (I * S) / N + immunity_loss_rate * R - vaccination_rate * S) * Tp;
        dI = (infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * ((I * S) / N + (1 - vaccine_efficacy) * (I * V / N)) - (recovery_rate + mortality_rate) * I) * Tp;
        dR = (recovery_rate * I - immunity_loss_rate * R) * Tp;
        dD = (mortality_rate * I) * Tp;
        dV = (vaccination_rate * S - (1 - vaccine_efficacy) * infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (I * V / N)) * Tp;
        dN = (-1 * mortality_rate * I) * Tp;

        S += Math.floor(dS);
        I += Math.floor(dI);
        R += Math.floor(dR);
        D += Math.floor(dD);
        V += Math.floor(dV);
        N += Math.floor(dN);

        S_out.push(S);
        I_out.push(I);
        R_out.push(R);
        D_out.push(D);
        V_out.push(V);
        N_out.push(N);
    }
    
    return { 'S': S_out, 'I': I_out, 'R': R_out, 'D': D_out, 'V': V_out, 'N': N_out };
}