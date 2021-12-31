function calc(data) {
    let Tp = 1;  // sampling interval in days, assume default = 1 day

    let S = 1368048;  // susceptible compartment
    let I = 50;  // infected compartment
    let R = 0;  // recovered compartment
    let D = 0;  // deceased compartment
    let V = 0;  // vaccinated compartment

    let N_0 = S + I + R + D + V;  // max initial population size
    let N = S + I + R + V;  // total alive population size
    
    infection_rate = 1 / data.get('infection_period');
    recovery_rate = 1 / data.get('recovery_period');
    mortality_rate = data.get('mortality_rate') * 0.01 * recovery_rate;
    immunity_loss_rate = 1 / data.get('immunity_period');
    mask_rate = data.get('mask_rate') / 100;
    social_distancing_rate = data.get('social_distancing_rate') / 100;
    vaccination_rate = data.get('vaccination_rate_per_1k') / 1000;
    mask_effectiveness = data.get('mask_effectiveness') / 100;
    social_distancing_effectiveness = data.get('social_distancing_effectiveness') / 100;
    vaccine_efficacy = data.get('vaccine_efficacy') / 100;
    time = data.get('time');

    let R_zero = infection_rate / (recovery_rate + mortality_rate);  // basic reproduction number
    let R_e = (infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (S / N) + infection_rate * (1 - mask_effectiveness * mask_rate) * (1 - social_distancing_effectiveness * social_distancing_rate) * (1 - vaccine_efficacy) * (V / N)) / (recovery_rate + mortality_rate);  // effective reproduction number
    let herd_immunity = 100 * (1 - (1 / R_zero)) / vaccine_efficacy;  // herd immunity

    if (herd_immunity > 100) {
        herd_immunity = '∞';
    } else if (herd_immunity < 0) {
        herd_immunity = '0%';
    } else {
        herd_immunity = herd_immunity.toFixed(0);
        herd_immunity += '%';
    }

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
    
    return { 'S': S_out, 'I': I_out, 'R': R_out, 'D': D_out, 'V': V_out, 'N': N_out, 'R_zero': R_zero, 'R_e': R_e, 'herd_immunity': herd_immunity };
}