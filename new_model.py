import matplotlib.pyplot as plt


S = [1000]
I = [1]
R = [0]
D = [0]
N = [S[-1]+I[-1]+R[-1]-D[-1]]

infection_rate = 1/4
recovery_rate = 1/8
mortality_rate = 2/100*recovery_rate
immunity_loss_rate = 1/90
mask_rate = 0.5
social_distancing_rate = 0.02

T_end = 1000

for t in range(1, T_end):
    dS = -1 * infection_rate*(1-0.35*mask_rate)*(1-0.65*social_distancing_rate) * (I[-1]*S[-1])/N[-1]+immunity_loss_rate*R[-1]
    dI = infection_rate*(1-0.35*mask_rate)*(1-0.65*social_distancing_rate) * (I[-1]*S[-1])/N[-1] - (recovery_rate+mortality_rate)*I[-1]
    dR = recovery_rate*I[-1]-immunity_loss_rate*R[-1]
    dD = mortality_rate*I[-1]

    S.append(S[-1] + dS)
    I.append(I[-1] + dI)
    R.append(R[-1] + dR)
    D.append(D[-1] + dD)
    N.append(S[-1]+I[-1]+R[-1]-D[-1])

fig, ax = plt.subplots()
# ax.scatter([t for t in range(T_end)], S)
# ax.scatter([t for t in range(T_end)], I)
# ax.scatter([t for t in range(T_end)], R)
ax.plot([t for t in range(T_end)], S)
ax.plot([t for t in range(T_end)], I)
ax.plot([t for t in range(T_end)], R)
ax.plot([t for t in range(T_end)], D)
ax.plot([t for t in range(T_end)], N)
ax.grid()
plt.show()
