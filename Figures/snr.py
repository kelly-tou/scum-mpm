import numpy as np
from numpy import linalg as LA
import math
import matplotlib.pyplot as plt
import scienceplots
plt.style.use(['science','grid'])

fig, ax = plt.subplots(figsize=(12, 5), layout='constrained')

def mpm(data):
    L = 2
    M = 2

    Y = []

    min_val = min(data)

    for i in range(len(data) - L):
        Y.append([0 for _ in range(L + 1)])
        for j in range(L + 1):
            Y[i][j] = data[i + j] - min_val

    _, _, Vh = LA.svd(np.array(Y), full_matrices=True)

    new_Vh = []
    if sum(Vh[0]) < sum(Vh[0] * -1):
        new_Vh.append(Vh[0] * -1)
    if Vh[1][0] > 0 and Vh[1][1] < 0 and Vh[1][2] > 0:
        new_Vh.append(Vh[1])
    elif Vh[1][0] < 0 and Vh[1][1] > 0 and Vh[1][2] < 0:
        new_Vh.append(Vh[1] * -1)
    elif Vh[2][0] > 0 and Vh[2][1] < 0 and Vh[2][2] > 0:
        new_Vh.append(Vh[2])
    elif Vh[2][0] < 0 and Vh[2][1] > 0 and Vh[2][2] < 0:
        new_Vh.append(Vh[2] * -1)

    V = np.transpose(new_Vh)

    V1 = np.delete(V, L, 0)
    V2 = np.delete(V, 0, 0)

    V1 = LA.pinv(np.transpose(V1))

    V2 = np.transpose(V2)

    computing_matrix = np.matmul(V1, V2)
    computing_matrix[0][0] = 0
    computing_matrix[1][0] = 1

    time_constants, vecs = LA.eig(computing_matrix)

    if time_constants[0] > 0 and time_constants[1] > 0:
        tc = min(time_constants)
    else:
        tc = max(time_constants)

    x = math.log(tc)
    t1 = abs(0.01 / x)

    return t1

tau = 0.80
sample_period = 0.01
ideal_samples = [1023 * np.exp(-(i * sample_period) / tau) for i in range(int(375))]

time_constant_estimations = []

snr = []
std_dev_perc = []

scum_snr = []
scum_std = []

vert_line_x = 0
vert_line_ymax = 0
horiz_line_y = 0
horiz_line_xmax = 0

for noise_std_dev in range(1, 33):
    for _ in range(100):
        noise = np.random.normal(0, noise_std_dev, size=len(ideal_samples))
        noisy_samples = ideal_samples + noise
        estimate = mpm(noisy_samples)
        time_constant_estimations.append(estimate)
    snr.append(20 * math.log(1023 / noise_std_dev, 10))
    std_dev_perc.append((np.std(time_constant_estimations) / tau))
    if noise_std_dev == 5:
        scum_snr.append(20 * math.log(1023 / noise_std_dev, 10))
        scum_std.append((np.std(time_constant_estimations) / tau))
        vert_line_x = 20 * math.log(1023 / noise_std_dev, 10)
        vert_line_ymax = (np.std(time_constant_estimations) / tau) * 18
        horiz_line_y = (np.std(time_constant_estimations) / tau)
        horiz_line_xmax = 20 * math.log(1023 / noise_std_dev, 10) / 87

ax.axvline(x=vert_line_x, ymax=vert_line_ymax, color='tab:red', label=r"SC$\mu$M's ADC", linestyle='--', linewidth=2)
ax.axhline(y=horiz_line_y, xmax=horiz_line_xmax, color='tab:red', linestyle='--', linewidth=2)
ax.plot(snr, std_dev_perc, color='tab:blue', marker='^', zorder=0, linewidth=2)
ax.scatter(scum_snr, scum_std, color='tab:red', marker='s', zorder=10)
ax.legend(loc='upper right')
ax.set_xlabel("SNR [dB]")
ax.set_ylabel(r"Normalized Standard Deviation $[\sigma$/$\tau]$")
secax = ax.secondary_yaxis('right', functions=(lambda x : x * tau, lambda y : y / tau))
secax.set_ylabel('Standard Deviation [s]')
ax.set_title(r"SNR vs. Standard Deviation of $\hat{\tau}$")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.show()
