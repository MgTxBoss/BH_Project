import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# === CONSTANTS ===
G = 6.67e-11
M = 1e13
m = 1.0
L = 46.0                             #angular momentum .
r_event_horizon = 2.0

# === INITIAL CONDITIONS ===
r0, v0, phi0 = 10.0, -0.05, 0.0      #Distance , Speed , Angle .
Y0 = np.array([r0, v0, phi0])

# === SIM PARAMETERS ===
t0, tf, dt = 0.0, 1000.0, 0.01       # Starting time , Ending time ,  step size .

def central_force_rhs(t, Y):
    r, v, phi = Y
    return np.array([
        v,
        (L**2)/(m**2 * r**3) - G*M/r**2,
        L/(m*r**2)
    ])

def rk4_step(f, t, y, dt):
    k1 = f(t, y)
    k2 = f(t + dt/2, y + dt/2*k1)
    k3 = f(t + dt/2, y + dt/2*k2)
    k4 = f(t + dt,   y + dt*k3)
    return y + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

# === RUN SIMULATION ===
ts, Ys = [t0], [Y0.copy()]
t, Y = t0, Y0.copy()
inspiral_time = None

while t < tf:
    if Y[0] <= r_event_horizon:
        inspiral_time = t
        print(f"Reached event horizon at r = {Y[0]:.4f}.")
        break
    Y = rk4_step(central_force_rhs, t, Y, dt)
    t += dt
    ts.append(t)
    Ys.append(Y.copy())

Ys   = np.array(Ys)
rs   = Ys[:,0]
phis = Ys[:,2]
xs   = rs * np.cos(phis)
ys   = rs * np.sin(phis)

# === SINGLE FIGURE WITH 3 SUBPLOTS ===
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# -- r(t)
ax1.plot(ts, rs, label="r(t)")
ax1.axhline(r_event_horizon, color='red', linestyle='--', label="Event horizon (r=2)")
ax1.set_ylabel("Radius r")
ax1.set_title("Radial distance vs. time")
ax1.grid(True)
ax1.legend()

# -- φ(t)
ax2.plot(ts, phis, color='orange', label="φ(t)")  # or if we want to see monotonic graph
ax2.set_ylabel("Angle φ (rad)")
ax2.set_title("Orbital angle vs. time")
ax2.grid(True)
ax2.legend()

# -- Orbit in the x–y plane
ax3.plot(xs, ys, label="Orbit path")
ax3.plot(0, 0, 'ro', label="Black hole")
horizon = plt.Circle((0,0), r_event_horizon, color='red', fill=False, linestyle='--')
ax3.add_patch(horizon)
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax3.set_aspect('equal', 'box')
ax3.set_title("Trajectory around black hole")
ax3.grid(True)
ax3.legend()

# === APPLY AUTOMATIC LAYOUT THEN MANUAL TUNING ===
fig.tight_layout()   # first try automatic spacing

# then override with precise manual adjustments:
fig.subplots_adjust(
    left=0.10,    # fraction of figure width from left edge
    right=0.95,   # fraction of figure width from right edge
    top=0.94,     # fraction of figure height from top edge
    bottom=0.06,  # fraction of figure height from bottom edge
    hspace=0.30,  # height spacing between rows of subplots
    wspace=0.20   # width spacing between columns (unused here)
)

plt.show()

# === FINAL STATUS ===
if inspiral_time is not None:
    print(f"Inspiral time to event horizon: {inspiral_time:.4f} seconds")
else:
    print("Did not reach the event horizon within simulation time.")

# === DATA COLLECTION FOR MULTIPLE L ===
def run_simulation_for_L(L_value):
    ts, Ys = [t0], [Y0.copy()]
    t, Y = t0, Y0.copy()
    while t < tf:
        if Y[0] <= r_event_horizon:
            break
        # Update L in the rhs function
        def rhs(t, Y):
            r, v, phi = Y
            return np.array([
                v,
                (L_value**2)/(m**2 * r**3) - G*M/r**2,
                L_value/(m*r**2)
            ])
        Y = rk4_step(rhs, t, Y, dt)
        t += dt
        ts.append(t)
        Ys.append(Y.copy())
    Ys = np.array(Ys)
    df = pd.DataFrame({
        't': ts,
        'r': Ys[:,0],
        'v': Ys[:,1],
        'phi': Ys[:,2]
    })
    return df

# --- Run for L=1..10, then 20,30,...,100 ---
L_values = list(range(1, 11)) + list(range(20, 101, 10))
L_dfs = {}
for L_val in L_values:
    L_dfs[L_val] = run_simulation_for_L(L_val)
    print(f"Simulated for L={L_val}")

# Optional: Save to CSV files
# for L_val, df in L_dfs.items():
#     df.to_csv(f"orbit_data_L{L_val}.csv", index=False)
