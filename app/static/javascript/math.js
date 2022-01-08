function calc(data) {
    let Tp = 1;  // sampling interval in days, assume default = 1 day

    let S = +data.get('susceptible_count');  // susceptible compartment
    let I = +data.get('infected_count');  // infected compartment
    let R = 0;  // recovered compartment
    let D = 0;  // deceased compartment
    let V = 0;  // vaccinated compartment

    let N_0 = S + I + R + D + V;  // max initial population size
    let N = S + I + R + V;  // total alive population size
    
    infection_rate = 1 / data.get('infection_period');
    recovery_rate = 1 / data.get('recovery_period');
    mortality_rate = data.get('mortality_rate') * 0.01 * recovery_rate;
    immunity_loss_rate = data.get('immunity_period') > 0 ? 1 / data.get('immunity_period') : 0; // if immunity_period > 0, return 1 / immunity_period, else return 0
    mask_rate = data.get('mask_rate') / 100;
    social_distancing_rate = data.get('social_distancing_rate') / 100;
    vaccination_rate = data.get('vaccination_rate_per_1k') / 1000;
    mask_effectiveness = data.get('mask_effectiveness') / 100;
    social_distancing_effectiveness = data.get('social_distancing_effectiveness') / 100;
    vaccine_efficacy = data.get('vaccine_efficacy') / 100;
    time = data.get('time');

    let S_out = [S], I_out = [I], R_out = [R], D_out = [D], V_out = [V], N_out = [N];

    for (let _ = 0; _ < time; _++) {
        S += Math.floor(-1 * infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (I * S) / N + immunity_loss_rate * R - vaccination_rate * S) * Tp;
        I += Math.floor(infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (I * S) / N + infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (1 - vaccine_efficacy) * (I * V / N) - recovery_rate * I - mortality_rate * I) * Tp;
        R += Math.floor(recovery_rate * I - immunity_loss_rate * R) * Tp;
        D += Math.floor(mortality_rate * I) * Tp;
        V += Math.floor(vaccination_rate * S - (1 - vaccine_efficacy) * infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (I * V / N)) * Tp;
        N += Math.floor(-1 * mortality_rate * I) * Tp;

        S_out.push(S); I_out.push(I); R_out.push(R); D_out.push(D); V_out.push(V); N_out.push(N);
    }
    
    return { 'S': S_out, 'I': I_out, 'R': R_out, 'D': D_out, 'V': V_out, 'N': N_out };
}