import numpy as np
import matplotlib.pyplot as plt

# Time settings
dt = 0.01
t = np.arange(0, 5, dt)

# Reference (step input)
r = np.ones_like(t)

# Plant (1st-order system)
y = np.zeros_like(t)
u = np.zeros_like(t)

# PID gains
Kp = 4.0
Ki = 1.0
Kd = 0.1

e_prev = 0.0
e_int = 0.0

for i in range(1, len(t)):
    e = r[i] - y[i-1]
    e_int += e * dt
    e_der = (e - e_prev) / dt

    u[i] = Kp * e + Ki * e_int + Kd * e_der

    # Plant dynamics: dy/dt = -y + u
    y[i] = y[i-1] + dt * (-y[i-1] + u[i])

    e_prev = e

# Plot
plt.figure()
plt.plot(t, r, "--", label="reference")
plt.plot(t, y, label="output")
plt.xlabel("Time [s]")
plt.ylabel("Response")
plt.legend()
plt.grid()
plt.show()
