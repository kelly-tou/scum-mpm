# Time Constant Estimation on a Low-Cost, Low-Power Microcontroller Using the Matrix Pencil Method

This repository contains the firmware and figure-generation code used in the paper:

**"Time Constant Estimation on a Low-Cost, Low-Power Microcontroller Using the Matrix Pencil Method"**

_Kelly L. Tou, Titan Yuan, Kristofer S. J. Pister_

The Matrix Pencil Method (MPM) is implemented on the Single-Chip Micro Mote (SCμM), a low-power, crystal-free, wireless system-on-chip for microrobotic and IoT applications. The SCμM features an on-chip 10-bit SAR ADC, an ARM Cortex M0 microprocessor, 64 kB of data and instruction memory each, and a 2.4 GHz transceiver.

## Contents

<pre> scum-mpm/
├── Firmware/           # C firmware for SCμM
│   ├── adc.c                      # SCμM ADC driver: configure ASC bits, trigger conversions via interrupt, and read or average samples
│   ├── adc.h
│   ├── adc_msb.c                  # Handle MSB wrap-around: extend raw 10-bit ADC samples into a continuous monotonic value
│   ├── adc_msb.h
│   ├── fixed_point.h              # Q44.20 fixed-point arithmetic: type definitions, conversions, basic ops (add, sub, mul, div, abs, pow, sqrt)
│   ├── gpio.c                     # Basic GPIO driver: init pins low, set/clear/toggle outputs, and handle external GPIO interrupts
│   ├── gpio.h
│   ├── matrix.c                   # Fixed-point matrix data structure: init, bounds-checked get/set, add, multiply, copy, and transpose
│   ├── matrix.h
│   ├── matrix_pencil_method.c     # Fixed-point matrix pencil method: build data/SVD matrices, compute eigenvalue, and extract signal time constant
│   ├── matrix_pencil_method.h
│   ├── memory_map.h               # SCμM memory map: peripheral base addresses and register access macros
│   ├── optical.c                  # Optical calibration driver: iteratively measure analog counters via SFD ISR and tune HF, LC, 2M RC, and IF clocks
│   ├── optical.h
│   ├── radio.c                    # SCμM radio driver: packet send/receive, channel calibration (LC sweep + FIR tuning), and interrupt handling
│   ├── radio.h
│   ├── rftimer.c                  # RF timer driver: init timer, schedule compare‐match callbacks and delays, and handle compare/capture interrupts
│   ├── rftimer.h
│   ├── scm3c_hw_interface.c       # SCμM hardware interface: configure analog scan chain, clocks (HF, 2 MHz RC, IF), DACs, LDOs, CRC, GPI/GPO, and peripheral initialization routines
│   ├── scm3c_hw_interface.h
│   ├── scum_defs.h                # SCμM definitions: default initial LC code and calibration reference target
│   ├── sensor_adc.c               # SCμM resistive-sensor demo: init hardware (clocks, ADC, RF timer), perform optical calibration, and periodically measure sensor time constant
│   ├── sensor_capacitor.c         # Sensor capacitor controller: cycle through configured capacitor masks and drive corresponding GPIOs for each mask
│   ├── sensor_capacitor.h
│   ├── sensor_gpio.c              # Sensor GPIO controller: configure analog-scan-chain enables, drive pins high/low/high-Z, and generate timed excitation pulses via RF timer
│   ├── sensor_gpio.h
│   ├── sensor_resistive.c         # Sensor resistive measurement: drive excitation, schedule ADC sampling via RF timer, accumulate readings in a state machine, and estimate the decay time constant
│   ├── sensor_resistive.h
│   ├── svd_3.c                    # Fixed-point SVD (right singular vectors): store AᵀA, then compute V via gradient ascent with orthogonal projection and cross-product enforcement
│   ├── svd_3.h
│   ├── uart.c                     # UART driver: interrupt-driven TX/RX with software XON/XOFF flow control, callbacks, and character escaping
│   ├── uart.h
│   ├── time_constant.c            # Time-constant estimator: buffer disambiguated ADC samples until decay completes, then compute exponential decay constant via matrix pencil method
│   ├── time_constant.h
│   ├── cm0dsasm.s                 # SCuM startup and interrupt vectors: define stack/heap regions, vector table, Reset_Handler, and IRQ entry stubs (masking/unmasking) that branch to C ISR routines
│   ├── retarget.c                 # Retarget C library I/O to UART: disable semihosting, stub FILE, and implement fgetc/fputc, uart_in/out, and _sys_exit for printf/scanf over memory‐mapped UART
│   ├── sensor_adc.uvoptx          # For compiling in Keil
│   └── sensor_adc.uvprojx         # For compiling in Keil
├── Figures/            # Python scripts for reproducing figures from the paper
│   ├── adc.py                     # Figure 2
│   ├── comparison.py              # Figure 5
│   ├── mean_std_plots.py          # Figure 4
│   └── snr.py                     # Figure 3
└── README.md           # This file </pre>

## Requirements

- SCμM v3c board
- nRF52840 board (for flashing and serial comm)
- UART connection configured to 19200 baud
- External capacitor and resistor, as decribed in the paper

## Getting Started

**Boot SCμM:** https://crystalfree.atlassian.net/wiki/spaces/SCUM/pages/1901559821/Sulu+Programming+With+nRF+Setup

**Compile Firmware For SCμM:** https://crystalfree.atlassian.net/wiki/spaces/SCUM/pages/2378596375/Building+SCuM+Firmware 
