# 02_fsm — Why Switching Is Needed

This section introduces **FSM (Finite State Machine)** as a
*supervisory decision layer*.

FSM does NOT replace PID.
FSM decides **which mode of control should be active**.

---

## Key Ideas (Only Three)

1. One control law is not enough for all situations
2. Systems behave differently depending on state
3. FSM selects modes based on conditions

---

## Intuition Example

- Startup vs Steady operation
- Safe mode vs Normal mode
- Saturation vs Linear region

FSM answers:
> "Which control behavior should be used **now**?"

---

## What We Do NOT Do Here

- No state transition tables
- No formal automata theory
- No UML diagrams

We start with simple conditional logic.
