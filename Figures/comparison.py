import matplotlib.pyplot as plt
import numpy as np
import scienceplots
plt.style.use(['science','grid'])
fig, ax = plt.subplots(1, 3, figsize=(14, 7), constrained_layout=True)

time_constants = [0.0263592, 0.0377928, 0.0651184, 0.0796184, 0.175216, 0.373376, 0.445952, 0.536888, 0.64604, 0.80072, 1.76144, 5.48584]
nominal_taus = np.array([0.020916, 0.0462, 0.110, 0.234, 0.404, 0.5, 1.058, 2.09, 4.599])
one_perc_tau = [0.01 * t for t in nominal_taus]
five_perc_tau = [0.05 * t for t in nominal_taus]

# Mean Absolute Error
mean_abs_errors = [0.000262747, 0.001034339, 0.001882469, 0.003390106, 0.003682061, 0.004372011, 0.00524067, 0.004635286, 0.004535988, 0.005226721, 0.012974679, 0.092524776]

ax[0].plot(time_constants, mean_abs_errors, label='Matrix Pencil Method', alpha=1, marker='p', linewidth=2)

ax[0].plot(nominal_taus, five_perc_tau, label=r'5\% of $\tau$', alpha=1, color="black", linestyle='--', linewidth=2)

ax[0].plot(nominal_taus,
            np.abs(
                np.array([
                    0.021575, 0.045671, 0.111, 0.233, 0.407, 0.499, 1.01,
                    2.099187, 4.549780
                ]) - nominal_taus),
            label="Exponential Fit",
            alpha=0.4,
            marker="^", 
            linewidth=2)
ax[0].plot(nominal_taus,
            np.abs(
                np.array([
                    0.022884, 0.049767, 0.117, 0.245, 0.417, 0.516, 1.03,
                    2.188900, 4.409927
                ]) - nominal_taus),
            label="Linear Fit",
            alpha=0.4,
            marker="v", 
            linewidth=2)
ax[0].plot(nominal_taus,
            np.abs(
                np.array([
                    0.022236, 0.048159, 0.115, 0.241, 0.414, 0.512, 1.03,
                    2.167384, 4.507946
                ]) - nominal_taus),
            label="Weighted Linear Fit",
            alpha=0.4,
            marker="o", 
            linewidth=2)
ax[0].plot(nominal_taus,
            np.abs(
                np.array([
                    0.022240, 0.043677, 0.104, 0.199, 0.331, 0.409, 0.826,
                    1.802195, 3.939816
                ]) - nominal_taus),
            label="Polynomial Fit",
            alpha=0.4,
            marker="s", 
            linewidth=2)

ax[0].set_yscale("log")
ax[0].set_xscale("log")
ax[0].grid(color='gray', linestyle='--', linewidth=0.5)

ax[0].legend()

ax[0].set_xlabel(r"Nominal Time Constant $\tau$ [s]", fontsize=17)
ax[0].set_ylabel("Mean Absolute Error [s]", fontsize=17)
ax[0].set_title("Mean Absolute Error", fontsize=18)

# Standard Error
std_errors = [4.80461E-05, 4.92733E-05, 0.000117763, 0.000131857, 0.000236828, 0.000478336, 0.000680023, 0.000765596, 0.000830664, 0.000933701, 0.002295489, 0.014506667]

ax[1].plot(time_constants, std_errors, label='Matrix Pencil Method', alpha=1, marker='p', linewidth=2)

ax[1].plot(nominal_taus, one_perc_tau, label=r'1\% of $\tau$', alpha=1, color="black", linestyle='--', linewidth=2)

ax[1].plot(nominal_taus,
            np.array([
                0.000604, 0.000472, 0.00189, 0.00202, 0.00301, 0.002800,
                0.00955, 0.024469, 0.031757
            ]),
            label="Exponential Fit",
            alpha=0.4,
            marker="^", 
            linewidth=2)
ax[1].plot(nominal_taus,
            np.array([
                0.000647, 0.000845, 0.00163, 0.00230, 0.00317, 0.00476,
                0.0133, 0.049733, 0.073143
            ]),
            label="Linear Fit",
            alpha=0.4,
            marker="v", 
            linewidth=2)
ax[1].plot(nominal_taus,
            np.array([
                0.000184, 0.000413, 0.00098, 0.00161, 0.00178, 0.00301,
                0.0103, 0.037237, 0.048494
            ]),
            label="Weighted Linear Fit",
            alpha=0.4,
            marker="o", 
            linewidth=2)
ax[1].plot(nominal_taus,
            np.array([
                0.000804, 0.001264, 0.00735, 0.00498, 0.00399, 0.00324,
                0.0136, 0.023325, 0.032916
            ]),
            label="Polynomial Fit",
            alpha=0.4,
            marker="s", 
            linewidth=2)

ax[1].set_yscale("log")
ax[1].set_xscale("log")
ax[1].grid(color='gray', linestyle='--', linewidth=0.5)

ax[1].legend()

ax[1].set_xlabel(r"Nominal Time Constant $\tau$ [s]", fontsize=17)
ax[1].set_ylabel("Standard Error [s]", fontsize=17)
ax[1].set_title("Standard Error", fontsize=18)

# Runtime Per Sample Processed
taus = [0.0263592, 0.0377928, 0.0651184, 0.0796184, 0.175216, 0.373376, 0.445952, 0.536888, 0.64604, 0.80072, 1.76144]
mpm_runtimes = [0.40797502, 0.39441134, 0.4048284, 0.4124817, 0.49551536, 0.67206296, 0.76896432, 0.85683466, 0.97628714, 1.12615582, 2.06911924]
mpm_n = [14.96, 20, 32.4, 39.16, 82.6, 175.56, 209.72, 252.66, 303.5, 375.06, 818.86]

wlg_runtimes = [0.07757604, 0.0949271, 0.13666074, 0.15716206, 0.29429476, 0.57120716, 0.67603036, 0.80067528, 0.92950658, 1.1346445, 2.2773667]
wlg_n = [9.42, 13.32, 22.88, 27.24, 59.9, 123.86, 147.88, 175.76, 206.86, 252.82, 517.88]

lg_runtimes = [0.04429412, 0.050796, 0.0705735, 0.08138224, 0.14729368, 0.28333072, 0.33320004, 0.39489886, 0.47220356, 0.57579634, 1.26155644]
lg_n = [13.24, 19.34, 30.88, 37.84, 79.92, 167.16, 198.84, 237.14, 285, 350.08, 781.94]

ax[2].plot(wlg_n, wlg_runtimes, label='Weighted Linear Fit', alpha=0.4, marker="o", color='red', linewidth=2)
ax[2].plot(lg_n, lg_runtimes, label='Linear Fit', marker="v", alpha=0.4, color='orange', linewidth=2)
ax[2].plot(mpm_n, mpm_runtimes, label='Matrix Pencil Method', marker='p', linewidth=2)

ax[2].set_yscale("log")
ax[2].set_xscale("log")
ax[2].grid(color='gray', linestyle='--', linewidth=0.5)

ax[2].legend(reverse=True)

ax[2].set_xlabel(r"Number of Samples Processed", fontsize=17)
ax[2].set_ylabel("Runtime [s]", fontsize=17)
ax[2].set_title("Runtime", fontsize=18)

plt.show()
