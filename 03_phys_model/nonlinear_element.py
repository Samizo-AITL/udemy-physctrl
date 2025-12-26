"""
nonlinear_element.py
Simple nonlinear input-output relationship
"""

import numpy as np

def nonlinear_block(u):
    return u**3  # intentionally nonlinear

inputs = np.linspace(-2, 2, 9)

print("Input -> Output")
for u in inputs:
    print(f"{u: .2f} -> {nonlinear_block(u): .2f}")
