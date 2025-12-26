"""
saturation_model.py
Simple saturation behavior
"""

def saturate(u, limit=1.0):
    return max(min(u, limit), -limit)

inputs = [-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0]

print("Input -> Saturated Output")
for u in inputs:
    print(f"{u: .1f} -> {saturate(u): .1f}")
