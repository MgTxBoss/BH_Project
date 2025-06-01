# Black Hole Trajectory Simulation – Project Overview

## Overview
This project numerically simulates the motion of a test particle (small black hole or star) around a supermassive black hole, focusing on the effect of angular momentum (L) on orbital stability and inspiral into the event horizon. The simulation uses a Runge-Kutta 4th order (RK4) solver and supports both Newtonian and relativistic (Schwarzschild) models. Results are visualized and compared with historical data, and the code is modular for future extensions such as gravitational self-force and waveform generation.

## Objectives
- Develop a robust RK4 solver for evolving second-order differential equations in black hole systems
- Model the motion of a small mass $m$ around a large black hole $M \gg m$
- Simulate orbital decay, time to event horizon, and stability as a function of angular momentum $L$
- Visualize orbital trajectories, phase space, and key physical quantities
- Export results to CSV for further analysis and comparison
- Provide an interactive Jupyter notebook for exploration and visualization

## Methodology
- **RK4 Integration:** Used for evolving geodesic and perturbed trajectories
- **Central Force Model:** Simulates both Newtonian and relativistic (Schwarzschild) limits
- **Python stack:** NumPy, Matplotlib, Pandas

## Features
- Modular codebase for testing and extending ODE solvers
- Visualization tools for plotting $r(t)$, $\phi(t)$, and trajectories in polar and Cartesian coordinates
- Batch simulations for a range of angular momentum values ($L$)
- Time-to-horizon detection logic for estimating merger timelines
- Data export to CSV for further analysis
- Jupyter notebook for interactive analysis, including comparison to historical CSV data

## Project Status (June 2025)
- RK4-based simulation of test particle inspiral around a single black hole completed
- Batch simulations for a range of angular momentum values ($L$) implemented
- Results exported to a combined CSV file (`all_orbits_data.csv`)
- Interactive Jupyter notebook for data analysis and visualization, including comparison to historical runs
- Next steps: Add gravitational self-force (GSF) effects and waveform generation

## Credits
- **Students:** Amit Kalaf, Adi Revach
- **Supervisor:** Dr. Jeremy Miller
- **Institution:** SCE Academic College of Engineering, Computer Science Department
