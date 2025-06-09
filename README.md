# Black Hole Trajectory Visualizer

A physics simulation project that visualizes particle trajectories around a black hole using the Schwarzschild metric.

## Overview

This project simulates the motion of particles in the gravitational field of a black hole, providing visual insights into orbital mechanics near extreme gravitational environments. The simulation uses numerical integration to solve the equations of motion and generates interactive plots showing the particle's path.

## Features

- **Schwarzschild Metric Implementation**: Accurate relativistic trajectory calculations
- **Visual Analysis**: Three-panel visualization showing:
  - Radial distance vs. time
  - Orbital angle evolution
  - 2D trajectory plot with event horizon
- **Multiple Scenarios**: Batch simulation for different angular momentum values
- **Event Horizon Detection**: Automatic detection when particles cross the event horizon

## Physics Parameters

- Gravitational constant: G = 6.67×10⁻¹¹
- Black hole mass: M = 10¹³ kg
- Particle mass: m = 1.0 kg
- Speed of light: c = 1.0 (normalized units)
- Event horizon radius: r = 2.0

## Usage

Run the main simulation:
```bash
python "BH Visualizer.py"
```

The program will generate visualizations and output the time taken for particles to reach the event horizon.

## Requirements

- NumPy
- Matplotlib
- Pandas

## Output

The simulation produces plots showing particle behavior around the black hole and prints inspection times for particles that fall into the black hole. 