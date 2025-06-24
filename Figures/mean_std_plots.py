import matplotlib.pyplot as plt
import scienceplots
plt.style.use(['science','grid'])
plt.figure(figsize=(8, 2))

time_constants = [0.0263592, 0.0377928, 0.0651184, 0.0796184, 0.175216, 0.373376, 0.445952, 0.536888, 0.64604, 0.80072, 1.76144, 5.48584, 8.00632]

# Mean Absolute Error
mean_abs_errors = [0.000262747, 0.001034339, 0.001882469, 0.003390106, 0.003682061, 0.004372011, 0.00524067, 0.004635286, 0.004535988, 0.005226721, 0.012974679, 0.092524776, 0.046186085]
two_perc_tc = [0.02 * tc for tc in time_constants]

plt.subplot(1, 2, 1)
plt.plot(time_constants, two_perc_tc, color='tab:red', label=r'2\% of $\tau$', linestyle='--', linewidth=2)
plt.plot(time_constants, mean_abs_errors, color='tab:blue', label='Measured', marker='^', linewidth=2)
plt.yscale("log")
plt.xscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)

handles, labels = plt.gca().get_legend_handles_labels()
order = [1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order], markerfirst=True)

plt.xlabel(r"Nominal Time Constant $\tau$ [s]")
plt.ylabel("Mean Absolute Error [s]")
plt.title(r"Mean Absolute Error of $\hat{\tau}$")

# Standard Error & CRLB
std_errors = [4.80461E-05, 4.92733E-05, 0.000117763, 0.000131857, 0.000236828, 0.000478336, 0.000680023, 0.000765596, 0.000830664, 0.000933701, 0.002295489, 0.014506667, 0.007340953]
pt_two_perc_tc = [0.002 * tc for tc in time_constants]
crlb_std_errors = [2.9126063298385544e-05, 3.5439932798316423e-05, 4.694067847936402e-05, 5.203215355267126e-05, 7.770866739274989e-05, 0.00011333705907871593, 0.000123771280438124, 0.00013616927945015738, 0.0001494330839933579, 0.00016635170975759766, 0.0002467486179169047, 0.0004349786755466315, 0.0005255079022829654]

plt.subplot(1, 2, 2)
plt.plot(time_constants, pt_two_perc_tc, color='tab:red', label=r'0.2\% of $\tau$', linestyle='--', linewidth=2)
plt.plot(time_constants, crlb_std_errors, color='tab:green', label='CRLB', linestyle='-.', linewidth=2)
plt.plot(time_constants, std_errors, color='tab:blue', label='Measured', marker='^', linewidth=2)
plt.yscale("log")
plt.xscale("log")
plt.grid(color='gray', linestyle='--', linewidth=0.5)

handles, labels = plt.gca().get_legend_handles_labels()
order = [2, 1, 0]
plt.legend([handles[i] for i in order], [labels[i] for i in order], markerfirst=True)

plt.xlabel(r"Nominal Time Constant $\tau$ [s]")
plt.ylabel("Standard Error [s]")
plt.title(r"Standard Error of $\hat{\tau}$")

plt.show()
