# BH_Project

This project simulates the motion of a small object around a massive black hole using a simple central force model. The simulation uses the Runge-Kutta 4th order (RK4) method to solve the equations of motion and visualizes:

- The radial distance from the black hole over time
- The orbital angle over time
- The trajectory in the x–y plane

## Features

- Detects when the object crosses the event horizon
- Plots the event horizon and the black hole
- Adjustable parameters for mass, angular momentum, and initial conditions

## How to Run

1. Make sure you have Python and the required libraries:
    ```sh
    pip install numpy matplotlib
    ```
2. Run the simulation:
    ```sh
    python "BH code.py"
    ```

## Output

- Three plots: radial distance vs. time, angle vs. time, and the orbit path
- Console output indicating if/when the object reaches the event horizon

## File Structure

- `BH code.py` — Main simulation and plotting script

## Parameters

You can adjust the following parameters in the script:
- `G` — Gravitational constant
- `M` — Mass of the black hole
- `L` — Angular momentum
- `r0`, `v0`, `phi0` — Initial conditions

---

Final project on EMRI system with 2 black holes (currently simulates one black hole).
