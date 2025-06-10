import matplotlib.pyplot as plt
import numpy as np
import scienceplots
plt.style.use(['science','grid'])
plt.figure(figsize=(12.5, 4.5))

time_constants = [0.0263592, 0.0377928, 0.0651184, 0.0796184, 0.175216, 0.373376, 0.445952, 0.536888, 0.64604, 0.80072, 1.76144, 5.48584]
nominal_taus = np.array([0.020916, 0.0462, 0.110, 0.234, 0.404, 0.5, 1.058, 2.09, 4.599])
one_perc_tau = [0.01 * t for t in nominal_taus]
five_perc_tau = [0.05 * t for t in nominal_taus]

# Mean Absolute Error
mean_abs_errors = [0.000262747, 0.001034339, 0.001882469, 0.003390106, 0.003682061, 0.004372011, 0.00524067, 0.004635286, 0.004535988, 0.005226721, 0.012974679, 0.092524776]

plt.subplot(1, 2, 1)
plt.plot(time_constants, mean_abs_errors, label='Matrix Pencil Method', alpha=1, marker='p')

plt.plot(nominal_taus, five_perc_tau, label=r'5\% of $\tau$', alpha=1, color="black", linestyle='--')

plt.plot(nominal_taus,
            np.abs(
                np.array([
                    0.021575, 0.045671, 0.111, 0.233, 0.407, 0.499, 1.01,
                    2.099187, 4.549780
                ]) - nominal_taus),
            label="Exponential Fit",
            alpha=0.4,
            marker="^")
plt.plot(nominal_taus,
            np.abs(
                np.array([
                    0.022884, 0.049767, 0.117, 0.245, 0.417, 0.516, 1.03,
                    2.188900, 4.409927
                ]) - nominal_taus),
            label="Linear Fit",
            alpha=0.4,
            marker="v")
plt.plot(nominal_taus,
            np.abs(
                np.array([
                    0.022236, 0.048159, 0.115, 0.241, 0.414, 0.512, 1.03,
                    2.167384, 4.507946
                ]) - nominal_taus),
            label="Weighted Linear Fit",
            alpha=0.4,
            marker="o")
plt.plot(nominal_taus,
            np.abs(
                np.array([
                    0.022240, 0.043677, 0.104, 0.199, 0.331, 0.409, 0.826,
                    1.802195, 3.939816
                ]) - nominal_taus),
            label="Polynomial Fit",
            alpha=0.4,
            marker="s")

plt.yscale("log")
plt.xscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.xlabel(r"Nominal Time Constant $\tau$ [s]", fontsize=17)
plt.ylabel("Mean Absolute Error [s]", fontsize=17)
plt.title("Mean Absolute Error", fontsize=18)

# Standard Error & CRLB
std_errors = [4.80461E-05, 4.92733E-05, 0.000117763, 0.000131857, 0.000236828, 0.000478336, 0.000680023, 0.000765596, 0.000830664, 0.000933701, 0.002295489, 0.014506667]

plt.subplot(1, 2, 2)
plt.plot(time_constants, std_errors, label='Matrix Pencil Method', alpha=1, marker='p')

plt.plot(nominal_taus, one_perc_tau, label=r'1\% of $\tau$', alpha=1, color="black", linestyle='--')

plt.plot(nominal_taus,
            np.array([
                0.000604, 0.000472, 0.00189, 0.00202, 0.00301, 0.002800,
                0.00955, 0.024469, 0.031757
            ]),
            label="Exponential Fit",
            alpha=0.4,
            marker="^")
plt.plot(nominal_taus,
            np.array([
                0.000647, 0.000845, 0.00163, 0.00230, 0.00317, 0.00476,
                0.0133, 0.049733, 0.073143
            ]),
            label="Linear Fit",
            alpha=0.4,
            marker="v")
plt.plot(nominal_taus,
            np.array([
                0.000184, 0.000413, 0.00098, 0.00161, 0.00178, 0.00301,
                0.0103, 0.037237, 0.048494
            ]),
            label="Weighted Linear Fit",
            alpha=0.4,
            marker="o")
plt.plot(nominal_taus,
            np.array([
                0.000804, 0.001264, 0.00735, 0.00498, 0.00399, 0.00324,
                0.0136, 0.023325, 0.032916
            ]),
            label="Polynomial Fit",
            alpha=0.4,
            marker="s")

plt.yscale("log")
plt.xscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()

plt.xlabel(r"Nominal Time Constant $\tau$ [s]", fontsize=17)
plt.ylabel("Standard Error [s]", fontsize=17)
plt.title("Standard Error", fontsize=18)

plt.show()
