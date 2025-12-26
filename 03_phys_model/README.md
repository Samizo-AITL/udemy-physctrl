# 03_phys_model — Why Control Becomes Difficult

This section introduces **physical models** as
*constraints on control behavior*.

Physical models explain why:
- the same controller does not always work
- switching is sometimes necessary

---

## Key Ideas (Only Three)

1. Real systems are nonlinear
2. Outputs do not scale linearly with inputs
3. Physical limits always exist

---

## Intuition First

- Gain works here, but not there
- More input does not always mean more output
- Saturation changes behavior

These effects are **not control problems**.
They are properties of the system itself.

---

## What We Do NOT Do Here

- No device physics
- No differential equations
- No control design

We only observe behavior.
