# Gravitational Wave Simulation from Binary Black Hole Systems

## Overview
This project aims to numerically solve Einstein’s field equations to model gravitational waves (GWs) emitted by Extreme Mass-Ratio Inspirals (EMRIs)—systems where a small black hole orbits a supermassive one. Our goal is to develop a stable and accurate algorithm to simulate the inspiral, compute orbital dynamics, and generate waveforms suitable for future space-based observatories like LISA.

## Objectives
- Develop a Runge-Kutta 4th order (RK4) solver for evolving second-order differential equations.
- Model the motion of a small mass $m$ around a large black hole $M \gg m$.
- Simulate orbital decay and time to merger (plunge).
- Visualize orbital trajectories and key physical quantities.

## Methodology
- **RK4 Integration:** Used for evolving geodesic and perturbed trajectories.
- **Central Force Model:** Simulates the Newtonian limit for early validation.
- **Python stack:** NumPy, Matplotlib, Pandas.

## Features
- Modular codebase for testing and extending ODE solvers
- Visualization tools for plotting $r(t)$, $\phi(t)$, and trajectories in polar and Cartesian coordinates
- Time-to-horizon detection logic for estimating merger timelines
- Data export to CSV for further analysis
- Jupyter notebook for interactive exploration and visualization

## Project Status (May 2025)
- RK4-based simulation of test particle inspiral around a single black hole completed
- Batch simulations for a range of angular momentum values ($L$) implemented
- Results exported to a combined CSV file
- Interactive Jupyter notebook for data analysis and visualization
- Next steps: Add gravitational self-force (GSF) effects and waveform generation

## Credits
- **Students:** Amit Kalaf, Adi Revach
- **Supervisor:** Dr. Jeremy Miller
- **Institution:** Academic College of Engineering, Computer Science Department
