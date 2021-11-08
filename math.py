# total initial population size
N = 13680470

Rh = 5
Bt_s = 0.67
Bt_a = 0.74
Ps = 0.1
Xi = 0.5
La_s = 0.1
La_a = 0.1
La_q = 0.05
Al_s = 0.2
Al_a = 0.2
De_s = 0.015
De_q = 0.015
Mu = 3.6529 * 10**-5

I_s = int(0.04 * N)
I_a = int(0.01 * N)
# people not infected
S = N - I_s - I_a
Q = 0
R = 0
D = 0

out = [S]
dS = 0

for i in range(10):
    dS = Rh - Bt_s * (1 - Ps * Xi) * S * I_s - Bt_a * (1 - Ps * Xi) * S * I_a - Mu * S
    S += int(dS)
    out.append(S)

print(out)

