"""
vi_curve_demo.py
Simple V-I curve intuition
"""

import numpy as np

voltages = np.linspace(0, 5, 6)

def vi_relation(v):
    if v < 1.0:
        return 0.0
    elif v < 3.0:
        return (v - 1.0) * 0.5
    else:
        return 1.0

print("V -> I")
for v in voltages:
    print(f"{v: .1f} V -> {vi_relation(v): .2f} A")
