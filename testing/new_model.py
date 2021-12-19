import matplotlib.pyplot as plt


S = [100000]
I = [49]
R = [0]
D = [0]
V = [0]
N_0 = S[-1]+I[-1]+R[-1]+D[-1]+V[-1]
N = [N_0 - D[-1]]

infection_rate = 1/4
recovery_rate = 1/12
mortality_rate = 2/100*recovery_rate
immunity_loss_rate = 1/90
mask_rate = 0.1
social_distancing_rate = 0.02
mask_effectiveness = 0.5
social_distancing_effectiveness = 0.85
vaccination_rate = 1/1000
vaccine_efficacy = 0.76

R0 = (infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate))/(mortality_rate+recovery_rate)
R_t = ((1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*infection_rate*(S[-1]/N[-1]+(1-vaccine_efficacy)*V[-1]/N[-1]))/(mortality_rate+recovery_rate)
herd_immunity = (1-(1/R0))/vaccine_efficacy
print(herd_immunity)
print(R_t)
T_end = 365

for t in range(1, T_end):
    if (t == 34):
        social_distancing_rate = 0.95
        R_t = ((1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*infection_rate*(S[-1]/N[-1]+(1-vaccine_efficacy)*V[-1]/N[-1]))/(mortality_rate+recovery_rate)
        print(R_t)
    if (t == 100):
        social_distancing_rate = 0.01
        mask_rate = 0
        R_t = ((1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*infection_rate*(S[-1]/N[-1]+(1-vaccine_efficacy)*V[-1]/N[-1]))/(mortality_rate+recovery_rate)
        print(R_t)
    dS = -1 * infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate) * (I[-1]*S[-1])/N[-1]+immunity_loss_rate*R[-1] - vaccination_rate*S[-1]
    dI = infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate) * (I[-1]*S[-1])/N[-1] + (1-vaccine_efficacy)*infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*(I[-1]*V[-1]/N[-1]) - (recovery_rate+mortality_rate)*I[-1]
    dR = recovery_rate*I[-1]-immunity_loss_rate*R[-1]
    dD = mortality_rate*I[-1]
    dV = vaccination_rate*S[-1] - (1-vaccine_efficacy)*infection_rate*(1-mask_effectiveness*mask_rate)*(1-social_distancing_effectiveness*social_distancing_rate)*(I[-1]*V[-1]/N[-1])

    S.append(int(S[-1] + dS))
    I.append(int(I[-1] + dI))
    R.append(int(R[-1] + dR))
    D.append(int(D[-1] + dD))
    V.append(int(V[-1] + dV))
    N.append(int(S[-1]+I[-1]+R[-1]+V[-1]))

fig, ax = plt.subplots()
ax.plot([t for t in range(T_end)], S)
ax.plot([t for t in range(T_end)], I)
ax.plot([t for t in range(T_end)], R)
ax.plot([t for t in range(T_end)], D)
ax.plot([t for t in range(T_end)], V)
ax.plot([t for t in range(T_end)], N)
ax.grid()
plt.show()
